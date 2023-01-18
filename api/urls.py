

from django.urls import path,include
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

app_name = 'api'
urlpatterns = [

    #Function views
    #path('', name='home'),
    # path('parts/',views.allparts,name='allparts'),
    # path('parts/<str:pk>/',views.partdetail,name='partdetail'),
    # path('suppliers/',views.allsuppliers,name='allsuppliers'),
    # path('suppliers/<int:pk>/',views.supplierdetail,name='supplierdetail'),

    #Class API views
    
    path('',include(router.urls)),  
    path('djangotoken/',ObtainAuthToken.as_view(),name='authview'),   # Django Token
    path('jwtoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwtoken/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('parts/',views.AllpartsAPIView.as_view(),name='allparts'),
    path('parts/<str:pk>/',views.PartdetailAPIView.as_view(),name='partdetail'),
    path('suppliers/',views.AllsuppliersAPIView.as_view(),name='allsuppliers'),
    path('suppliers/<int:id>/',views.SupplierdetailAPIView.as_view(),name='supplierdetail'),  #custom Class-based views require actual fiield name here, not PK
    
    #Generic Views

    # path('parts/',views.PartsListAPIView.as_view(),name='allparts'),
    # path('parts/<str:pk>/',views.RetrieveUpdateDeletePart.as_view(),name='partdetail'),
    # path('suppliers/',views.SuppliersListAPIView.as_view(),name='allsuppliers'),
    # path('suppliers/<int:pk>/',views.RetrieveUpdateDeleteSupplier.as_view(),name='supplierdetail'), 

     
] 






 ######  Routers

 