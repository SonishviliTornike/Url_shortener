from  short_url_app import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('shorten_history/', views.shorten_history,  name='history'),
    path('<str:short_code>/', views.redirect_short_code, name='redirect'),
    path('<str:short_code>/info', views.urls_info, name='info')
]
