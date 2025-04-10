from django.db import models
from django.utils.text import slugify

# Create your models here.
class UserModel(models.Model):
    Role_choice=[
        ('ADMIN', 'Administrator'),
        ('MOD', 'Moderator'),
        ('AUTHOR', 'Author'),
        ('EDITOR', 'Editor'),
        ('REVIEWER', 'Reviewer'),
        ('CONTRIBUTOR', 'Contributor'),
        ('MEMBER', 'Member'),
        ('GUEST', 'Guest'),
        ('MANAGER', 'Manager'),
        ('DEVELOPER', 'Developer'),
    ]
    user_name=models.CharField(max_length=30)
    slug=models.SlugField(unique=True,blank=True)
    role=models.CharField(max_length=300,choices=Role_choice,default='DEVELOPER')
    profile_picture=models.ImageField(upload_to='media',null=True,blank=True)
    Phone_number=models.CharField(max_length=12,null=True,blank=True)
    Bio=models.TextField(max_length=5000,null=True,blank=True)

    #define new slug field
    def save(self,*args,**kwargs):
        if not self.slug:
            slug=slugify(self.user)
            counter=1
            while UserModel.objects.filter(slug==slug).exists():
                slug=f"{slug}"-counter
                counter+=1
            self.slug=slug
        super.save(*args,**kwargs)        



    #convert the human redeable form 
    def __str__(self):
        return self.user_name