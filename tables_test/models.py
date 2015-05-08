from django.db import models

# Create your models here.
class Person(models.Model):
	first_name = models.CharField(verbose_name="first name", max_length=200)
	last_name = models.CharField(verbose_name="last name", max_length=200)
	age = models.IntegerField(verbose_name="age")

	@property
	def calculate(self):
		return u"%s %s <b>Mucha Lucha<b>" % (self.first_name, self.last_name)