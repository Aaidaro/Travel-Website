from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('', about_view, name= "about"),
    path('resume', resume_view, name= "resume"),
    path('projects', project_view, name= "projects"),
    path('single', project_single_view, name= "single project")
]
