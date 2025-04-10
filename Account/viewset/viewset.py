from rest_framework import viewsets
from ..models import UserModel
from ..serializer.serializer import*
from ..utilities.pagination import userPagination


class AccountViewset(viewsets.ModelViewSet):
    serializer_class=UserListSerializer
    queryset=UserModel.objects.all()
    pagination_class=userPagination




    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset


    def get_serializer_class(self):
        if self.action=='List':
            return UserListSerializer
        elif self.action==['create','update','partial_update']:
            return UserRetrieveSerializer
        elif self.action=='retrieve':
            return UserWriteSerializer
        return super().get_serializer_class()