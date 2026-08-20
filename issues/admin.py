from django.contrib import admin
from .models import Reporter, Issue


admin.site.register(Reporter)
admin.site.register(Issue)