from django.db import models

class Urls(models.Model):
    original_url = models.URLField(unique=True)
    short_url = models.URLField(unique=True)
    visit_count = models.IntegerField(default=0)


