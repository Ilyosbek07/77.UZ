from django.contrib import admin
from apps.store.models import PopularSearch, Category, SubCategory, Ad, Photo, Address, District, Region

admin.site.register(PopularSearch)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Ad)
admin.site.register(Photo)
admin.site.register(Address)
admin.site.register(District)
admin.site.register(Region)
