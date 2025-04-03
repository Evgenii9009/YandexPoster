from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from mysite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_main)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)