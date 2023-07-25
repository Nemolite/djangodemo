from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', index,name='index'),
    path('category/<int:id>/',category,name='category' ),
    path('product/<int:id>/',product,name='product' ),
    path('onas/',onas,name='onas' ),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)