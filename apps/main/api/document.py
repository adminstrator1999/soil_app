from rest_framework.viewsets import ModelViewSet

from main.models import Document
from main.serializers.document import DocumentSerializer


class DocumentViewSet(ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()

    def get_serializer_class(self):
        context = super(DocumentViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context
