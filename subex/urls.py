from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from subject.views import *

app_name='subject'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('subject/', SubjectLV.as_view(), name='index'),
    path('subject/<int:pk>/', SubjectDV.as_view(), name='detail'),
    path('search', search, name='searchview'),
    path('', SearchView.as_view(), name='search'),
    path('tag/<str:tag>/',TaggedObjectLV.as_view(), name='tagged_object_list')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)