from django.urls import path

from . import views

urlpatterns = [
    path('', views.PublisherListView.as_view()),
    path('banco/', views.BankChooseTemplate.as_view()),
    path('banco/compra/', views.PaymentKind.as_view())
    ]
