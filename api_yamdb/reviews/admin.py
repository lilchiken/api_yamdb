from django.contrib import admin
from reviews.models import Title, Genre, Category

admin.site.register(Title, Genre, Category)