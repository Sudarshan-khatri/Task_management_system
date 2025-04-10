from  rest_framework import viewsets
from ..models import CommentModel
from ..serializer.serializer import*


class CommentViewset(viewsets.ModelViewSet):
    queryset=CommentModel.objects.all()
    serializer_class=CmtListSerializer




    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset
    

    #get_serialize_class show how to send data
    def get_serializer_class(self):
        if self.action=='List':
            return CmtListSerializer
        elif self.action==['create','update','partial_update']:
            return CmtWriteSerializer
        elif self.action=='retrieve':
            return CmtRetrieveSerializer
        return super().get_serializer_class(self)