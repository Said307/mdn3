


from django.db import models





class ExpensiveProductsManager(models.Manager):
    
    def all_expensive(self):
        return self.get_queryset().filter(price__gt=1000)