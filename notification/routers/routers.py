from rest_framework.routers import DefaultRouter
from ..viewset.viewset import NotificationViewset


#set the router for the notification app 
router=DefaultRouter()
router.register('notifications',NotificationViewset,basename='notification')