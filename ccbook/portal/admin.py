from django.contrib import admin
from .models import *

admin.site.register([Navigation, Rank, Classify, Book, Chapter])
