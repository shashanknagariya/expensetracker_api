# from unittest import TestCase
from django.test import TestCase
from restapi import models
from django.urls import reverse

# Create your tests here.


class Testmodels(TestCase):
    def test_expense(self):
        expense = models.expense.objects.create(
            amount=220,
            merchant="Nagariya Kirana store",
            description="Faltu saman",
            category="Music",
        )
        inserted_expense = models.expense.objects.get(pk=expense.id)

        self.assertEqual(220, inserted_expense.amount)
        self.assertEqual("Nagariya Kirana store", inserted_expense.merchant)
        self.assertEqual("Faltu saman", inserted_expense.description)
        self.assertEqual("Music", inserted_expense.category)


class Testviews(TestCase):
    def test_expense_create(self):
        payload = {
            "amount": 50,
            "merchant": "AT",
            "description": "bill payment",
            "category": "utilities",
        }

        res = self.client.post(
            reverse("restapi:expense-list-create"), payload, format="json"
        )
        self.assertEqual(201, res.status_code)

        jsno_res = res.json()
        self.assertEqual(str(payload["amount"]), jsno_res["amount"])
        self.assertEqual(payload["merchant"], jsno_res["merchant"])
        self.assertEqual(payload["description"], jsno_res["description"])
        self.assertEqual(payload["category"], jsno_res["category"])
        self.assertIsInstance(jsno_res["id"], int)

    def test_expense_list(self):
        res = self.client.get(reverse("restapi:expense-list-create"), format="json")
        self.assertEqual(200, res.status_code)

        json_res = res.json()

        self.assertIsInstance(json_res, list)

        expneses = models.expense.objects.all()
        self.assertEqual(len(expneses), len(json_res))
