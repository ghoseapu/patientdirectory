# This file declares PatientsConfig class (subclass of django.apps.AppConfig)
# that represents Rest CRUD Apis app and its configuration.

from django.apps import AppConfig

class PatientsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'patients'

# Note: We can set default type to UUID instead of Integer by following 2 steps:
# Step 1: Create a UUIDModel class in patients/models.py
# Step 2: Set default_auto_field = 'django.db.models.UUIDField' here in line 7
