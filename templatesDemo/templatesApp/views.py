from django.shortcuts import render


def renderTemplate(request):
    myDict = {"name": "Bharath"}
    return render(request, 'templatesApp/firstTemplate.html', myDict)


def renderEmployee(request):
    myDict = {"id": 123, "name": "John", "sal": 10000}
    return render(request, 'templatesApp/employeeTemplate.html', myDict)
