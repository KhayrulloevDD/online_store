import json
import pdb

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class TestProductAPI(APITestCase):

    def setUp(self):
        super().setUp()
        self.product_url = reverse("product-list")
        self.product_detail_url = reverse("product-detail", args=[1])

        self.valid_product_data = {
            "name": 'Кефир',
            "cost": 30.5,
            "price": 50.9,
            "count": 10,
        }

        self.invalid_product_data1 = {
            "name": 'Кефир',
            "cost": -1,
            "price": 50.9,
            "count": 10,
        }

        self.invalid_product_data2 = {
            "name": 'Кефир',
            "cost": 10,
            "price": -2,
            "count": 10,
        }

        self.invalid_product_data3 = {
            "name": 'Кефир',
            "cost": 10,
            "price": 20,
            "count": -2,
        }

    def test_post_method_for_valid_product_data(self):
        response = self.client.post(self.product_url, data=json.dumps(self.valid_product_data),
                                    content_type='application/json')

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response.data, {
            "id": 1,
            "name": "Кефир",
            "cost": 30.5,
            "price": 50.9,
            "count": 10
        })

    def test_post_method_for_invalid_product_data1(self):
        response = self.client.post(self.product_url, data=json.dumps(self.invalid_product_data1),
                                    content_type='application/json')

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response.data, {
            "cost": [
                "Ensure this value is greater than or equal to 0.0."
            ]
        })

    def test_post_method_for_invalid_product_data2(self):
        response = self.client.post(self.product_url, data=json.dumps(self.invalid_product_data2),
                                    content_type='application/json')

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response.data, {
            "price": [
                "Ensure this value is greater than or equal to 0.0."
            ]
        })

    def test_post_method_for_invalid_product_data3(self):
        response = self.client.post(self.product_url, data=json.dumps(self.invalid_product_data3),
                                    content_type='application/json')

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response.data, {
            "count": [
                "Ensure this value is greater than or equal to 0.0."
            ]
        })

    def test_post_method_for_valid_product_data_with_the_same_name(self):
        self.test_post_method_for_valid_product_data()

        response2 = self.client.post(self.product_url, data=json.dumps(self.valid_product_data),
                                     content_type='application/json')

        self.assertEquals(response2.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response2.data, {
            "name": [
                "product with this Название already exists."
            ]
        })

    def test_put_product(self):
        self.test_post_method_for_valid_product_data()
        response = self.client.put(self.product_detail_url, data=json.dumps({
            "name": "Масло",
            "cost": 200,
            "price": 300,
            "count": 199
        }), content_type='application/json')

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data, {
            "id": 1,
            "name": "Масло",
            "cost": 200,
            "price": 300,
            "count": 199
        })

    def test_get_product(self):
        self.test_post_method_for_valid_product_data()
        response = self.client.get(self.product_detail_url, content_type='application/json')

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data, {
            "id": 1,
            "name": "Кефир",
            "cost": 30.5,
            "price": 50.9,
            "count": 10
        })

    def test_get_un_existed_product(self):
        response = self.client.get(self.product_detail_url, content_type='application/json')

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEquals(response.data, {
            "detail": "Not found."
        })

    def test_delete_post(self):
        self.test_post_method_for_valid_product_data()
        response = self.client.delete(self.product_detail_url, content_type='application/json')

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
