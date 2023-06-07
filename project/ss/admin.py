from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(ProductsName)
admin.site.register(category)
admin.site.register(ResAddress)
admin.site.register(ShiAddress)
admin.site.register(Order)
admin.site.register(Complaint)
admin.site.register(offername)
admin.site.register(suboffer)
admin.site.register(orderdetailadmin)
admin.site.register(Payment)

class SizeAdmin(admin.ModelAdmin):
    list_display=("product","name")

admin.site.register(Size , SizeAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=("name","price","brand")

admin.site.register(Product , ProductAdmin)