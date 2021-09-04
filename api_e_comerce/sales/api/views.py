from django.db.models import Prefetch
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAuthenticatedOrAdminReadOnly
from sales.models import Sale, SaleDetail, PayMethod
from .serializer import SaleSerializer, SaleDetailSerializer


class SaleModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrAdminReadOnly]
    serializer_class = SaleSerializer

    def get_queryset(self):
        if not self.request.user.is_staff:
            return Sale.objects.filter(user=self.request.user)
        else:
            return Sale.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = SaleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if self.request.user == serializer.validated_data['user']:
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response({"error":"El usuario no tiene permiso para crear una venta en esta cuenta"})


class SaleDetailModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrAdminReadOnly]
    serializer_class = SaleDetailSerializer
    queryset = SaleDetail.objects.all()
