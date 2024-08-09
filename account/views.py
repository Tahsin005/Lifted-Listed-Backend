from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from rest_framework import viewsets
from . models import UserAccount
from . serializers import UserAccountSerializer, UserRegistrationSerializer, UserLoginSerializer, UserProfileUpdateSerializer, PasswordChageSerializer,AllUserSerializer
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes

from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
# Create your views here.
class UserAccountViewSet(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    
class UserRegistrationSerializerViewSet(APIView):
    serializer_class = UserRegistrationSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            
            token = default_token_generator.make_token(user)
            print('Token', token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print('Uid', uid)
            
            confirm_link = f"https://lifted-listed-backend.onrender.com/user/active/{uid}/{token}"
            

            email_subject = "Confirm Your Email"
            email_body = render_to_string('confirm_email.html', {'confirm_link': confirm_link})
            
            email = EmailMultiAlternatives(email_subject, '', to=[user.email]) 
            email.attach_alternative(email_body, "text/html")
            
            email.send() 
            
            return Response('Check your email for confirmation')
        return Response(serializer.errors)

def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None
        
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Your account has been verified. You can now go to the login page to login')
    else:
        return HttpResponse('Your account has not been verified')
# def activate(request, uid64, token):
#     try:
#         uid = urlsafe_base64_decode(uid64).decode()
#         user = User._default_manager.get(pk=uid)
#     except(User.DoesNotExist):
#         user = None
        
#     if user is not None and default_token_generator.check_token(user, token):
#         user.is_active = True
#         user.save()
#         return redirect('login')
#     else:
#         return redirect('login')

class UserLoginApiView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=self.request.data)
        
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            
            user = authenticate(username=username, password=password)
            
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                print(token, _)
                login(request, user)
                return Response({'token': token.key, 'user_id' : user.id})
            else:
                return Response({'error': 'Invalid Credentials'})
        return Response(serializer.errors)
    
class UserLogoutApiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        if request.user.auth_token:
            request.user.auth_token.delete()
        logout(request)
        return redirect('login')
    
class UserProfileUpdateApiView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileUpdateSerializer
    
class PasswordChangeApiView(APIView):
    def post(self, request):
        serializer = PasswordChageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Password changed successfully'})
        return Response(serializer.errors)
    

class AllUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AllUserSerializer