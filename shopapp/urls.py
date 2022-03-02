from django.urls import path
from. import views
app_name='shopapp'
urlpatterns = [

    path('',views.allProdcat,name='allProdcat'),
    path('<slug:c_slug>/',views.allProdcat,name='allb'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetails, name='proCatD'),

    ]
