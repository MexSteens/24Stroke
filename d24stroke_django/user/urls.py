from django.urls import path, include

from user import views

urlpatterns = [
    path('billingaddress/', views.BillingAddressList.as_view()),
    path('billingaddress/<int:user_id>/', views.BillingAddressDetail.as_view()),
    path('useraddress/', views.UserAddressList.as_view()),
    path('useraddress/<int:user_id>/', views.UserAddressDetail.as_view()),
]