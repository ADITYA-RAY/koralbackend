from django.shortcuts import render
from rest_framework import viewsets
from .serializers import QuotationSerializer
from .models import Quotation

# Create your views here.


class QuotationView(viewsets.ModelViewSet):
    serializer_class = QuotationSerializer
    queryset = Quotation.objects.all()


def index(request):
    return render(request, 'index.html')
