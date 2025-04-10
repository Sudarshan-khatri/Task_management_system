from django.db import models
from Account.models import UserModel
from TaskMode.models import TaskAction
from django.utils.text import slugify


# Create your models here.
class NotificationModel(models.Model):
    noticetype=[
        ('ASSIGNMENT','Assignment'),
        ('DEADLINE','Deadline'),
        ('COMMENT','Comment'),
        ('STATUS_CHANGE','Status_change')
    ]
    user=models.ForeignKey(UserModel,on_delete=models.CASCADE)
    slug=models.SlugField(unique=True,blank=True)
    message=models.CharField(max_length=25555)
    notification_type=models.CharField(max_length=255,choices=noticetype,default='Comment')
    related_task=models.ForeignKey(TaskAction,on_delete=models.CASCADE,null=True)
    is_read=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)


    #define the new slug field
    def save(self,*args,**kwargs):
        if not self.slug:
            slug=slugify(self.user)
            counter=1
            while NotificationModel.objects.filter(slug==slug).exists():
                slug=f"{slug}"-counter
                counter+=1
            self.slug=slug
        super.save(*args,**kwargs)        

    def __str__(self):
        return  self.user