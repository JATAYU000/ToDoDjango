from django.db import models
from django.utils import timezone 
#to take date and give to database at the time of entry
from django.contrib.auth.models import User
#importing user data from auth models
from django.urls import reverse

class Task(models.Model):
	taskname = models.CharField(max_length=200)
	status = models.BooleanField(default=True)
	description = models.TextField(null = True,blank=True)
	date = models.DateTimeField(default = timezone.now)
	user = models.ForeignKey(User, on_delete=models.CASCADE) #to delete tasks if user is deleted
	
	def __str__(self):
		return self.taskname
		# to print thew task name in the objects.all() command

	def get_absolute_url(self):
		return reverse('task-detail',kwargs={'pk':self.pk})