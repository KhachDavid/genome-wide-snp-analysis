from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='app_pca/index.html'), name='app_pca_index'),
    path('pca/submit_data/', pca, name='app_pca_pca'),
]