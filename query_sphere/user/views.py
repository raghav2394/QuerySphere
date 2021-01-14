from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import  CreateUserForm,QueryForm

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import QuerySerializer,MyTokenObtainPairSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated,AllowAny

class QueryViewset(viewsets.ModelViewSet):
	queryset= Query.objects.all()
	serializer_class=QuerySerializer
	authentication_classes=[JWTAuthentication]
	permission_classes=[AllowAny]

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'user/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'user/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def home(request):
	form=QueryForm()
	if request.method == 'POST':
		form = QueryForm(request.POST)
		if form.is_valid():

			name=form.cleaned_data['name']
			email=form.cleaned_data['email']
			query=form.cleaned_data['query']
			q=Query(name=name,email=email,query=query)
			q.save()
			messages.success(request, 'Query sent to mentor' )

			return redirect('home')
			

	context = {'form':form}
	return render(request, 'user/dashboard.html', context)	



