from django.contrib import admin
from pluk.models import Article, Comment
from pluk.models import UserProfile

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(UserProfile)