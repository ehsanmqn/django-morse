from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from Morse_api.morse import MorseCode

import json
import base64

class TestMorseAPI(APITestCase):
    def test_input_required(self):
        url = self._get_url()

        data = {}

        response = self.client.post(url, data, format='multipart')

        parsed_response = json.loads(response.content)
        self.assertIn('input', parsed_response)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_morse_api(self):
        url = self._get_url()

        input_string = 'This is a test for Morse API'
        data = {'input': input_string}

        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        parsed_response = json.loads(response.content)

        self.assertIn('morse', parsed_response)
        response_morse = parsed_response['morse']
        self.assertEqual(input_string.upper(), MorseCode.decode(base64.b64decode(response_morse).decode("utf-8")))

    def _get_url(self):
        return reverse('morse')