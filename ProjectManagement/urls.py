from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("project_user.urls")),
    path('add_project/', include("project_details.urls")),
    path('client/', include("project_clients.urls")),
    path('addition/', include("project_admin.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
