from django.contrib import admin

from hms.models import Contact_us, Doctor, Document, UpdateNew,UserProfile,Appointment

# Register your models here.

admin.site.register(Contact_us)
admin.site.register(UserProfile)
admin.site.register(Appointment)
admin.site.register(Document)
admin.site.register(UpdateNew)
admin.site.register(Doctor)