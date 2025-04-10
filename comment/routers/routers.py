from rest_framework.routers import DefaultRouter
from ..viewset.viewset import CommentViewset

#set the default router
router=DefaultRouter()
router.register('Comments',CommentViewset,basename='comment')