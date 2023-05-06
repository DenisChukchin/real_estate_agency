from django.contrib import admin

from .models import Flat, Complaint, Owner


class PropertyOwnerOwnedFlats(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner',)


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ('created_at',)
    list_display = ('address', 'price',
                    'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)
    inlines = (PropertyOwnerOwnedFlats,)


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ("complainant", "flat", "complaint_text")
    raw_id_fields = ("complainant", "flat")


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    search_fields = ('owner',)
    list_display = ('owner', 'owners_phonenumber', 'owner_pure_phone')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
