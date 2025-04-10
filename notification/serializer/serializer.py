from rest_framework import serializers
from ..models import NotificationModel

#make  the class of the serailizer for the notification
#serializer to show all the list 
class NotificationListSerializer(serializers.ModelSerializer):
    class Meta:
        model=NotificationModel
        fields=['user','slug','message','notification_type','related_task','is_read','created_at']



#retreive the data using serializer
class NotificationRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model=NotificationModel
        fields=['user','message','is_read','created_at']


#write the data  using serializer
class NotificationWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=NotificationModel
        fields=['user','message','notification_type','related_task']
        
        