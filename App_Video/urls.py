from django.urls import path
from . import views

app_name = "App_Video"

urlpatterns = [
    path("", views.VideoList, name="video_list_t"),
    path("upload/", views.UploadVideo.as_view(), name="upload_video"),
    path("details/<slug:slug>/", views.video_details, name="video_details"),
]
