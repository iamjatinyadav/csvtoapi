import csv
import pandas as pd
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PincodeData
from .serializers import PincodeDataSerializer

from rest_framework import viewsets

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend



class UploadCSVView(APIView):
    def post(self, request):
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            return Response({'error': 'Not a CSV file'})

        df = pd.read_csv(csv_file)
        for Pincode,District,StateName in zip(df.Pincode, df.District, df.StateName):
            models = PincodeData(pincode=Pincode, dictrict=District, state=StateName, country="india")
            models.save()
        return Response({'success': 'Data added successfully'})


class PincodeDataView(APIView):

    def get(self, request, format=None):
        snippets = PincodeData.objects.all()
        serializer = PincodeDataSerializer(snippets, many=True)
        return Response(serializer.data)


class PincodeDataDetail(APIView):
    

    def get_object(self, pk):
        try:
            return PincodeData.objects.get(pk=pk)
        except PincodeData.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pincode = self.get_object(pk)
        serializer = PincodeDataSerializer(pincode)
        return Response(serializer.data)



class PincodeListView(viewsets.ReadOnlyModelViewSet):
    queryset = PincodeData.objects.all()
    serializer_class = PincodeDataSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['pincode']
    filterset_fields = ['state',]

    ordering_fields = ('id',)


