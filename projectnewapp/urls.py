from django.urls import path,include
from projectnewapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('',views.home, name="home"),
    path('about',views.about, name="about"),
    path('store',views.store, name="store"),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)