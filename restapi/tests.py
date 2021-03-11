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
            "amount": 50.0,
            "merchant": "AT",
            "description": "bill payment",
            "category": "utilities",
        }

        res = self.client.post(
            reverse("restapi:expense-list-create"), payload, format="json"
        )
        self.assertEqual(201, res.status_code)

        jsno_res = res.json()
        self.assertEqual(payload["amount"], jsno_res["amount"])
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

    def test_expense_create_required_fields_missing(self):
        payload = {
            "merchant": "AT",
            "description": "bill payment",
            "category": "utilities",
        }

        res = self.client.post(
            reverse("restapi:expense-list-create"), payload, format="json"
        )
        self.assertEqual(400, res.status_code)

    def test_expense_retrieve(self):
        expense = models.expense.objects.create(
            amount=500,
            merchant="Nagariya cloth",
            description="Cloth daily wear",
            category="Cloth",
        )
        res = self.client.get(
            reverse("restapi:expense-retrieve-delete", args=[expense.id]), format="json"
        )

        self.assertEqual(200, res.status_code)
        json_res = res.json()

        self.assertEqual(expense.id, json_res["id"])
        self.assertEqual(expense.amount, json_res["amount"])
        self.assertEqual(expense.description, json_res["description"])
        self.assertEqual(expense.category, json_res["category"])

    def test_expense_delete(self):
        expense = models.expense.objects.create(
            amount=500,
            merchant="Nagariya cloth",
            description="Cloth daily wear",
            category="Cloth",
        )
        res = self.client.delete(
            reverse("restapi:expense-retrieve-delete", args=[expense.id]), format="json"
        )
        self.assertEqual(204, res.status_code)

        self.assertFalse(models.expense.objects.filter(pk=expense.id).exists())
