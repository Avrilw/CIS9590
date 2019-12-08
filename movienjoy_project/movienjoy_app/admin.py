from django.contrib import admin
from movienjoy_app.models import Movie, User, Review, Comment, Watchlist

# Register your models here.
admin.site.register(Movie)
admin.site.register(User)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Watchlist)

