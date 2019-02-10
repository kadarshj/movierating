from .models import MoviesList,Subscribe
from rest_framework import serializers

class MoviesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = MoviesList
        fields = ('id','title', 'url', 'imdbrating', 'year', 'gen_action', 'gen_comedy','is_subscribed')

class SubscribeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Subscribe
        fields = ('movielist','is_subscribed')

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
        fields = ('user_id','sublike','is_subscribed', 'movielist', 'subscribejoin')