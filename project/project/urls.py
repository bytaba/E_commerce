from django.contrib import admin
from django.urls import path , include
from .            import views

urlpatterns = [
    path('admin/'    , admin.site.urls                            ),
    path( ''         , views.home_view         , name='home_view' ),
    path('account/'  , include('account.urls') , name='account'   )
]
