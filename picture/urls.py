from django.urls import path
from . import views
from django.conf.urls.static  import static
from django.conf import settings

app_name = "picture"


urlpatterns = [
    path("movie/<int:movie_id>", views.movie, name="movie"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)