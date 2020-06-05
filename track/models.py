from django.db import models

# Create your models here.
class home(models.Model):
	
	#l_name=models.CharField(max_length=200)
	img=models.ImageField(upload_to='')
	