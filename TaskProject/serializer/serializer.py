from rest_framework import serializers
from ..models import ProjectModel

#serializer to show all the list 
class TaskProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjectModel
        fields=['name','description','status','start_date','end_date','created_at','updated_at','created_by','members']



#retreive the data using serializer
class TaskModelRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjectModel
        fields=['name','description','status','start_date','end_date','created_by','members']


#write the data  using serializer
class TaskModeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProjectModel
        fields=['name','description','status','created_by','members']
        
        