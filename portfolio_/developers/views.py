from django.shortcuts import render, get_object_or_404, redirect
from .models import Programmer

def developer_list(request):
    programmers = Programmer.objects.all()
    return render(request, 'developers/developer_list.html', {'programmers': programmers})

def developer_detail(request, pk):
    programmer = get_object_or_404(Programmer, pk=pk)
    return render(request, 'developers/developer_detail.html', {'programmer': programmer})

def add_developer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        language = request.POST.get('language')
        framework = request.POST.get('framework')
        experience = request.POST.get('experience')
        
        Programmer.objects.create(
            name=name,
            surname=surname,
            age=age,
            language=language,
            framework=framework,
            experience=experience
        )
        return redirect('developers:developer_list')
        
    return render(request, 'developers/add_developer.html')