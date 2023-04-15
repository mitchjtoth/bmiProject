from django.test import TestCase
from django.test import RequestFactory
from bmiCalc.views import calculate_bmi
from django.test import Client
from django.urls import reverse
import pytest

# class CalculateBMITests(TestCase):
#     def test_get(self):
#         response = self.client.get('')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'bmiCalc/calculate_bmi.html')
        
#     def test_post_valid_input(self):
#         response = self.client.post('', {'weight': '150', 'height_feet': '5', 'height_inches': '10'})
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'bmiCalc/calculate_bmi.html')
#         self.assertContains(response, 'Your BMI is')
        
#     def test_post_invalid_input(self):
#         response = self.client.post('', {'weight': '', 'height_feet': '5', 'height_inches': '10'})
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'bmiCalc/calculate_bmi.html')
#         self.assertContains(response, 'Please try again with valid inputs')

# from django.test import TestCase
# from django.test import RequestFactory
# from bmiCalc.views import calculate_bmi
# from django.test import Client
# from django.urls import reverse
# import pytest

# Create your tests here.
def test_one():

    assert 1 == 1

def test_calculate_bmi_normal():
    client = Client()
    response = client.post('', {'weight': '150', 'height_feet': '5', 'height_inches': '8'})
    print(response.context)
    assert response.status_code == 200
    assert 'bmi' in response.context
    assert 'bmiResult' in response.context
    assert response.context['bmi'] == 23.4
    assert response.context['bmiResult'] == 'Your bmi is normal weight'

def test_calculate_bmi_norm():
    client = Client()
    response = client.post('', {'weight': '110.5', 'height_feet': '5', 'height_inches': '5'})
    print(response.context)
    assert response.status_code == 200
    assert 'bmi' in response.context
    assert 'bmiResult' in response.context
    assert response.context['bmi'] == 18.8
    assert response.context['bmiResult'] == 'Your bmi is normal weight'

def test_calculate_bmi_obese():
    client = Client()
    response = client.post('', {'weight': '180', 'height_feet': '5', 'height_inches': '2'})
    print(response.context)
    assert response.status_code == 200
    assert 'bmi' in response.context
    assert 'bmiResult' in response.context
    assert response.context['bmi'] == 33.7
    assert response.context['bmiResult'] == 'Your bmi is obese'

def test_calculate_bmi_value_error():
    client = Client()
    url = ''
    response = client.post(url, {'weight': '1001', 'height_feet': '0', 'height_inches': '0'})
    assert response.status_code == 200
    assert 'Please try again with valid inputs' in response.content.decode('utf-8')