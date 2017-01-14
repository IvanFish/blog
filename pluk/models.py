from django.contrib.auth.models import User
from django.db import models
import django.utils
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings




SHORT_TEXT_LEN = 500

class Article (models.Model):
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=django.utils.timezone.now)
    #text = models.TextField()
    text = RichTextUploadingField(blank=True, default='')
    likes = models.IntegerField(verbose_name='Нравится', default=0)
    dislikes = models.IntegerField(verbose_name='Не нравится', default=0)

    user = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_short_text (self):
        if len(self.text) > SHORT_TEXT_LEN:
            return self.text [:SHORT_TEXT_LEN]
        else:
            return self.text

class Comment(models.Model):
    article = models.ForeignKey('pluk.Article', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=django.utils.timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class UserProfile(models.Model):
    # Эта строка обязательна. Она связывает UserProfile с экземпляром модели User.
    user = models.OneToOneField(User)

    # Дополнительные атрибуты, которые мы хотим добавить.
    website = models.URLField(blank=True)


    # Переопределяем метод __unicode__(), чтобы вернуть что-либо значимое! Используйте __str__() в Python 3.*
    def __str__(self):
        return self.user.username
        
        
class UserLikes(models.Model):
    class Meta:
        db_table = 'app_blog_user_likes'
        verbose_name = 'оценку пользователя'
        verbose_name_plural = 'Оценки пользователей'
    UserModel = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')
    user = models.ForeignKey(UserModel, verbose_name="Пользователь")
    article = models.ForeignKey(Article, verbose_name="Статья")
    like = models.BooleanField(verbose_name="Нравится", default=False)
    dislike = models.BooleanField(verbose_name="Не нравится", default=False)
    
    def __str__(self):
        return self.user.username














