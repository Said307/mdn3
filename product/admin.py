from django.contrib import admin




from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title','slug',
        'price',
        'discount',
        'description',
        'condition','category',
        'seller',
        'delivery_type','get_tags',
        'is_active',
        'created_on',
        'updated_on','get_rating'
    )
    prepopulated_fields = {"slug": ("title","description")}



class ProductQuestionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'text', 'reply','created_on','updated_on'
    )

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title', 'parent','created_on','updated_on'
    )

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductCategory,ProductCategoryAdmin)
admin.site.register(ProductImage)
admin.site.register(ProductVideo)
admin.site.register(ProductQuestion,ProductQuestionAdmin)
admin.site.register(ProductReview)
admin.site.register(Tag)
admin.site.register(DeliveryType)
admin.site.register(BrowsingHistory)
 