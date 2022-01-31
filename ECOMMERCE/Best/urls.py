from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('first',views.first,name='first'),
    path('second',views.second,name='second'),
    path('third',views.third,name='third'),
    path('fourth',views.fourth,name='fourth'),
    path('new/<str:slug>',views.product_detailss,name='product_details'),
    path('input',views.p_search,name='input'),
    path('reg',views.reg,name='reg'),
    path('log',views.log,name='log'),
    
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


  


