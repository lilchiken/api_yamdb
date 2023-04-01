from django.contrib import admin

from reviews.models import (User, Review, Comment, Title, Genre, Category)


admin.site.register(User, Review, Comment, Title, Genre, Category)
