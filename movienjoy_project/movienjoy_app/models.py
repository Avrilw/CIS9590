from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=268)
    release_date = models.DateField()
    box_office = models.IntegerField()
    duration = models.IntegerField()
    language = models.CharField(max_length=100)
    overview = models.TextField()
    genre = models.TextField()
    casts = models.TextField()
    rate = models.FloatField()
    director = models.CharField(max_length=100)

    def __str__(self):
        return self.movie_name


class User(models.Model):
    user_id = models.EmailField(max_length=254,unique=True,primary_key=True)
    user_name = models.CharField(max_length=254,unique=True)
    password = models.CharField(max_length=25,unique=False)
    birthday = models.DateField(auto_now=False,auto_now_add=False,unique=False)
    gender = models.CharField(max_length=16,unique=False)
    occuptation = models.CharField(max_length=254,unique=False)
    register_date = models.DateField(auto_now_add=True,unique=False)

    def __str__(self):
        return self.user_name


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=268)
    re_content = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Comment(models.Model):
    comment_id = models.AutoField(unique=True,primary_key=True)
    com_content = models.CharField(max_length=512,unique=False)
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    com_date = models.DateTimeField(auto_now_add=True,unique=False)


class Watchlist(models.Model):
    class Meta:
        unique_together = (('user_id', 'movie_id'),)

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return str((self.user_id, self.movie_id)[0])



