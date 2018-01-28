# Imports
from django.contrib import admin
from .models import UserProfile, Title, Country, MembershipLevel, PaymentMethod

# Register your models here.
class CountryModelAdmin(admin.ModelAdmin):
    list_display=["name"]
    list_filter = ["name"]
    search_fields = ['name']
    class Meta:
        model = Country


admin.site.register(UserProfile)
admin.site.register(Title)
admin.site.register(Country, CountryModelAdmin)
admin.site.register(MembershipLevel)
admin.site.register(PaymentMethod)
