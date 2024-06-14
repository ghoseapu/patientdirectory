# This file manages serialization and deserialization with PatientSerializer class
# (subclass of rest_framework.serializers.ModelSerializer).

# Serializers in Django REST Framework are responsible for converting complex data types,
# such as querysets and model instances, to native Python datatypes
# that can then be easily rendered into JSON, XML, or other content types.
# They also provide deserialization, allowing parsed data to be converted back into complex types,
# after first validating the incoming data.

from rest_framework import serializers
from .models import Patient
from datetime import datetime

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        # fields = ['id', 'first_name', 'last_name', 'gender', 'date_of_birth', 'age', 'status']
        fields = '__all__'
        read_only_fields = ['age']

    # 'age' field value is calculated by using 'date_of_birth' field value
    def create(self, validated_data):
        date_of_birth = validated_data.get('date_of_birth')
        validated_data['age'] = self.calculate_age(date_of_birth)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        validated_data['age'] = self.calculate_age(date_of_birth)
        return super().update(instance, validated_data)

    # calculate age by using birthdate
    def calculate_age(self, birth_date):
        # Get today's date
        today = datetime.today()
        # Parse the date of birth string into a datetime object
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d")

        # Calculate age by subtracting the year of birth from the current year
        age = today.year - birth_date.year

        # Adjust if the birthday hasn't occurred yet this year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age

