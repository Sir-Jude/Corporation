from django.contrib import admin
from .models import Corporation

class CorporationAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Main details", {"fields": ["user", "corporation_name", "sector"]}),
        ("Contacts", {"fields": ["address", "phone_number", "email"]}),
        ("Online", {"fields": ["url", "linkedin"]})
    ]
    list_display = ["corporation_name"]
    list_filter = ["user", "sector", "founding_date"]
    search_fields = ["user", "sector", "founding_date"]

admin.site.register(Corporation, CorporationAdmin)