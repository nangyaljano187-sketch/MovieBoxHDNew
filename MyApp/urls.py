from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("Movies/",views.Moviess,name="Movies"),
    path("videos/",views.videos,name="videos"),
    path("pictures/",views.pictures,name="pictures"),
    path("TrandingMovies/",views.Tranding_Movies,name="Tranding_Movies"),
    path("download/<int:id>/",views.download_Movie,name="download_Movie"),
    path("categories/<str:pk>",views.catogri_page,name="catogri_page"),
    path('searchs/',views.All_search,name="search"),
    path("Codepage/",views.Code_page,name="Code_page"),
    path("vsearch/",views.VIdEO_SEARCH,name="VIdEO_SEARCH"),
    path("vcatogri/<str:pk>",views.VIDEOS_S,name="VIDEOS_S"),
    path("PicsSearch/",views.PicsSearch_p,name="PicsSearch_p"),
    path("Picscatogri/<str:pk>",views.Pics_catogri_page,name="Pics_catogri_page"),
    path("downloadPictures/<int:id>/",views.download_pics,name="download_pics"),
    path("FNpagesdjhdsueuwyeruWWWymnmnmndsFNpagesdjhdsueuwyeruymnmnmndsdjhdjh",views.FN_page,name="FN_page"),
    path("Fncatogripage/<str:pk>",views.Fn_catogri_page,name="Fn_catogri_page"),
    path("fnsearch/",views.FNsearch_page,name="FNsearch_page"),
    path('uploadedpageccxnbjhdhjhcytdghdbncxmzdmbbhgdhgshgdshxcbnxchdgdhgcxhhfdgdgdfg/',views.uploaded_page,name='uploaded_page'),
    path("deletepapularImage/<int:pk>/",views.delete_papularImage,name='delete_papularImage'),
    path("DatabaseSaveMoviesCatogri/",views.Database_save_movies_catogri,name="Database_save_movies_catogri"),
    path("deleteMCategori/<int:pk>",views.delete_M_categori,name='delete_M_categori'),
    path("dbSaveDMovies/",views.db_save_DMovies,name="db_save_DMovies"),
    path("PapularVideosUploaded/",views.Papular_Videos_uploaded,name='Papular_Videos_uploaded'),
    path("PapularVideosDelete/<int:pk>",views.Papular_videos_delete,name='Papular_videos_delete'),
    path("PapularVideosCategori/",views.Papular_Videos_categori,name="Papular_Videos_categori"),
    path("VIDEOScATEGORI/<int:pk>",views.VIDEOS_CATEGORI,name='VIDEOS_CATEGORI'),
    path("VIDEOSpANELuPLOADED/",views.VIDEOS_PANEL_UPLOADED,name="VIDEOS_PANEL_UPLOADED"),
    path("PapularPictureUploaded/",views.Papular_picture_uploaded,name="Papular_picture_uploaded"),
    path("DeletePicUploadedData/<int:pk>",views.Delete_Pic_uploaded_data,name='Delete_Pic_uploaded_data'),
    path("PapularPicsCategoriUploaded/",views.Papular_pics_categori_uploaded,name="Papular_pics_categori_uploaded"),
    path("DeleteAllPicsCategories/<int:pk>",views.Delete_allPics_categories,name='Delete_allPics_categories'),
    path("ALLPICSUploaded/",views.ALL_PICS_uploaded,name="ALL_PICS_uploaded"),
    path("FNcatogries/",views.FN_catogries,name="FN_catogries"),
    path('deleteFNVIDEOS/<int:pk>',views.delete_FN_VIDEOS,name="delete_FN_VIDEOS"),
    path("FNALLUploaded/",views.FN_ALL_uploaded,name="FN_ALL_uploaded"),
    path("fnVideosDelete/<int:pk>",views.fn_videos_delete,name="fn_videos_delete"),
    path("TarndSearch/",views.Tarnd_search,name="Tarnd_search"),
    path("TrandUploaded/",views.TrandUploaded,name="TrandUploaded"),
    path("TrandUploadedDalete/<int:pk>",views.TrandUploaded_dalete,name="TrandUploaded_dalete"),
    path("ADMINPanelCode/",views.ADMIN_panel_code,name="ADMIN_panel_code")
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    