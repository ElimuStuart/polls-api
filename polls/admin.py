from django.contrib import admin
from .models import Choice, Poll

admin.site.reister(Choice)
admin.site.reister(Poll)
