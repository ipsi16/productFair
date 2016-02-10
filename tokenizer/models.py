from django.db import models

# Create your models here.
class Question(models.Model):
	
	id = models.IntegerField(primary_key=True)
	question_text = models.CharField(max_length=300)
	volunteer = models.CharField(max_length=200,default='Kamini')
	answer = models.CharField(max_length=200)

