from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from restapi import models, serializers
from django.forms.models import model_to_dict

# Create your views here.
class ExpenseListCreate(APIView):
    def get(self, request):
        expenses = models.expense.objects.all()

        # all_expenses = [model_to_dict(expenses) for expense in expenses]

        serializer = serializers.Expense(expenses, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        # amount = request.data["amount"]
        # merchant = request.data["merchant"]
        # description = request.data["description"]
        # category = request.data["category"]

        # expense = models.expense.objects.create(
        #     amount=amount, merchant=merchant, description=description, category=category
        # )

        serializer = serializers.Expense(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
