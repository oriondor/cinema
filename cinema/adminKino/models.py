import os
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils.translation import ugettext_lazy as _
#from django.core.files.storage import FileSystemStorage

#fs = FileSystemStorage(location='/media/photos')

class Film(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=1000)
	main_image = models.ImageField(upload_to='films', default='none')
	trailer_link = models.CharField(max_length=100)
	cinema_type = ArrayField(models.CharField(max_length=4),size=3)
	seo_URL = models.CharField(max_length=100)
	seo_title = models.CharField(max_length=100)
	seo_keywords = ArrayField(models.CharField(max_length=100))
	seo_description = models.CharField(max_length=1000)

class FilmImage(models.Model):
	film = models.ForeignKey('Film',on_delete=models.CASCADE)
	image = models.ImageField(upload_to='films')
	

@receiver(models.signals.post_delete, sender=Film)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.main_image:
        if os.path.isfile(instance.main_image.path):
            os.remove(instance.main_image.path)

@receiver(models.signals.post_delete, sender=FilmImage)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)



class UserManager(BaseUserManager):
	"""Define a model manager for User model with no username field."""

	use_in_migrations = True

	def _create_user(self, email, password, **extra_fields):
		"""Create and save a User with the given email and password."""
		if not email:
			raise ValueError('The given email must be set')
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password=None, **extra_fields):
		"""Create and save a regular User with the given email and password."""
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		"""Create and save a SuperUser with the given email and password."""
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		return self._create_user(email, password, **extra_fields)




class User(AbstractUser):
	"""User model."""

	username = None
	email = models.EmailField(_('email address'), unique=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	objects = UserManager() 