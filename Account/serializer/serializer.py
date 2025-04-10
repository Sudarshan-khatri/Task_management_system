from rest_framework import serializers
from ..models import UserModel


#serializer to show all the list 
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserModel
        fields=['user_name','slug','role','profile_picture','Phone_number','Bio']



#retreive the data using serializer
class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserModel
        fields=['user_name','profile_picture','Bio']


#write the data  using serializer
class UserWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserModel
        fields=['user_name','slug','role','Phone_number','Bio']
        
        