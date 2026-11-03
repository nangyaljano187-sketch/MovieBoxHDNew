from django.db import models

# Create your models here.


class PapularMovies(models.Model):
  movies_Action2=models.CharField(max_length=100,null=True,blank=True)
  movies_img2=models.ImageField(upload_to="papular_img",null=True,blank=True)
  movies_name2=models.CharField(max_length=200,null=True,blank=True)
  movies_Action2=models.CharField(max_length=100, null=True,blank=True)
  movies_year2=models.IntegerField(null=True,blank=True)
  
  
class Movie_catogri(models.Model):
  catogri_name=models.CharField(max_length=200,null=True,blank=True)
  def __str__(self):
    return self.catogri_name
  
class Movies(models.Model):
  Movies_img=models.ImageField(upload_to="movies", null=True,blank=True)
  Movies_file=models.FileField(upload_to="movies_play", null=True,blank=True)
  Movies_name=models.CharField(max_length=100, null=True,blank=True)
  Movies_year=models.IntegerField(null=True,blank=True)
  Movies_Action=models.CharField(max_length=100, null=True,blank=True)
  Movies_ActionF=models.ForeignKey(Movie_catogri,on_delete=models.CASCADE, null=True,blank=True)
  Movies_duration=models.CharField(max_length=100, null=True,blank=True)
  Movies_description=models.CharField(max_length=900, null=True,blank=True)
  
  # ================
  # videos models
  # ================
  
  
class PapularVideos(models.Model):
  Vides_image=models.ImageField(upload_to="papular videos",null=True,blank=True)
  Videos_name=models.CharField(max_length=200,null=True,blank=True)
  Videos_Action=models.CharField(max_length=200,null=True,blank=True)
  def __str__(self):
    return self.Videos_name
  
class Videos_categori(models.Model):
  video_catogri=models.CharField(max_length=250,null=True,blank=True)
  def __str__(self):
    return self.video_catogri
  
class Videos(models.Model):
  Videos_File=models.FileField(upload_to="videos files",null=True,blank=True)
  Videos_Action_F=models.ForeignKey(Videos_categori,on_delete=models.CASCADE ,null=True,blank=True)
  Videos_Title=models.CharField(max_length=180,null=True,blank=True)
  Videos_decs=models.CharField(max_length=400,null=True,blank=True)
  Videos_Action_m2=models.CharField(max_length=100,null=True,blank=True)
  def __str__(self):
    return self.Videos_Title
  
  
class Papular_picturs(models.Model):
  Papular_image=models.ImageField(upload_to="Papular_images",null=True,blank=True)
  Papular_image_Title=models.CharField(max_length=300,null=True,blank=True)
  def __str__(self):
    return self.Papular_image_Title
  
  
class Pics_catogri(models.Model):
  pics_catogri_name=models.CharField(max_length=300,null=True,blank=True)
  def __str__(self):
    return self.pics_catogri_name
  
class Pictures_model(models.Model):
  Pics_Action=models.ForeignKey(Pics_catogri,on_delete=models.CASCADE ,null=True,blank=True)
  Pics_Image=models.ImageField(upload_to="Pictures_page_images",null=True,blank=True)
  Pics_Title=models.CharField(max_length=400,null=True,blank=True)
  Pics_Action2=models.CharField(max_length=100,null=True,blank=True)
  def __str__(self):
    return self.Pics_Title
  

class FN_catogri(models.Model):
  FN_catogri_name=models.CharField(max_length=200,null=True,blank=True)
  def __str__(self):
    return self.FN_catogri_name
  
class FN_model(models.Model):
  Fn_file=models.FileField(upload_to="FN_play", null=True,blank=True)
  Fn_name=models.CharField(max_length=100, null=True,blank=True)
  Fn_year=models.IntegerField(null=True,blank=True)
  Fn_Action=models.CharField(max_length=100, null=True,blank=True)
  Fn_ActionF=models.ForeignKey(FN_catogri,on_delete=models.CASCADE, null=True,blank=True)
  Fn_duration=models.CharField(max_length=100, null=True,blank=True)
  Fn_description=models.CharField(max_length=900, null=True,blank=True)
  
# Tranding Movies

class Tranding_movies(models.Model):
  Trand_M_img=models.FileField(upload_to="Trandingmoviepics",null=True,blank=True)
  Trand_M_name=models.CharField(max_length=200,null=True,blank=True)
  Trand_M_Action=models.CharField(max_length=130,null=True,blank=True)
  Trand_M_desc=models.CharField(max_length=400,null=True,blank=True)
  Trand_M_year=models.CharField(max_length=500,null=True,blank=True)
  Trand_M_link=models.CharField(max_length=20000,null=True,blank=True)
  def __str__(self):
    return self.Trand_M_name
  
  