from rest_framework import viewsets
from ..models import ProjectModel
from ..serializer.serializer import*



#class of the viewsets
class projectviewset(viewsets.ModelViewSet):
    serializer_class=TaskProjectListSerializer
    queryset=ProjectModel.objects.all()




    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset
    
    def get_serializer_class(self):
        if self.action==['create','update','partial_update']:
            return TaskModeWriteSerializer
        if self.action=='retrieve':
            return TaskModelRetrieveSerializer
        return super().get_serializer()