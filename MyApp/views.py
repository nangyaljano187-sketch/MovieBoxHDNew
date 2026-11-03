from django.shortcuts import render,redirect
from django.http import HttpResponse,FileResponse
from MyApp.models import Movies,PapularMovies,Movie_catogri,PapularVideos
from MyApp.models import Videos_categori,Videos,Papular_picturs
from MyApp.models import Pics_catogri,Pictures_model,FN_catogri,FN_model
from MyApp.models import Tranding_movies
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
import os
from django.db.models import Q
# Create your views here.

def home(request):
  M_data1=PapularMovies.objects.all()
  V_data2=PapularVideos.objects.all()
  Image_data3=Papular_picturs.objects.all()
  context_data1={
    'M_data1':M_data1,
    'V_data2':V_data2,
    'Image_data3':Image_data3,
  }
  return render(request,"index.html",context_data1)


def All_search(request):
  get_all_catogri=Movie_catogri.objects.all()
  Query_search=request.GET.get('search')
  m_data2=Movies.objects.all()
  if Query_search:
    m_data2=Movies.objects.filter(
      Q(Movies_name__icontains=Query_search)|
      Q(Movies_description__icontains=Query_search)|
      Q(Movies_Action__icontains=Query_search)|
      Q(Movies_year__icontains=Query_search)
      )
    
  searchAllCount=m_data2.count()
  
  context_search={
    'Query_search':Query_search,
    'm_data2':m_data2,
    'get_all_catogri':get_all_catogri,
    'searchAllCount':searchAllCount
  }
  return render(request,"search.html",context_search)

def PicsSearch_p(request):
  get_all_pics_catogri=Pics_catogri.objects.all()
  getAll_pics=Pictures_model.objects.all()
  get_searchInp=request.GET.get("PicSearch")
  if get_searchInp:
    getAll_pics=Pictures_model.objects.filter(
      Q(Pics_Title__icontains=get_searchInp)|
      Q(Pics_Action2__icontains=get_searchInp)
      )
    
  allSETcOUNt=getAll_pics.count()
  context_pics={
    'get_all_pics_catogri':get_all_pics_catogri,
    'getAll_pics':getAll_pics,
    'get_searchInp':get_searchInp,
    'allSETcOUNt':allSETcOUNt
  }
  return render(request,"PicsSearch.html",context_pics)

def catogri_page(request,pk):
  get_catogri_id=Movie_catogri.objects.get(id=pk)
  get_all_catogri=Movie_catogri.objects.all()
  all_set=Movies.objects.filter(Movies_ActionF=get_catogri_id)
  all_Movies=Movies.objects.all()
  Catoricount=all_set.count()
  contex_catogri={
    'M_data':all_set,
    'all_set':all_set,
    'get_all_catogri':get_all_catogri,
    'Catoricount':Catoricount
  }
  return render(request,'catogri.html',contex_catogri)


def Moviess(request):
  M_data=Movies.objects.all()
  movies_filter=Movies.objects.filter(id=2)
  get_all_catogri=Movie_catogri.objects.all()
  Moviescount=M_data.count()
  
  paginator=Paginator(M_data,20)
  page_number=request.GET.get("page")
  M_data=paginator.get_page(page_number)
  context_data={
    'M_data':M_data,
    'get_all_catogri':get_all_catogri,
    'Moviescount':Moviescount
  }
  return render(request,"movies.html",context_data)

def download_Movie(request,id):
  movie=get_object_or_404(Movies,id=id)
  file_path=movie.Movies_file.path
  file_name=movie.Movies_name + ".mp4" if movie.Movies_name else os.path.basename(file_path)
  return FileResponse(open(file_path,"rb"),as_attachment=True,filename=file_name)

def download_pics(request,id):
  PICS=get_object_or_404(Pictures_model,id=id)
  file_path=PICS.Pics_Image.path
  file_name=PICS.Pics_Title + ".jpg" if PICS.Pics_Title else os.path.basename(file_path)
  return FileResponse(open(file_path,"rb"),as_attachment=True,filename=file_name)

def videos(request):
  getAll_videos_categori=Videos_categori.objects.all()
  ALL_VIDEOS=Videos.objects.all()
  context_videos={
    'getAll_videos_categori':getAll_videos_categori,
    'ALL_VIDEOS':ALL_VIDEOS
  }
  return render(request,"videos.html",context_videos)

def pictures(request):
  get_all_pics_catogri=Pics_catogri.objects.all()
  get_allPics=Pictures_model.objects.all()
  PicsCount=get_allPics.count()
  context_pics={
    'get_all_pics_catogri':get_all_pics_catogri,
    'get_allPics':get_allPics,
    "PicsCount":PicsCount
  }
  return render(request,"pictures.html",context_pics)

def Tranding_Movies(request):
  get_all_Tranding_Movie=Tranding_movies.objects.all()
  Moviescount=get_all_Tranding_Movie.count()
  
  paginator=Paginator(get_all_Tranding_Movie,50)
  page_number=request.GET.get("page")
  get_all_Tranding_Movie=paginator.get_page(page_number)
  context_Tarnding_ovies={
    'Moviescount':Moviescount,
    'get_all_Tranding_Movie':get_all_Tranding_Movie
  }
  return render(request,"Tranding_Movies.html",context_Tarnding_ovies)

def Tarnd_search(request):
  Tranding_Movies_all=Tranding_movies.objects.all()
  Trand_query_get=request.GET.get("search")
  Moviescount=Tranding_Movies_all.count()
  if Trand_query_get:
    Tranding_Movies_all=Tranding_movies.objects.filter(
      Q(Trand_M_name__icontains=Trand_query_get)|
      Q(Trand_M_desc__icontains=Trand_query_get)|
      Q(Trand_M_Action__icontains=Trand_query_get)|
      Q(Trand_M_year__icontains=Trand_query_get)
      )
  context_data_trand={
    'Moviescount':Moviescount,
    'Tranding_Movies_all':Tranding_Movies_all
  }
  return render(request,"TrandingMovieSearch.html",context_data_trand)


def TrandUploaded(request):
  if request.method=='POST':
    VAL0040=request.FILES.get("Trand_M_img")
    VAL0041=request.POST.get("Trand_M_name")
    VAL0042=request.POST.get("Trand_M_Action")
    VAL0043=request.POST.get("Trand_M_desc")
    VAL0044=request.POST.get("Trand_M_year")
    VAL0045=request.POST.get("Trand_M_link")
    
    DB_dataBASE_TRAND=Tranding_movies(Trand_M_img=VAL0040,Trand_M_name=VAL0041,Trand_M_Action=VAL0042,Trand_M_desc=VAL0043,Trand_M_year=VAL0044,Trand_M_link=VAL0045)
    DB_dataBASE_TRAND.save()
  get_all_data=Tranding_movies.objects.all()
  context_data7={
    'get_all_data':get_all_data
  }
  return render(request,"TrandUploaded.html",context_data7)

def TrandUploaded_dalete(request,pk):
  get_trand_id=Tranding_movies.objects.get(id=pk)
  get_trand_id.delete()
  return redirect("TrandUploaded")

def Code_page(request):
  if request.method == "POST":
    webinp=request.POST.get("Website")
    codeinp=request.POST.get("code")
    if webinp == "Moviesboxos" and codeinp == "cine@1236":
      return redirect("FN_page")
    else:
      return redirect("Code_page")
      
  return render(request,"codeForm.html")

def ADMIN_panel_code(request):
  if request.method=='POST':
    webinp_panel=request.POST.get("Website")
    PASSWORD_panel=request.POST.get("code")
    
    if webinp_panel == "Moviesboxos" and PASSWORD_panel =="secret@123$321@secret":
      return redirect("uploaded_page")
    else:
      return redirect("ADMIN_panel_code")
  return render(request,"AdminPanelCode.html")

def VIdEO_SEARCH(request):
  allV_coatogri_get=Videos_categori.objects.all()
  v_query_s=request.GET.get("v_search")
  v_data=Videos.objects.all()
  if v_query_s:
    v_data=Videos.objects.filter(
      Q(Videos_Title__icontains=v_query_s)|
      Q(Videos_decs__icontains=v_query_s)|
      Q(Videos_Action_m2__icontains=v_query_s)
      )
    context_Vsearch={
      'v_data':v_data,
      'v_query_s':v_query_s,
      'allV_coatogri_get':allV_coatogri_get
    }
  return render(request,"videosearch.html",context_Vsearch)

def VIDEOS_S(request,pk):
  get_catogri_idV=Videos_categori.objects.get(id=pk)
  allV_coatogri_get=Videos_categori.objects.all()
  all_setV=Videos.objects.filter(Videos_Action_F=get_catogri_idV)
  contex_V_S={
    'get_catogri_idV':get_catogri_idV,
    'allV_coatogri_get':allV_coatogri_get,
    'all_setV':all_setV
  }
  return render(request,"vcatogri.html",contex_V_S)

def Pics_catogri_page(request,pk):
  get_catogri_idP=Pics_catogri.objects.get(id=pk)
  get_all_piccatogri=Pics_catogri.objects.all()
  all_setP=Pictures_model.objects.filter(Pics_Action=get_catogri_idP)
  allSETcOUNt=all_setP.count()
  context_PIC_catogri={
    'get_catogri_idP':get_catogri_idP,
    'get_all_piccatogri':get_all_piccatogri,
    'all_setP':all_setP,
    "allSETcOUNt":allSETcOUNt
  }
  return render(request,"PicCatogri.html",context_PIC_catogri)

def FN_page(request):
  get_FN_catogri=FN_catogri.objects.all()
  get_all_fn=FN_model.objects.all()
  allSETcOUNt=get_all_fn.count()
  context_datafn={
    'get_all_fn':get_all_fn,
    'get_FN_catogri':get_FN_catogri,
    'allSETcOUNt':allSETcOUNt
  }
  return render(request,"FN.html",context_datafn)

def Fn_catogri_page(request,pk):
  get_catogri_idFn=FN_catogri.objects.get(id=pk)
  get_all_Fncatogri=FN_catogri.objects.all()
  all_setFN=FN_model.objects.filter(Fn_ActionF=get_catogri_idFn)
  allSETcOUNt=all_setFN.count()
  context_Fn_catogri={
    'get_catogri_idFn':get_catogri_idFn,
    'get_all_Fncatogri':get_all_Fncatogri,
    'all_setFN':all_setFN,
    "allSETcOUNt":allSETcOUNt
  }
  return render(request,"FNCatogri.html",context_Fn_catogri)

def FNsearch_page(request):
  get_all_Fncatogri=FN_catogri.objects.all()
  get_allFN_model=FN_model.objects.all()
  get_inpFn=request.GET.get("search")
  if get_inpFn:
    get_allFN_model=FN_model.objects.filter(
      Q(Fn_name__icontains=get_inpFn)|
      Q(Fn_description__icontains=get_inpFn)|
      Q(Fn_Action__icontains=get_inpFn)|
      Q(Fn_year__icontains=get_inpFn)
      )
    
  allSETcOUNt=get_allFN_model.count()
  context_FN={
    'get_all_Fncatogri':get_all_Fncatogri,
    'get_allFN_model':get_allFN_model,
    'allSETcOUNt':allSETcOUNt,
    'get_inpFn':get_inpFn
  }
  return render(request,'search_FN.html',context_FN)


def uploaded_page(request):
  if request.method== "POST":
    val1=request.POST.get("action2")
    val2=request.FILES.get("Movies_image")
    val3=request.POST.get("name2")
    val4=request.POST.get("year2")
    
    save_database_data=PapularMovies(movies_Action2=val1,movies_img2=val2,movies_name2=val3,movies_year2=val4)
    save_database_data.save()
    
  Movies_show_panel=PapularMovies.objects.all()
  context_panel={
    'Movies_show_panel':Movies_show_panel
  } 
  return render(request,"uploading_page.html",context_panel)


def delete_papularImage(request,pk):
  get_id_p_Movies=PapularMovies.objects.get(id=pk)
  get_id_p_Movies.delete()
  return redirect("uploaded_page")


def Database_save_movies_catogri(request):
  if request.method=="POST":
    val1_1=request.POST.get("M_catogri")
    
    db_save_M_categori=Movie_catogri(catogri_name=val1_1)
    db_save_M_categori.save()
    
  get_Movies_categori=Movie_catogri.objects.all()
  context_data_M_c={
    'get_Movies_categori':get_Movies_categori
  }
  return render(request,"DMovieCatogri.html",context_data_M_c)

def delete_M_categori(request,pk):
  get_id_C_Movies=Movie_catogri.objects.get(id=pk)
  get_id_C_Movies.delete()
  return redirect("Database_save_movies_catogri")


def db_save_DMovies(request):
  if request.method== "POST":
    VAL1_M=request.FILES.get("M_files")
    VAL2_M=request.POST.get("M_name")
    VAL3_M=request.POST.get("M_year")
    VAL4_M=request.POST.get("M_Action")
    VAL5_M=request.POST.get("M_Action_F")
    VAL6_M=request.POST.get("M_duration")
    VAL7_M=request.POST.get("M_description")
    
    db_Movies_save=Movies(Movies_file=VAL1_M,Movies_name=VAL2_M,Movies_year=VAL3_M,Movies_Action=VAL4_M,Movies_duration=VAL6_M,Movies_description=VAL7_M)
    db_Movies_save.save()
  get_Movies_categori=Movie_catogri.objects.all()
  context_data45={
    'get_Movies_categori':get_Movies_categori
  }
  return render(request,"DMovies.html",context_data45)

# Papular_videos
def Papular_Videos_uploaded(request):
  if request.method=="POST":
    val1_Papular_Videos=request.FILES.get("Vides_image")
    val2_Papular_Videos=request.POST.get("Videos_name")
    val3_Papular_Videos=request.POST.get("Videos_Action")
    
    DB_SAVE_papular_videos=PapularVideos(Vides_image=val1_Papular_Videos,Videos_name=val2_Papular_Videos,Videos_Action=val3_Papular_Videos)
    DB_SAVE_papular_videos.save()
    
  show_template_data=PapularVideos.objects.all()
  context_data_P_Videos={
    'show_template_data':show_template_data
  }
    
  return render(request,"DPapularVIdeos.html",context_data_P_Videos)

def Papular_videos_delete(request,pk):
  get_dalate_id=PapularVideos.objects.get(id=pk)
  get_dalate_id.delete()
  return redirect("Papular_Videos_uploaded")

def Papular_Videos_categori(request):
  if request.method=="POST":
    VAL1_v_CATEGORI=request.POST.get('video_catogri')
    
    DB_VIDEOS_CATEGORI=Videos_categori(video_catogri=VAL1_v_CATEGORI)
    DB_VIDEOS_CATEGORI.save()
  get_all_Videos_categori=Videos_categori.objects.all()
  context_data_V_categori={
    'get_all_Videos_categori':get_all_Videos_categori
  }
  return render(request,"VideosCUploaded.html",context_data_V_categori)

def VIDEOS_CATEGORI(request,pk):
  get_Videos_categori_id=Videos_categori.objects.get(id=pk)
  get_Videos_categori_id.delete()
  return redirect("Papular_Videos_categori")

def VIDEOS_PANEL_UPLOADED(request):
  if request.method=='POST':
    if request.method=='POST':
      VAL01=request.FILES.get("Videos_File")
      VAL02=request.POST.get("Videos_Action_F")
      VAL03=request.POST.get("Videos_Title")
      VAL04=request.POST.get("Videos_decs")
      VAL05=request.POST.get("Videos_Action_m2")
      
      DB_dataSave_uploaded=Videos(Videos_File=VAL01,Videos_Title=VAL03,Videos_decs=VAL04,Videos_Action_m2=VAL05)
      DB_dataSave_uploaded.save()
     
  return render(request,"VideosUploaded.html")

# PAPULAR VIDEOS

def Papular_picture_uploaded(request):
  if request.method=='POST':
    VAL001=request.FILES.get('Papular_image')
    VAL002=request.POST.get('Papular_image_Title')
    
    DB_DATASAVE_UPLOADED_PICTURE=Papular_picturs(Papular_image=VAL001,Papular_image_Title=VAL002)
    DB_DATASAVE_UPLOADED_PICTURE.save()
  
  getALL_pictures=Papular_picturs.objects.all()
  context_data001={
    'getALL_pictures':getALL_pictures
  }
  return render(request,"PapualerPICSuPloaded.html",context_data001)

def Delete_Pic_uploaded_data(request,pk):
  get_allpic_id=Papular_picturs.objects.get(id=pk)
  get_allpic_id.delete()
  return redirect("Papular_picture_uploaded")

def Papular_pics_categori_uploaded(request):
  if request.method == 'POST':
    VAL0001=request.POST.get('pics_catogri_name')
    
    DB_PICScATEGORI_UPLOADED=Pics_catogri(pics_catogri_name=VAL0001)
    DB_PICScATEGORI_UPLOADED.save()
  
  SHOW_ALL_uploaded_categori=Pics_catogri.objects.all()
  context_PICS={
    'SHOW_ALL_uploaded_categori':SHOW_ALL_uploaded_categori
  }
  return render(request,'PapularPICcategori.html',context_PICS)


def Delete_allPics_categories(request,pk):
  get_all_picCategori_id=Pics_catogri.objects.get(id=pk)
  get_all_picCategori_id.delete()
  return redirect("Papular_pics_categori_uploaded")

def ALL_PICS_uploaded(request):
  if request.method=='POST':
    VAL0011=request.POST.get("Pics_Action")
    VAL0012=request.FILES.get("Pics_Image")
    VAL0013=request.POST.get("Pics_Title")
    VAL0014=request.POST.get("Pics_Action2")
    
    DB_UPLADED_pics_save=Pictures_model(Pics_Image=VAL0012,Pics_Title=VAL0013,Pics_Action2=VAL0014)
    DB_UPLADED_pics_save.save()
  return render(request,"PictureALLUploaded.html")

# FN CATEGORI 

def FN_catogries(request):
  if request.method == 'POST':
    VAL0020=request.POST.get("FN_catogri_name")
    
    DB_FN_categori_save=FN_catogri(FN_catogri_name=VAL0020)
    DB_FN_categori_save.save()
  
  show_all_FNcategories=FN_catogri.objects.all()
  context_FN_show={
    'show_all_FNcategories':show_all_FNcategories
  }
  return render(request,'FNuPLOADEDpaNAL.html',context_FN_show)


def delete_FN_VIDEOS(request,pk):
  get_id_in_FN_CATEGORI=FN_catogri.objects.get(id=pk)
  get_id_in_FN_CATEGORI.delete()
  return redirect("FN_catogries")

def FN_ALL_uploaded(request):
  if request.method == 'POST':
    val0030=request.FILES.get('Fn_file')
    val0031=request.POST.get('Fn_name')
    val0032=request.POST.get('Fn_year')
    val0033=request.POST.get('Fn_Action')
    val0034=request.POST.get('Fn_ActionF')
    val0035=request.POST.get('Fn_duration')
    val0036=request.POST.get('Fn_description')
    
    DB_FN_ALL_MODEL_uploaded=FN_model(Fn_file=val0030,Fn_name=val0031,Fn_year=val0032,Fn_Action=val0033,Fn_duration=val0035,Fn_description=val0036)
    DB_FN_ALL_MODEL_uploaded.save()
    
  showall_fn_data=FN_model.objects.all()
  context_fn_all={
    'showall_fn_data':showall_fn_data
  }
  return render(request,"FNMODELUPLOADED.html",context_fn_all)

def fn_videos_delete(request,pk):
  get_id_in_fn_model=FN_model.objects.get(id=pk)
  get_id_in_fn_model.delete()
  return redirect("FN_ALL_uploaded")