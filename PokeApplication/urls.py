from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pokecheck/', admin.site.urls),
    path('pokecheck/', include('pokecheck.urls')),
]
