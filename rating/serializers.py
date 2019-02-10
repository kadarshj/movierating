from .models import MoviesList,Subscribe
from rest_framework import serializers

class MoviesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = MoviesList
        fields = ('title', 'url', 'imdbrating', 'year', 'gen_action', 'gen_comedy')

class SubscribeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Subscribe
        fields = ('movielist','sublike')

class RatingSerializers(serializers.ModelSerializer):

    class Meta:
        model = Subscribe
        fields = ('movielist','rating')

class SubscribeAllSerializer(serializers.ModelSerializer):

    class Meta:
        model = MoviesList
        fields = ('title', 'url', 'imdbrating', 'year', 'gen_action', 'gen_comedy')

class SubscribeRelatedSerializers(serializers.ModelSerializer):
    subscribejoin = SubscribeAllSerializer(source="movielist")
    class Meta:
        model = Subscribe
        fields = ('user_id', 'movielist','sublike', 'subscribejoin')