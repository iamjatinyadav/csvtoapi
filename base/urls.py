from django.urls import path
from .views import UploadCSVView, PincodeDataView, PincodeDataDetail, PincodeListView

urlpatterns = [
    path('upload-csv/', UploadCSVView.as_view()),
    path("pincode-data/", PincodeDataView.as_view()),
    path("pincode-data/<int:pk>/", PincodeDataDetail.as_view()),
    path("pincode/", PincodeListView.as_view({'get': 'list'})),
]