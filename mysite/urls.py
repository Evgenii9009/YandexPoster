from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from mysite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_main),
    path('places/<int:place_id>/', views.place_detail)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)