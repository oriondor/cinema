from django.shortcuts import render, redirect
from .models import Film, FilmImage
from django.contrib.auth.decorators import user_passes_test

def check_admin(user):
	return user.is_staff

@user_passes_test(check_admin)
def home(request):
	context={'cont':'Выберите категорию'}
	return render(request,'home.html',context)

@user_passes_test(check_admin)
def films(request,methods=["POST"]):
	if request.method == "POST":
		r = request.POST
		seo_keywords = r['seo_kwds'].split(' ')
		checkboxes=[]
		trailer_link = r['trailer_link']
		if trailer_link[:4]!='http':
			trailer_link = 'https://'+trailer_link
		for param in r:
			if param[:5]=="check":
				checkboxes.append(r[param])
		f = Film(name = r['film_name'],description=r['description'], \
			main_image = request.FILES['main_photo'],trailer_link = trailer_link, \
			cinema_type=checkboxes,seo_URL=r['seo_url'], seo_title=r['seo_title'], \
			seo_keywords=seo_keywords, seo_description=r['seo_description'])
		f.save()
		for image in request.FILES.getlist('add_photos'):
			f_imgs = FilmImage(film=f, image=image)
			f_imgs.save()
		return redirect('films')
	films = Film.objects.all()
	context={'films':films}
	return render(request,'films.html',context)

@user_passes_test(check_admin)
def delete(request,del_id,methods=["GET"]):
	instance = Film.objects.filter(id=del_id)	
	instance.delete()
	return redirect('films')


@user_passes_test(check_admin)
def film(request,film_id):
	film = Film.objects.get(id=film_id)
	other_photos_objects = FilmImage.objects.filter(film=film)
	print(other_photos_objects)
	other_photos = []
	for item in other_photos_objects:
		other_photos.append(item)
	context = {
	'film':film,
	'other_photos':other_photos
	}
	return render(request, 'film_card.html', context)