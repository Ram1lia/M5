from movie_app.models import *
from rest_framework import serializers
from movie_app.models import *


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name '.split()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title director rating '.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta :
        model = Review
        fields = '__all__'


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text movie'.split()


class MovieReviewSerializer(serializers.ModelSerializer):
    review = ReviewSerializer()
    rating = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        field = '__all__'
    def get_rating(self):
        r = [review.grade for review in review.all()]
        return sum(r)/ len(r) if r else None