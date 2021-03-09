# from unittest import TestCase
from django.test import TestCase
from restapi import models

# Create your tests here.


class Testmodels(TestCase):
    def test_expense(self):
        expense = models.expense.objects.create(
            amount=220,
            merchant="Nagariya Kirana store",
            descrption="Faltu saman",
            category="Music",
        )
        inserted_expense = models.expense.objects.get(pk=expense.id)

        self.assertEqual(200, inserted_expense.amount)
        self.assertEqual("Nagariya Kirana store", inserted_expense.merchant)
        self.assertEqual("Faltu saman", inserted_expense.description)
        self.assertEqual("Music", inserted_expense.category)
