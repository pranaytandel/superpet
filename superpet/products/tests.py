from django.test import TestCase
from.models import Product

def add(a,b):
    return a+b

# Create your tests here.
class ProductTEST(TestCase):

    def setUp(self):
        self.product=Product.manager.create(product_name="testProduct", 
                               product_price=2500,
                               product_brand="Superpet",
                               product_picture="abc.jpeg",
                               product_description="description for test")
    

    def test_create_product(self):
        product=Product.manager.get(id=self.product.id)
        self.assertEqual(self.product,product)
        


    def test_add(self):
        self.assertEqual(add(5,5),10)

    
    def test_all_products(self):
        product=Product.manager.all()
        self.assertTrue(len(product)>0)
