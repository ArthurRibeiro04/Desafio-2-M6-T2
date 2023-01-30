from django.db import models

class Operation(models.Model):
    Transaction_type = models.CharField(max_length=100)
    Data = models.CharField(max_length=20)
    Value = models.CharField(max_length=100)
    CPF = models.CharField(max_length=100)
    Card = models.CharField(max_length=100)
    Time = models.CharField(max_length=100)
    Owner = models.CharField(max_length=100)
    Shop_name = models.CharField(max_length=100)
    
    def __repr__(self) -> str:
        return f'<Operation [{self.pk}] - {self.Transaction_type} - {self.Owner} - {self.Shop_name}>'
