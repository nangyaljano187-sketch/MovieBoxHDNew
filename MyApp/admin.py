from django.contrib import admin
from MyApp.models import Movies,PapularMovies,Movie_catogri,PapularVideos,Videos_categori,Videos
from MyApp.models import Papular_picturs,Pics_catogri,Pictures_model
from MyApp.models import FN_catogri,FN_model,Tranding_movies
# Register your models here.

admin.site.register(Movies)
admin.site.register(PapularMovies)
admin.site.register(Movie_catogri)
admin.site.register(PapularVideos)
admin.site.register(Videos_categori)
admin.site.register(Videos)
admin.site.register(Papular_picturs)
admin.site.register(Pics_catogri)
admin.site.register(Pictures_model)
admin.site.register(FN_catogri)
admin.site.register(FN_model)
admin.site.register(Tranding_movies)