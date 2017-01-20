from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
	"""Topic user is learning about"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User)

	def __str__(self):
		"""Return string rep of the model"""
		return self.text


# class Memory(models.Model):
# 	"""A sample memory"""
# 	text = models.CharField(max_length=200)
# 	date_added = models.DateTimeField(auto_now_add=True)
#
# 	class Meta:
# 		verbose_name_plural = 'memories'
#
# 	def __str__(self):
# 		"""A sample representation"""
# 		return self.text

class Entry(models.Model):
	"""Specific something about topic"""
	topic = models.ForeignKey(Topic)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		"""Return string rep of the model"""
		return self.text[:50] + "..."

