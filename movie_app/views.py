from django.shortcuts import render
from movie_app.models import *
from movie_app.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def directors_view(request):
    if request.method == 'GET':
        director = Director.objects.all()
        serializer = DirectorSerializer(director, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        name = request.data.get('name')
        director = Director.objects.create(name= name)
        return Response (data = {'director' : DirectorSerializer(director).data},
                         status= status.HTTP_201_CREATED)



@api_view(['GET','DELETE'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        serializer = DirectorDetailSerializer(director, many=False)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





@api_view(['GET', 'POST'])
def movie_view(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        title = request.data.get ('title')
        description = request.data.get ('description')
        duration = request.data.get ('duration')
        director = request.data.get ('director')
        movie = Movie.objects.create(title=title,description=description,director_id=director,duration=duration)
        return Response(data={'movie ':MovieSerializer(movie).data},
                        status = status.HTTP_201_CREATED)

@api_view(['GET','DELETE','PUT'])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieDetailSerializer(movie, many=False)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director')
        return Response({"message": "Data were changed!",
                         'movie': MovieSerializer(movie).data},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def review_view(request):
    if request.method == 'GET':
        movie = Review.objects.all()
        serializer = ReviewSerializer(movie, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
         text = request.data.get('text')
         movie = request.data.get('movie')
         stars = request.data.get('stars')
         review = Review.objects.create(text=text,movie_id=movie, stars=stars)
         return Response(data= {'review': ReviewSerializer(review).data},
                        status=status.HTTP_201_CREATED)




@api_view(['GET'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewDetailSerializer(review, many=False)
    return Response(data=serializer.data)

@api_view(['GET'])
def movie_review_view(request):
    movie = Movie.objects.all()
    serializer = MovieReviewSerializer(movie, many=True)

    return Response (data= serializer.data)