from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
<<<<<<< HEAD
ALLOWED_HOSTS = ['*']

#update here
=======
ALLOWED_HOSTS = ['0.0.0.0', 'bitsalumniclub-api.herokuapp.com', '127.0.0.1']

# adding few changes here 
>>>>>>> 0241d8008a173ba974ccc9aca0714d3229e31873
