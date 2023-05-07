from django.contrib import admin

from .models import Flat, Complaint, Owner


class PropertyOwnerOwnedFlats(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner',)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ('created_at',)
    list_display = ('address', 'price',
                    'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)
    inlines = (PropertyOwnerOwnedFlats,)


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ("complainant", "flat", "text")
    raw_id_fields = ("complainant", "flat")


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    search_fields = ('owner',)
    list_display = ('owner', 'phonenumber', 'pure_phonenumber')
