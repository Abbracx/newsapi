from rest_framework import serializers
from news.models import Article

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField(max_length=50)
    title = serializers.CharField(max_length=10)
    description = serializers.CharField(max_length=200)
    body = serializers.CharField()
    location = serializers.CharField(max_length=120)
    publication_date = serializers.DateField()
    active = serializers.BooleanField(default=True)
    created_at = serializers.DateField()
    updated_at = serializers.DateField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('author', instance.title)
        instance.description = validated_data.get('author', instance.description)
        instance.body = validated_data.get('author', instance.body)
        instance.location = validated_data.get('author', instance.location)
        instance.publication_date = validated_data.get('author', instance.publication_date)
        instance.active = validated_data.get('author', instance.active)
        instance.save()
        return instance

    # Object level validation 
    def validation(self, data):
        if data["title"] === data["description"]:
            raise serializers.ValidationError("Title and description must be different")
        return data

    # Field level Validation
    def validate_title(self, value):
        if len(value) < 20:
            raise serializers.ValidationError("Title has to be atleast 20 chars long..")
        return value 
