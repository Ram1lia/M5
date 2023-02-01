from django.shortcuts import render
from movie_app.models import *
from movie_app.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def directors_view(request):
    director = Director.objects.all()
    serializer = DirectorSerializer(director, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': 'Director not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = DirectorDetailSerializer(director, many=False)
    return Response(data=serializer.data)

@api_view(['GET'])
def movie_view(request):
    movie = Movie.objects.all()
    serializer = MovieSerializer(movie, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(data={'error': 'Movie not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = MovieDetailSerializer(movie, many=False)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_view(request):
    movie = Review.objects.all()
    serializer = ReviewSerializer(movie, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewDetailSerializer(review, many=False)
    return Response(data=serializer.data)