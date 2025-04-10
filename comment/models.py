from django.db import models

# Create your models here.
class CommentModel(models.Model):
    task=models.ForeignKey('TaskMode.TaskAction',on_delete=models.CASCADE,null=True,blank=True)
    author=models.ForeignKey('Account.UserModel',on_delete=models.CASCADE,null=True,blank=True)
    cmt=models.TextField(max_length=20000)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.cmt
