from django.contrib import admin
from .models import Team
from .models import Analytic

# Register your models here.
"""teams model registration"""
admin.site.register(Team)
admin.site.register(Analytic)