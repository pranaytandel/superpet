from django.urls import path
from .views import ProductListView
from.views import ProductDetailView
from.views import royalCaninProducts,CategoryDetailView,search,ProductCreateView,ProductUpdateView, ProductDeleteView,ProductAdminView
urlpatterns =[
    path("",ProductListView.as_view(),name="products"),
    path("<int:pk>",ProductDetailView.as_view(),name="productdetail"),
    path("royal-Canin-Products/",royalCaninProducts,name="royalcanin"),
    path("<slug:slug>",CategoryDetailView.as_view(),name="category"),
    path("search/",search,name="search"),
    path("createproduct/",ProductCreateView.as_view(),name="createproduct"),
    path("updateproduct/<int:pk>",ProductUpdateView.as_view(),name="updateproduct"),
    path("deleteproduct/<int:pk>", ProductDeleteView.as_view(),name="deleteproduct"),
    path("product-admin/",ProductAdminView.as_view(),name="product-admin"),
    


]