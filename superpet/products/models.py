from django.db import models
from autoslug import AutoSlugField

# Create your models here.
#=============================================
#           custome product manager
#==========================================
class ProductManager(models.Manager):
    #whenever you will call all()funcation get_queryset will be invoked
    def get_queryset(self) :
       # return super().get_queryset().order_by('product_name')
        return ProductQueryset(self.model)
    
    def royalCanin(self):
        return ProductQueryset(self.model).filter(product_brand="Royal Canin")
    
    def drools(self):
        return ProductQueryset(self.model).filter(product_brand="Drools")
    

#========================================
#      custome product query set
#=========================================
class ProductQueryset(models.QuerySet):
    def range(self,start_price,end_price):
        return self.filter(product_price__range=(start_price,end_price))
    

#==========================================
#           category
#=======================================
class Category(models.Model):
    category_name=models.CharField(max_length=45,default="")
    category_slug=AutoSlugField(populate_from='category_name',unique=True)

    def __str__(self):
        return self.category_name
        

#=======================================
#               product model (default manager-object)
#=======================================


class Product(models.Model):
    product_name=models.CharField(max_length=70,default="product name")
    product_description=models.TextField(default="description")
    product_price=models.PositiveIntegerField(default=0)
    product_brand=models.CharField(max_length=60,default="superpet")
    product_picture=models.ImageField(upload_to="products/",default="")
    Category=models.ForeignKey(Category,on_delete=models.PROTECT,null=True)

#changeing name of manager
    manager=models.Manager()

# custome manager
    cm=ProductManager()

    def __str__(self):
        return self.product_name
    

    
    

