# from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from firstApp.models import Parliament1
from rest_framework import filters
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializer import Parliament1Serializer


class SearchAPIView(generics.ListCreateAPIView):
    """With endpoint search/ it return results filtered by name"""

    permission_classes = [AllowAny]
    http_method_names = ["get"]
    serializer_class = Parliament1Serializer
    search_fields = ["name"]
    filter_backends = (filters.SearchFilter,)
    queryset = Parliament1.objects.all()


class Parliament1Viewset(viewsets.ModelViewSet):
    """return whole list or search endpoint for /dob /id /pp"""

    permission_classes = [AllowAny]
    http_method_names = ["get"]
    serializer_class = Parliament1Serializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["pp", "dob"]
    queryset = Parliament1.objects.all()


class Parliament1Viewsetpp(viewsets.ModelViewSet):
    """Return whole list or parameter filtered /mp(id) /pp /dob"""

    permission_classes = [AllowAny]
    http_method_names = ["get"]  # Allow only GET requests
    serializer_class = Parliament1Serializer

    def get_queryset(self):
        """
        Filtering against 'id','pp' and 'dob' query parameter in the URL.
        """
        queryset = Parliament1.objects.all()
        id = self.request.query_params.get("mp")
        pp = self.request.query_params.get("pp")
        dob = self.request.query_params.get("dob")
        if id is not None:
            # endpoint: ?mp=21
            queryset = queryset.filter(id=id)  # return filtered by id
            return queryset
        if pp is not None:
            # endpoint: ?mp=21
            queryset = queryset.filter(pp=pp)  # return filtered by pp
            return queryset
        if dob is not None:
            queryset = queryset.filter(dob=dob)  # return filtered by dob
            return queryset
        return queryset  # return whole list
