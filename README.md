# cinema

Example cinema website with admin panel for viewing and creating films
There are two admin-panels:
/admin
/adminka
To use admin panels you should do './manage.py createsuperuser' first and login as superuser through login page

This version doesn't provide any functionality for customization of view (banners, logos) through admin panel. By now all of the banners are hardcoded.

It's required to use this code over your own django project with your own settings.py file that would contain your own database settings. You should use Postres for this project.
Just copy the code of the apps and urls from project to your new django project, run migrations and your're all set!

All dependencies are in requirements.txt
