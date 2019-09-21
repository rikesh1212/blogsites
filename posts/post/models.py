from django.db import models

# Create your models here.
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE,)
    image = models.ImageField()
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/{}/".format(self.slug)

    def get_update_url(self):
        return "/{}/update/".format(self.slug)

    def get_delete_url(self):
        return "/{}/delete/".format(self.slug)


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    email = models.EmailField()
    cellphone_num = models.IntegerField()  #+"977"

    def __str__(self):
        return self.user.username




