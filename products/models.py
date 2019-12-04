from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Animal(models.Model):
	"""docstring for ClassName"""
	animal_id = models.CharField(max_length = 20)
	animal_variety = models.CharField(max_length = 20)
	animal_sex = models.CharField(max_length = 10)
	animal_old = models.CharField(max_length = 10)
	animal_size = models.CharField(max_length = 20)
	animal_color = models.CharField(max_length = 10)
	animal_from = models.CharField(max_length = 50)
	animal_health = models.CharField(max_length = 50)
	
	animal_remark = models.TextField(max_length = 10)
	animal_image = models.ImageField(upload_to = 'images/')

	animal_owner = models.ForeignKey(User, on_delete = models.CASCADE)

	pub_data = models.DateTimeField()
	def __str__(self):
		return self.animal_id 

