from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('newpage/', views.new_page, name = 'newpage'),
    path('entries/', views.view_entry, name = 'entry')
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

