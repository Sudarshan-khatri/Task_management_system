from rest_framework.routers  import DefaultRouter
from ..viewset.viewset import TaskModeViewset


#set the routers
router=DefaultRouter()
router.register('taskmodes',TaskModeViewset,basename='taskmode')