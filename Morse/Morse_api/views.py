import rest_framework
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from Morse_api.serializers import MorseAPISerializer
from Morse_api.morse import MorseCode

import base64

class MorseAPI(APIView):
    def post(self, request):
        request_data = request.data

        serializer = MorseAPISerializer(data=request_data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        return Response({
            'morse': base64.b64encode(bytes(MorseCode.encode(message=data['input']), 'utf-8')),
        }, status=status.HTTP_201_CREATED)