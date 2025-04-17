from django.shortcuts import render


def employee_overview(request):

   # Hier die entsprechenden Filter anlegen und die context-Variable definieren, um die Daten an das Template zu übergeben

    return render(request, 'employees/employee_list.html')
