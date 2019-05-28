from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    company_name = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    zip = models.IntegerField()
    email = models.EmailField()
    web = models.URLField()
    age = models.IntegerField()

    class Meta:
        ordering = ['id']
