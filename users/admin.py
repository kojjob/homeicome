from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

  """Custom UserAdmin"""

  list_display = ("username", "gender", "language", "currency", "superhost" )
  list_filter = ("superhost", "currency", "language") 