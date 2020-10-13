from django.db import models


class Bulletin(models.Model):
    body = models.TextField()