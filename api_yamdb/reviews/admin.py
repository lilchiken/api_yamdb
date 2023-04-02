from django.contrib import admin

from reviews.models import (User, Title, Category,
                            Genre, Review, Comment)

admin.site.register(User)
admin.site.register(Title)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Comment)
