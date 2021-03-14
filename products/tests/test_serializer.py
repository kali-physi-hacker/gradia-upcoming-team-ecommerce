from django.test import TestCase
from products.serializers import ProductSerializer


class ProductSerializerTest(TestCase):
    def setUp(self):
        self.title = "Product Title"
        self.description = "Product's description"
        self.price = 100.00

        self.data = {
            "title": self.title,
            "description": self.description,
            "price": self.price,
        }

        self.error_message = "This field is required."

    def test_object_creation(self):
        """
        Test that product can be created with title, description and price as mandatory fields
        return:
        """
        serializer = ProductSerializer(data=self.data)
        self.assertTrue(serializer.is_valid())
        product = serializer.save()

        self.assertEqual(product.title, self.title)
        self.assertEqual(product.description, self.description)
        self.assertEqual(product.price, self.price)
        self.assertTrue(product.is_active)
        self.assertTrue(product.available)

    def test_object_is_not_created_without_required_fields(self):
        """
        Tests that product is not created if title, description or price
        return:
        """
        data1 = self.data.copy()
        del data1["title"]

        serializer = ProductSerializer(data=data1)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors.get("title")[0], self.error_message)

        data2 = self.data.copy()
        del data2["description"]

        serializer = ProductSerializer(data=data2)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors.get("description")[0], self.error_message)

        data3 = self.data.copy()
        del data3["price"]

        serializer = ProductSerializer(data=data3)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors.get("price")[0], self.error_message)
