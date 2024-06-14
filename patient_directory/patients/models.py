# This file defines Patient data model class (subclass of django.db.models.Model).

from django.db import models
from datetime import datetime
import uuid

class Patient(models.Model):
    # 1 character length is better than 4-6 characters length value while saving into database table.
    # The tuples would help in displaying 'Male' instead of 'M' (for example) in front end.
    # Boolean is the best type if there are two options. 'status' field has two options (active, inactive)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    date_of_birth = models.CharField(max_length=30, null=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=False)
    age = models.IntegerField(null=False)
    status = models.BooleanField(default=True)

    # The following function will help in setting age value if we add patient using shell command
    def save(self, *args, **kwargs):
        # Get today's date
        today = datetime.today()
        if not self.age:
            # Parse the date of birth string into a datetime object
            birth_date = datetime.strptime(self.date_of_birth, "%Y-%m-%d")

            # Calculate age by subtracting the year of birth from the current year
            self.age = today.year - birth_date.year

            # Adjust if the birthday hasn't occurred yet this year
            if (today.month, today.day) < (birth_date.month, birth_date.day):
                self.age -= 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
