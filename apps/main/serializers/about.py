from rest_framework import serializers

from main.models import History, HistoryImages, File


class HistoryImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryImages
        exclude = []


class HistorySerializer(serializers.ModelSerializer):
    images = serializers.PrimaryKeyRelatedField(queryset=File.objects.all(), required=False, allow_null=True)
    
    class Meta:
        model = History
        exclude = []
        
    def create(self, validated_data):
        images = validated_data.pop('images', None)
        history_obj = History.objects.create(**validated_data)
        if images:
            data = [HistoryImages(image=image, history=history_obj) for image in images]
            HistoryImages.objects.bulk_create(data)
        return history_obj
    
    def update(self, instance, validated_data):
        instance.historyimages_set.all().delete()
        images = validated_data.pop('images', None)
        if images:
            data = [HistoryImages(image=image, history_id=instance.id) for image in images]
            HistoryImages.objects.bulk_create(data)
        return super(HistorySerializer, self).update(instance, validated_data)
            
        

