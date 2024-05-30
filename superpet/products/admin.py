from django.contrib import admin
from.models import Product
from.models import Category

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','product_name','product_description','product_price','product_brand','Category']

admin.site.register(Product, ProductAdmin)
#====================================================================


class CategoryAdmin(admin.ModelAdmin):
    list_display=["id","category_name","category_slug"]

admin.site.register(Category,CategoryAdmin)


#admin.site.register(modelName)
#admin.site.register(model)

