from rest_framework.routers import DefaultRouter
from ..viewset.viewset import projectviewset


#create a router
router=DefaultRouter()
router.register('projects',projectviewset,basename='project')