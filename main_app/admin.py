from django.contrib import admin

# Register your models here.
from .models import Finch, Feeding, Toy

# Register
admin.site.register(Finch)
admin.site.register(Feeding)
admin.site.register(Toy)
