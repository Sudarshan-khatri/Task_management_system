from rest_framework import serializers
from ..models import TaskAction


#class to serialize the data
#serializer to show all the list 
class TaskModeListSerializer(serializers.ModelSerializer):
    class Meta:
        model=TaskAction
        fields=['title','description','project','status','priority','due_date','reated_date','updated_at','created_by','assigned_to']



#retreive the data using serializer
class TaskModelRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model=TaskAction
        fields=['title','description','project','status','priority','created_by','assigned_to']


#write the data  using serializer
class TaskModeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=TaskAction
        fields=['title','description','project','status','priority','created_by']
        
        