from rest_framework import viewsets
from ..models import NotificationModel
from ..serializer.serializer import*
from ..utilities.pagination import myPageNumberPagination

#make the viewset:
class NotificationViewset(viewsets.ModelViewSet):
    serializer_class=NotificationListSerializer
    queryset=NotificationModel.objects.all().order_by('-id')
    pagination_class=myPageNumberPagination





    def get_queryset(self):
        queryset=super.get_queryset()
        return queryset
    

    #function to make serializer functional 
    def get_serializer_class(self):
        if self.action=='List':
            return NotificationListSerializer
        elif self.action==['create','update','partial_update']:
            return NotificationWriteSerializer
        elif self.action=='retrieve':
            return NotificationRetrieveSerializer
        return super().get_serializer_class()