from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Event, Venue


class EventAdmin(ModelAdmin):
    model = Event
    menu_icon = 'date'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('title', 'start_time', 'embargo_until')
    list_filter = ('embargo_until', )
    search_fields = ('title',)

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(EventAdmin)

class VenueAdmin(ModelAdmin):
    model = Venue
    menu_icon = 'site'  # change as required
    menu_order = 250  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('name', )
    search_fields = ('title',)

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(VenueAdmin)
