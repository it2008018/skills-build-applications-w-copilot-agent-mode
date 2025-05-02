# filepath: octofit-tracker/backend/octofit_tracker/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fitness',  # Add this line
]

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',  # Name of your MongoDB database
    }
}