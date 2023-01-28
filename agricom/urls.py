
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', admin.site.urls),
    path('reporter/', include('reporter.urls'))
]
