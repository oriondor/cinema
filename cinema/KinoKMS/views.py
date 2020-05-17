from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from adminKino.models import Film, FilmImage,User

from datetime import date


def home(request):
	months = ['zero','Января','Февраля','Марта','Апреля','Мая','Июня','Июля','Августа','Сентября','Октября','Ноября','Декабря']
	films = Film.objects.all()
	today = date.today()
	print("Today's date:", today)
	context={
	'films':films,
	'day': f'{today.day} {months[today.month]}'
	}
	return render(request,'main.html', context)

def afisha(request,film="all"):
	if film=='all':
		films = Film.objects.all()
		context={'films':films}
		return render(request,'afisha.html', context)
	else:
		film = Film.objects.get(id=film)
		other_photos_objects = FilmImage.objects.filter(film=film)
		print(other_photos_objects)
		other_photos = []
		for item in other_photos_objects:
			other_photos.append(item)
		context = {
		'film':film,
		'other_photos':other_photos
		}
		return render(request,'film.html', context)

def login_view(request, methods=["POST"]):
	if request.method=="POST":
		if request.POST.get('Login')=='Login':
			print(request.POST['log_mail'])
			user = authenticate(email=request.POST['log_mail'], password=request.POST['log_pass'])
			#print(user)
			if user is not None:
				print('redirectin to homepage...')
				login(request, user)
				return redirect('main')
			else:
				return redirect('login_view')
		elif request.POST.get('Login')=="Registration":
			user = User.objects.create_user(email=request.POST['reg_mail'], password=request.POST['reg_pass'])
			user.first_name=request.POST['first_name']
			user.last_name=request.POST['last_name']
			user.save()
			return redirect('login_view')
		else:
			return redirect('login_view')
	context = {}
	return render(request,'login.html',context)


def logout_view(request):
    logout(request)
    return redirect('home')