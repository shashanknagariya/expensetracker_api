from django.contrib import admin
from django.urls import path, include
from restapi import views

urlpatterns = [
    path("expense/", views.ExpenseListCreate.as_view(), name="expense-list-create")
]
