from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from subscriber.serializers.MobileSubscriberSerializer import MobileSubscriberSerializer, MobSubNumbersSerializer, MobSubUpdateSerializer
from subscriber.models.MobileSubscriberModel import MobileSubscriberModel
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from subscriber.models.services import services
from rest_framework import status


class ListMobSubNumbersAPI(generics.ListAPIView):
    """
    Endpoint to list all MobileSubscriberModel numbers

[
    {
        "msisdn": "+233244124094"
    },
    {
        "msisdn": "+233549724548"
    }
]
    """

    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = MobSubNumbersSerializer

    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend,)
    search_fields = [
        'msisdn',
        'customer_id_owner__email',
        'customer_id_user__email',
        '=service_type',
    ]

    def get_queryset(self):

        return MobileSubscriberModel.objects.all().order_by("-service_start_date")


class CreateMobileSubscriberAPI(generics.CreateAPIView):
    """
    Endpoint to create a MobileSubscriberModel

{
    "id": 3,
    "msisdn": "+233549124195",
    "customer_id_owner": 3,
    "customer_id_user": 3,
    "service_type": "MOBILE_POSTPAID",
    "service_start_date": 1648392306.886409
}
    """

    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = MobileSubscriberSerializer
    queryset = MobileSubscriberModel.objects.all()


class ListMobileSubscriberAPI(generics.ListAPIView):
    """
    Endpoint to list all MobileSubscribers

[
    {
        "id": 3,
        "msisdn": "+233549124195",
        "customer_id_owner": 3,
        "customer_id_user": 3,
        "service_type": "MOBILE_POSTPAID",
        "service_start_date": 1648392306.886409
    },
    {
        "id": 2,
        "msisdn": "+233244122034",
        "customer_id_owner": 2,
        "customer_id_user": 2,
        "service_type": "MOBILE_PREPAID",
        "service_start_date": 1648386228.716224
    }
]
    """

    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = MobileSubscriberSerializer
    queryset = MobileSubscriberModel.objects.all()

    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend,)
    search_fields = [
        'msisdn',
        'customer_id_owner__email',
        'customer_id_user__email',
        '=service_type',
    ]

    def get_queryset(self):

        return MobileSubscriberModel.objects.all().order_by("-service_start_date")


class RetrieveMobSubAPI(generics.RetrieveAPIView):
    """
    Endpoint to retrieve specified MobileSubscriberModel details

{
    "id": 2,
    "msisdn": "+233244122034",
    "customer_id_owner": 2,
    "customer_id_user": 2,
    "service_type": "MOBILE_PREPAID",
    "service_start_date": 1648386228.716224
}
    """

    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = MobileSubscriberSerializer
    queryset = MobileSubscriberModel.objects.all()
    lookup_field = 'pk'


class UpdateMobileSubscriberAPI(generics.UpdateAPIView):
    """
    Endpoint to update specified MobileSubscriberModel details

{
    "id": 2,
    "msisdn": "+233244122034",
    "customer_id_owner": 2,
    "customer_id_user": 2,
    "service_type": "MOBILE_POSTPAID",
    "service_start_date": 1648386228.716224
}
    """

    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = MobSubUpdateSerializer
    queryset = MobileSubscriberModel.objects
    lookup_field = 'pk'

    def put(self, request, pk):
        model = get_object_or_404(MobileSubscriberModel, pk=pk)
        service_type = self.request.data.get('service_type', None)

        if not service_type:
            return Response({
                "service_type": ["This field may not be blank."]
            },
                status=status.HTTP_400_BAD_REQUEST)
        data = {
            "service_type": service_type}
        serializer = MobSubUpdateSerializer(model, data=data, partial=True)
        if serializer.is_valid():
            serializer.update(model, data)
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteMobileSubscriberAPI(generics.DestroyAPIView):
    """
    Endpoint to delete specified Mobile Subscriber
    """
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = MobileSubscriberSerializer
    queryset = MobileSubscriberModel.objects.all()
    lookup_field = 'pk'
