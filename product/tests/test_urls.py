from django.test import TestCase
from django.urls import reverse
from product.models import Product


class TestUrls(TestCase):

    def test_products_url(self):
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_products_detail_url_404(self):
        url = reverse('product-detail', args=[1])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_products_detail_url_200(self):
        Product.objects.create(
            name='Кефир',
            cost=30.5,
            price=50.9,
            count=10,
        )
        url = reverse('product-detail', args=[1])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
