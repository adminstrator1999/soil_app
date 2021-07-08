from rest_framework import serializers
from django.utils.translation import gettext as _

from main.models import News
from main.serializers.files import FileSerializer


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        exclude = []

    def update(self, instance, validated_data):
        views_count = validated_data.get('view_count', None)
        if views_count:
            raise serializers.ValidationError(detail=_('Views count can not be upgraded'))
        return super(NewsSerializer, self).update(instance, validated_data)

    def to_representation(self, instance):
        self.fields['image'] = FileSerializer(instance=instance.image)
        return super(NewsSerializer, self).to_representation(instance)
