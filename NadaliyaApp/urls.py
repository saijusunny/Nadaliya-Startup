from django.urls import re_path,path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    #############################################################<<<<<<<<< LANDING MODULE >>>>>>>>>>>>>>>>>
    path('', views.index, name='index'),
    path('user_type', views.user_type, name='user_type'),
    path('login_main',views.login_main, name='login_main'),
    path('forgotPassword/', views.forgotPassword,name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate,name='resetpassword_validate'),
    path('resetPassword/', views.resetPassword,name='resetPassword'),
    path('logout/', views.logout,name='logout'),

    ############################################################ <<<<<<<<< Staff MODULE >>>>>>>>>>>>>>>>>
    path('creator_registration/',views.creator_registration,name='creator_registration'),

    path('index_creator_confirmation/<int:user_id>/',views.index_creator_confirmation,name='index_creator_confirmation'),
    path('staff_home/',views.staff_home,name='staff_home'),
    path('staff_validate/',views.staff_validate,name='staff_validate'),
    ############################################################ <<<<<<<<< User MODULE >>>>>>>>>>>>>>>>>

    path('artist_registration/',views.artist_registration,name='artist_registration'),
    path('index_artist_confirmation/<int:user_id>/',views.index_artist_confirmation,name='index_artist_confirmation'),
    path('profile_user_creation/',views.profile_user_creation,name='profile_user_creation'),
    
    path('user_home/',views.user_home,name='user_home'),

    
    ]