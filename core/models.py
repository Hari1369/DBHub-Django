from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

class TestModel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.name

    class Meta:
        db_table="optimizer"
        
        
        
class Client(TenantMixin):
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table="Client_optimizer"
    
class Domain(DomainMixin):
    pass