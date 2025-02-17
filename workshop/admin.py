from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Workshop)
admin.site.register(Reviews)
admin.site.register(Admission)
admin.site.site_header = "The Calligarphy "