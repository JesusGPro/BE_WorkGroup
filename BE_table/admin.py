from django.contrib import admin

from .models import FollowupBE

admin.site.site_header = 'FCS Bulk Emulsion Administration' # default: "Django Administration"
admin.site.index_title = 'FCS Bulk Emulsion Dashboard' # default: "Site administration"
admin.site.site_title = 'FCS BE Admin' # default: "Django site admin"

@admin.register(FollowupBE)
class FollowupBEAdmin(admin.ModelAdmin):
    list_display = ['date', 'tunnel_location', 'advance', 'blast_time', 'holes_total_number', 'holes_length', 'cut_holes_kg', 'stop_holes_kg',
                     'bottom_holes_kg', 'perimeter_holes_kg', 'contour_holes_kg', 'incident_time_lost', 'total_quantity',
                     'created_at', 'edited_at', 'username_field',]  # Fieds to display in the list view
    
