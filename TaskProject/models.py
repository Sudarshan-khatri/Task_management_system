from django.db import models
from Account.models import UserModel

# Create your models here.
class ProjectModel(models.Model):
    Status_Choice=[
        ('PLANNING','Planning'),
        ('ACTIVATE','Activate'),
        ('ON_HOLD','On_hold'),
        ('COMPLETED','Completed'),
        ('CANCELLED','Cancelled'),
    ]
    name=models.CharField(max_length=300,null=True,blank=True)
    description=models.TextField(max_length=4000,null=True,blank=True)
    status=models.CharField(max_length=40,choices=Status_Choice,default='Planning')
    start_date=models.DateTimeField(null=True,blank=True)
    end_date=models.DateTimeField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey('Account.UserMOdel',on_delete=models.CASCADE,null=True,related_name='project_name')
    members=models.ManyToManyField(UserModel,related_name='team')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering=['-created_at']