from rest_framework.viewsets import ModelViewSet

from main.models import History
from main.serializers.about import HistorySerializer


class HistoryViewSet(ModelViewSet):
    serializer_class = HistorySerializer
    queryset = History.objects.all()
