import os
from django.conf.urls import url
from django.conf import settings
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application

DEBUG = (os.environ.get("DEBUG", "on") == "on");
SECRET_KEY = (os.environ.get("SECRET_KEY", os.urandom(32)));
ALLOWED_HOSTS = (os.environ.get("ALLOWED_HOSTS", "localhost, 127.0.0.1").split(','));

def index(request):
	return (HttpResponse("Hello world"));

urlpatterns = (
	url(r'^$', index),
);

settings.configure(
	DEBUG = DEBUG,
	SECRET_KEY = SECRET_KEY,
	ALLOWED_HOSTS = ALLOWED_HOSTS,
	ROOT_URLCONF = __name__,
	MIDDLEWARE_CLASSES = (
		"django.middleware.common.CommonMiddleware",
		"django.middleware.csrf.CsrfViewMiddleware",
		"django.middleware.clickjacking.XFrameOptionsMiddleware",
	),
);

application = get_wsgi_application();

if __name__ == "__main__":
	import sys
	from django.core.management import execute_from_command_line

	execute_from_command_line(sys.argv);
