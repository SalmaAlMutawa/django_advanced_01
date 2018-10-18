from django.db import models
from stores.models import Store

# Create your models here.
class Inventory (models.Model):
	name = models.TextField()
	store = models.ForeignKey(Store ,default=1, on_delete=models.CASCADE)
	# inventory_choices = (
	# 	(empty, 'Empty'),
	# 	(not_empty, 'Not Empty'),
	# )
	is_empty = models.BooleanField(default = True)
	last_updated = models.DateTimeField()
	
	def __str__(self):
		return self.name