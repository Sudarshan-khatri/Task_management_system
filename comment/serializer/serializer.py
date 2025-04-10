from rest_framework import serializers
from ..models import CommentModel


#serializer to show all the list 
class CmtListSerializer(serializers.ModelSerializer):
    class Meta:
        model=CommentModel
        fields=['task','author','cmt','created_at','updated_at']



#retreive the data using serializer
class CmtRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model=CommentModel
        fields=['task','author','cmt']


#write the data  using serializer
class CmtWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=CommentModel
        fields=['task','author','cmt']
        
        