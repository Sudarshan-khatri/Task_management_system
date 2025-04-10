from rest_framework import serializers
from .models import UserModel 

#serializer to list the data
class UserListSerializers(serializers.ModelSerializer):
    class Meta:
        Model=UserModel
        fields=[]



