from rest_framework import viewsets
from ..models import TaskAction
from ..serializer.serializer import*
from ..utilities.pagination import TaskModePagination

#class for the viewsets
class TaskModeViewset(viewsets.ModelViewSet):
    serializer_class=TaskModeListSerializer
    queryset=TaskAction.object.all()
    pagination_class=TaskModePagination





    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset
    

    def get_serializer_class(self):
        if self.action==['create','update','partial_update']:
            return TaskModeWriteSerializer
        elif self.action=='retrieve':
            return TaskModelRetrieveSerializer
        return super().get_serializer_class()
