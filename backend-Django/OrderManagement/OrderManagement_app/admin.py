from django.contrib import admin

#from django.contrib import admin
from .models import OtherOrdersExcluded,Customer,Product,Order

class UserAdmin_Orders(admin.ModelAdmin):
        list_display = ('name', 'price', 'created', 'updated')

class UserAdmin_Product(admin.ModelAdmin):
    list_display = ('name', 'price', 'type')
class UserAdminCustomer(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')

class UserAdmin_Order(admin.ModelAdmin):
    list_display = ('customer', 'date', 'notes', 'last_updated', 'created_at')


admin.site.register(OtherOrdersExcluded, UserAdmin_Orders)
admin.site.register(Product,UserAdmin_Product)
admin.site.register(Order,UserAdmin_Order)
admin.site.register(Customer,UserAdminCustomer)
