from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import MoviesListSerializer, SubscribeSerializers,SubscribeRelatedSerializers,RatingSerializers
from .models import MoviesList,Subscribe
from rest_framework import status
from movie.models import User
from django.core import serializers


class MovieListView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        mlist = MoviesList.objects.all()[:1000]
        mserializer = MoviesListSerializer(mlist, many=True)
        return Response(mserializer.data)


class SubscribeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        aw = Subscribe.objects.all()
        serializer = SubscribeSerializers(aw, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubscribeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubscribeListView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user = request.user
        user_obj = User.objects.get(email=user)
        user_id = user_obj.id
        mymovielist = Subscribe.objects.select_related('movielist').filter(user_id=user_id, is_subscribed=True)
        mserializer = SubscribeRelatedSerializers(mymovielist, many=True)
        return Response(mserializer.data)

class RatingView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        aw = Subscribe.objects.all()
        serializer = SubscribeSerializers(aw, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RatingSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
