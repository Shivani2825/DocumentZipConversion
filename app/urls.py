from django.urls import path
from . import views,api_views


urlpatterns = [
    path('',views.signuppage,name='signup'),
    path('saveuser/',views.saveuser,name='saveuser'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('loginuser/',views.loginuser,name='loginuser'),
    path('upload/',views.upload,name='upload'),
    path('download/<int:id>/',views.download,name='download'),
    path('api/register/', api_views.PersonRegistrationAPI.as_view(), name='api-register'),
    path('api/login/', api_views.PersonLoginAPI.as_view(), name='api-login'),
    path('api/upload/', api_views.FilesUploadAPI.as_view(), name='api-upload'),

]


