from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'name': 'hi', 'sname': 'hello'})

# def add(request):
#     val1 = int(request.GET['no1'])  # Convert to integer
#     val2 = int(request.GET['no2'])  # Convert to integer
#     res = val1 + val2
#     return render(request, 'result.html', {'result': res})

def add(request):
    if request.method == 'GET':  # Check if the request is a POST
        try:
            val1 = int(request.GET['no1'])  # Convert to integer
            val2 = int(request.GET['no2'])  # Convert to integer
            res = val1 + val2
            return render(request, 'result.html', {'result': res})
        except ValueError:
            return HttpResponse("Invalid input. Please enter valid numbers.")
    return render(request, 'home.html')  # Return the form page if not a POST request
