

from django.urls import path,include


from . import views

app_name = 'api2'

""" 
urlpatterns = [

    #path('suppliers/',views.SupplierListView.as_view()),
    #path('suppliers/<int:pk>/',views.SupplierDetailView.as_view()),
    path('',views.api_root,name='Home'),
    path('suppliers/',views.GenericSupplierList.as_view(),name='SupplierList'),
    path('suppliers/<int:pk>/',views.GenericSupplierDetail.as_view(),name='SupplierDetails'),



]
 """


#  ######  Routers

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'suppliers',views.SupplierViewset,basename="supplier")
router.register(r'parts',views.PartsViewset,basename="part")

urlpatterns =  [
 
    path('',include(router.urls)),  

 ]