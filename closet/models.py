from django.db import models
from django.contrib.auth.models import User

class InventoryItem(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=100)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, blank=True, null=True)
    data_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def _str_(self):
        return self.name
    
class Category(models.Model):
	name = models.CharField(max_length=200)
	class Meta:
		verbose_name_plural = 'categories'
	def __str__(self):
		return self.name