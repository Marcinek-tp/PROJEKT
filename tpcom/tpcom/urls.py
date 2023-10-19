from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('strona.urls')),
    #path('home/', include('strona.urls')), to nie potrzebne
    path('about/', include('strona.urls')),
    path('contact/', include('strona.urls')),
    path('pricing/', include('strona.urls')),
    path('instrukcje/', include('strona.urls')),
    path('opismMedica/', include('strona.urls')),
    path('kursy/', include('strona.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
