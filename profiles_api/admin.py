from django.contrib import admin

from profiles_api import models

#Making accessible through the Django admin web interface all the database for users
admin.site.register(models.UserProfile)
