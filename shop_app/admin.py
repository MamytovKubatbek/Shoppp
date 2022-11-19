from django.contrib import admin
from .models import *

# Register your models here.
class ClothesAdmin(admin.ModelAdmin):
    list_display=('id', 'clothes_name','price','size', 'color', 'brand_of_clothes','gender_of_clothes','publication', 'sent_at', 'update_at')
    list_display_links=('id', 'clothes_name')
    search_fields = ['clothes_name', 'description']
    list_editable = ('publication',)
    list_filter = ('publication', 'brand_of_clothes')

class OrderAdmin(admin.ModelAdmin):
    list_display=('id', 'full_name','email','phone_number','sent_at')
    list_display_links=('id', 'full_name')
    search_fields = ['full_name',]

admin.site.register(Brand)
admin.site.register(Gender_clothes)
admin.site.register(Clothes,ClothesAdmin)
admin.site.register(Order, OrderAdmin)
