from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK as _200_OK,
    HTTP_400_BAD_REQUEST as _400_BAD
)
# Create your views here.

class DefaultView(APIView):
    def post(self, request: Request):
        return Response({"Hello": "World"}, _200_OK)