from django.contrib import admin




from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title','slug',
        'price',
        'discount',
        'description',
        'condition',
        'seller',
        'delivery_type',
        'is_active',
        'created_on',
        'updated_on','get_rating'
    )
    prepopulated_fields = {"slug": ("title","description")}

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(ProductImage)
admin.site.register(ProductVideo)
admin.site.register(ProductQuestion)
admin.site.register(ProductReview)
admin.site.register(Tag)
admin.site.register(DeliveryType)
admin.site.register(BrowsingHistory)
 