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

@pytest.fixture
def client():
    client = Client()
    return client

def test_calculate_bmi(client):
    response = client.post('', {'weight': 150, 'height_feet': 5, 'height_inches': 8})
    assert response.status_code == 200
    assert 'bmi' in response.context
    assert 'bmiResult' in response.context
    assert response.context['bmi'] == 23.4
    assert response.context['bmiResult'] == 'Your bmi is normal weight'


def test_calculate_bmi_with_missing_fields(client):
    response = client.post('', {'weight': '', 'height_feet': 5, 'height_inches': 8})
    assert response.status_code == 200
    assert 'message' in response.context
    assert response.context['message'] == "could not convert string to float: ''"


def test_calculate_bmi_with_invalid_fields(client):
    response = client.post('', {'weight': 1500, 'height_feet': -5, 'height_inches': 20})
    assert response.status_code == 200
    assert 'message' in response.context
    assert response.context['message'] == 'Please try again with valid inputs'


def test_calculate_bmi_with_high_bmi(client):
    response = client.post('', {'weight': 1000, 'height_feet': 5, 'height_inches': 8})
    assert response.status_code == 200
    assert 'message' in response.context
    assert response.context['message'] == 'Error: BMI cannot be that high of a number. Please try new values'

#Need to fix integration tests 

# from django.test import LiveServerTestCase
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# class BMITest(LiveServerTestCase):
    
#     def setUp(self):
#         self.driver = webdriver.Firefox()
        
#     def tearDown(self):
#         self.driver.quit()
        
#     def test_calculate_bmi(self):
#         self.driver.get(self.live_server_url)
#         self.assertEqual(self.driver.title, "BMI Calculator")
        
#         weight_field = self.driver.find_element_by_name('weight')
#         height_feet_field = self.driver.find_element_by_name('height_feet')
#         height_inches_field = self.driver.find_element_by_name('height_inches')
        
#         weight_field.send_keys('150')
#         height_feet_field.send_keys('5')
#         height_inches_field.send_keys('7')
        
#         submit_button = self.driver.find_element_by_xpath('//input[@type="submit"]')
#         submit_button.send_keys(Keys.RETURN)
        
#         bmi_element = self.driver.find_element_by_xpath('//p[contains(text(), "Your BMI is ")]')
#         self.assertIsNotNone(bmi_element)