from django.contrib import admin
from .models import Category, Product, Command


admin.site.site_header = "E-Shop"
admin.site.site_title = "Young-shop"
admin.site.index_title = "The seller"


class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'date_added')


class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_added')
    search_fields = ('title',)
    list_editable = ('price',)


class AdminCommand(admin.ModelAdmin):

    list_display = ('items', 'name', 'email', 'address', 'ville', 'pays','total','command_date')


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Command, AdminCommand)



