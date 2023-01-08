from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('newpage/', views.new_page, name = 'newpage'),
    path('wiki/<str:title>', views.entry, name = 'entries')
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

