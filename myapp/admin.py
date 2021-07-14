from django.contrib import admin
from myapp.models import Button, RequiredButton

# Register your models here.
admin.site.register(Button)
admin.site.register(RequiredButton)
# admin.site.register(DimmingButton)
