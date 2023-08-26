from django.contrib import admin

from django.contrib import admin

from apps.store.models import Ad, Category, District, Region, Photo, SubCategory


class ApplicateUserAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'project_name']
    search_fields = ['full_name', 'project_name']


class AdAdmin(admin.ModelAdmin):
    search_fields = ['name']


class RegionAdmin(admin.ModelAdmin):
    search_fields = ['name']



class DistrictAdmin(admin.ModelAdmin):
    search_fields = ['name']



class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']



class SubCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name', 'category']


admin.site.register(Ad, AdAdmin)
# admin.site.register(SubCategory, SubSellerAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
