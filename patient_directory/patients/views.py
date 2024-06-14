# This file contains functions to process HTTP requests and produce HTTP responses (using PatientSerializer).

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Patient
from .serializers import PatientSerializer
from rest_framework import status
from uuid import UUID

@api_view()
def view_intro(request):
    return Response({'success': 409, 'message': 'Welcome to Patient Directory Management'})

@api_view(['GET', 'POST'])
def view_patient_list(request):
    # GET method to retrieve all patients
    if request.method == 'GET':
        patient_obj = Patient.objects.all()
        serializer = PatientSerializer(patient_obj, many=True)
        return Response({'msg': 'Successfully retrieved data', 'data': serializer.data}, status=status.HTTP_200_OK)

    # POST method to create a new patient
    elif request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Patient created successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'msg': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def view_single_patient(request, id: UUID):
    # GET method to retrieve single patient by id
    if request.method == 'GET':
        patient_obj = Patient.objects.get(id=id)
        serializer = PatientSerializer(patient_obj)
        return Response({'msg': 'Successfully retrieved data', 'data': serializer.data}, status=status.HTTP_200_OK)

    # PUT method to update a patient (full update)
    elif request.method == 'PUT':
        patient_obj = Patient.objects.get(id=id)
        serializer = PatientSerializer(patient_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Patient updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PATCH method to partially update a patient
    elif request.method == 'PATCH':
        patient_obj = Patient.objects.get(id=id)
        serializer = PatientSerializer(patient_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Patient updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE method to delete a patient
    elif request.method == 'DELETE':
        patient_obj = Patient.objects.get(id=id)
        patient_obj.delete()
        return Response({'msg': 'Patient deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    return Response({'msg': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
