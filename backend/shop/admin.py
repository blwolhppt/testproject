from django.contrib import admin

from .models import Organization, Shop

admin.site.register(Shop)


class OrganizationShopInline(admin.TabularInline):
    model = Shop
    extra = 1


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    inlines = [OrganizationShopInline, ]
