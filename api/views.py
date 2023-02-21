from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company, Employee
from api.serializers import CompanySerializers, EmployeeSerializers
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here. 
# Created a class for handling all the views 

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()   # Got all the objcets ffrom models
    serializer_class = CompanySerializers # Initialized serialized_class

#  http://127.0.0.1:8000/api/v1/companies/1/employees/
    # Custom api urls
    @action(detail= True, methods=['get'])
    def employees(self, request, pk=None):  # method name is employees. so it will take employee in URL
        # When the given company_id does not exist
        try:
            company = Company.objects.get(pk = pk)
            emps = Employee.objects.filter(company = company)
            emps_serializers = EmployeeSerializers(emps, many = True, context = {'request': request})
            return Response(emps_serializers.data)
        except Exception as  e :
            return Response({
                'message' : "Company does not exist"
            })




class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
