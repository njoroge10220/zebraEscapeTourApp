from django.contrib import admin

from .models import Place, Picture, Listing, Contact, Website_Image, Place_Wording,Regular_User

# Register your models here.

admin.site.register(Place)
admin.site.register(Picture)
admin.site.register(Listing)
admin.site.register(Contact)
admin.site.register(Website_Image)
admin.site.register(Place_Wording)
admin.site.register(Regular_User)