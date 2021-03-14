from django.urls import reverse

from rest_framework.test import APITestCase, APIClient

from products.models import Product


class ProductCreateTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.product_data = {"title": "Product 1", "description": "Product Description", "price": 50.00}

        self.required_error_message = "This field is required."

    def test_product_creation_success(self):
        """
        Tests that product is created if required fields are passed and returns 201 status code and product
        return:
        """
        response = self.client.post(reverse("product_list"), data=self.product_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["title"], self.product_data.get("title"))
        self.assertEqual(response.json()["description"], self.product_data.get("description"))
        self.assertEqual(float(response.json()["price"]), self.product_data.get("price"))

        product = Product.objects.get(title=self.product_data.get("title"))
        self.assertEqual(product.title, self.product_data.get("title"))
        self.assertEqual(product.description, self.product_data.get("description"))
        self.assertEqual(product.price, self.product_data.get("price"))

    def test_product_creation_failure_if_required_field_missing(self):
        """
        Tests that product creation fails if required field are missing
        return:
        """

        # Test for title missing
        data = self.product_data.copy()
        del data["title"]
        response = self.client.post(reverse("product_list"), data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json().get("title")[0], self.required_error_message)
        self.assertEqual(len(Product.objects.all()), 0)

        # Test for description missing
        data = self.product_data.copy()
        del data["description"]
        response = self.client.post(reverse("product_list"), data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json().get("description")[0], self.required_error_message)
        self.assertEqual(len(Product.objects.all()), 0)

        # Test for price missing
        data = self.product_data.copy()
        del data["price"]
        response = self.client.post(reverse("product_list"), data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json().get("price")[0], self.required_error_message)
        self.assertEqual(len(Product.objects.all()), 0)