from django.contrib import admin
from .models import Contact, Member, Allperson

# Register your models here.
admin.site.register(Contact)
admin.site.register(Member)
admin.site.register(Allperson)
