from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Patient
import uuid

class PatientTests(APITestCase):
    # create a sample Patient object to use in the tests.
    def setUp(self):
        self.patient = Patient.objects.create(
            id=uuid.uuid4(),
            first_name = "John",
            last_name = "Doe",
            date_of_birth = "1994-06-04",
            status = True
        )

    # test intro message
    def test_view_intro(self):
        url = reverse('intro')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Welcome to Patient Directory Management')

    # test GET '/patients' endpoint for listing all patients
    def test_view_patient_list_get(self):
        url = reverse('patient_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)

    # test POST '/patients' endpoint for creating new patients
    def test_view_patient_list_post(self):
        url = reverse('patient_list')
        data = {
            "first_name": "Jane",
            "last_name": "Doe",
            "date_of_birth": "1974-06-04",
            "gender": "M",
            "status": False
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['data']['first_name'], 'Jane')
        self.assertEqual(response.data['data']['age'], 50)

    # test GET '/patients/<id>' endpoint for retrieving data for single patient
    def test_view_single_patient_get(self):
        url = reverse('single_patient', args=[self.patient.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['first_name'], 'John')
        self.assertEqual(response.data['data']['age'], 30)

    # test PUT '/patients/<id>' endpoint for fully updating data for single patient
    def test_view_single_patient_put(self):
        url = reverse('single_patient', args=[self.patient.id])
        data = {
            "first_name": "Jack",
            "last_name": "Donald",
            "date_of_birth": "1984-06-04",
            "gender": "M",
            "status": True
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['last_name'], 'Donald')
        self.assertEqual(response.data['data']['age'], 40)

    # test PATCH '/patients/<id>' endpoint for partially updating  data for single patient
    def test_view_single_patient_patch(self):
        url = reverse('single_patient', args=[self.patient.id])
        data = {
            "last_name": "Kirsten"
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['last_name'], 'Kirsten')

    # test DELETE '/patients/<id>' endpoint for deleting single patient
    def test_view_single_patient_delete(self):
        url = reverse('single_patient', args=[self.patient.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Patient.objects.count(), 0)
