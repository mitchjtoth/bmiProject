from django.test import TestCase
from django.test import RequestFactory
from bmiCalc.views import calculate_bmi
from django.test import Client

# Create your tests here.
def test_one():

    assert 1 == 1


# def test_calculate_bmi():
#     # Create a request object with POST data
#     data = {'weight': '150', 'height_feet': '5', 'height_inches': '6'}
#     request = RequestFactory().post('/', data=data)
    
#     # Call the view function and get the response
#     response = calculate_bmi(request)
#     context = response.context
#     # Check that the response has the expected content
#     assert response.status_code == 200
#     assert 'bmi' in context
#     assert 'bmiResult' in context
#     assert context['bmi'] == 24.8
#     assert context['bmiResult'] == 'Your bmi is normal weight'

def test_calculate_bmi():
    client = Client()
    response = client.post('', {'weight': '150', 'height_feet': '5', 'height_inches': '8'})
    assert response.status_code == 200
    assert 'bmi' in response.context
    assert 'bmiResult' in response.context
    assert response.context['bmi'] == 23.4
    assert response.context['bmiResult'] == 'Your bmi is normal weight'