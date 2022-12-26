from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as login_view

from .views import index

urlpatterns = [
    path('login/', login_view.LoginView.as_view(), name="login"),
    path('logout/', login_view.LogoutView.as_view(), name="logout"),
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('rooms/', include('rooms.urls')),
    path('owner/', include('owner.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)