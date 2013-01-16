from django.db import models

class Starter(models.Model):
	title = models.CharField(max_length=120)
	body = models.TextField()