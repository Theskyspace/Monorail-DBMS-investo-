from django.db import models

class search(models.Model):
	searches = models.CharField(max_length=30)