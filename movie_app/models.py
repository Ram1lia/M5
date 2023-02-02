from django.db import models
# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=200)

class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    duration = models.FloatField(default=0)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)




    @property
    def rating(self):
        count = self.product_reviews.count()
        if count == 0:
            return 0
        total = 0
        for i in self.product_reviews.all():
            total += i.stars
        return total / count


CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


class Review(models.Model):
    text = models.TextField(max_length=200)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=CHOICES, null=True)







