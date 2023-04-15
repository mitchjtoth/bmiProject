import django
django.setup()
from django.http import HttpResponse
from django.shortcuts import render

# merged all of the previous functions just to clean up the clutter
def calculate_bmi(request):
    if request.method == 'POST':
        weight = request.POST.get('weight')
        height_feet = request.POST.get('height_feet')
        height_inches = request.POST.get('height_inches')
        
        # validate input
        try:
            # make sure inputs are the right data types
            if weight is not None:
                weight = float(weight)
            if height_feet is not None:
                height_feet = int(height_feet)
            if height_inches is not None:
                height_inches = int(height_inches)
            else:
                raise ValueError()
            # check if input's break any weird boundary
            if weight < 1 or weight > 1000 or weight is None or height_feet is None or height_feet < 1 or height_feet > 10 or height_inches is None or height_inches < 0 or height_inches > 11:
                # raise a value error
                raise ValueError()
            elif type(weight) == str or type(height_inches) == str or type(height_feet) == str:
                raise ValueError()
        except ValueError:
            # send the response to the html template
            return render(request, 'bmiCalc/calculate_bmi.html', {'message': 'Please try again with valid inputs'})

        
        # calculate the bmi using the given formula
        weight = float(weight) * 0.45
        height = float(height_feet) * 12 + float(height_inches)
        height = float(height) * 0.025
        height = height**2
        bmiScore = weight / height
        
        # round the bmi score
        bmi = round(bmiScore, 1)
        if bmi is None:
            return render(request, 'bmiCalc/calculate_bmi.html', {'message': 'Error: BMI could not be calculated'})
        elif bmi < 18.5:
            bmiResult = 'Your bmi is underweight'
        elif bmi >= 18.5 and bmi < 25:
            bmiResult = 'Your bmi is normal weight'
        elif bmi < 30:
            bmiResult = 'Your bmi is overweight'
        elif bmi > 100:
            return render(request, 'bmiCalc/calculate_bmi.html', {'message': 'Error: BMI cannot be that high of a number. Please try new values'})
        else:
            bmiResult = 'Your bmi is obese'

        context = {'bmi': bmi, 'bmiResult': bmiResult}
        return render(request, 'bmiCalc/calculate_bmi.html', context)
    return render(request, 'bmiCalc/calculate_bmi.html')