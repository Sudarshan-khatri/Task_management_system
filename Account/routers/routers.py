from rest_framework.routers import DefaultRouter
from ..viewset.viewset  import AccountViewset

#set and register the router
router=DefaultRouter()
router.register('accounts',AccountViewset,base_name='account')
