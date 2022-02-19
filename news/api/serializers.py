from rest_framework import serializers
from datetime import datetime
from django.utils.timesince import timesince
from news.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    # Definition of extra fields for my serializer
    time_since_publication = serializers.SerializerMethodField()

    class Meta:
        model = Article
        exclude = ("id",)
        # fields = "__all__"
        # fields = ("title", "description", "body")

    def get_time_since_publication(self, object):
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta

    # Object level validation 
    def validation(self, data):
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Title and description must be different")
        return data

    # Field level Validation
    def validate_title(self, value):
        if len(value) < 20:
            raise serializers.ValidationError("Title has to be atleast 20 chars long..")
        return value 
