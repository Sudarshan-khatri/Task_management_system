from django.db import models
from Account.models import UserModel
from TaskProject.models import ProjectModel

# Create your models here.
class TaskAction(models.Model):
    PRIORITY_CHOICE=[
        ('LOW','Low'),
        ('MEDIUM','Medium'),
        ('HIGH','High'),
        ('CRITICAL','Critical'),
    ]


    STATUS_CHOICE=[
        ('TO_DO','To_Do'),
        ('INPROGRESS','In_Progress'),
        ('INREVIEW','In_Review'),
        ('DONE','Done'),
        ('BLOCK','Block'),
    ]



    title=models.CharField(max_length=255)
    description=models.TextField(max_length=1000,null=True,blank=True)
    project=models.ForeignKey(ProjectModel,on_delete=models.CASCADE,null=True,blank=True,related_name='project_name')
    status=models.CharField(max_length=244,choices=STATUS_CHOICE,default='To_Do')
    priority=models.CharField(max_length=255,choices=PRIORITY_CHOICE,default='Low')
    due_date=models.DateTimeField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(UserModel,on_delete=models.CASCADE,null=True,blank=True)
    assigned_to=models.CharField(max_length=233)




    def __str__(self):
        return self.title
    

