from django.urls import path, include

from product import views

urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view()),
    path('products/search/', views.search),
    path('subscribe/', views.api_add_subscriber),
    path ('products/', views.ProductsDetailView.as_view({'get': 'list'})),
    path('products/highlightedproducts/', views.HighlightedProductDetail.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
    path('images/<slug:product_slug>/<slug:image_slug>/', views.ImageDetail.as_view()),
]