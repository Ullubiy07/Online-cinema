from django.shortcuts import render


def serials_home(request):
    return render(request, 'serials/serials_home.html')
