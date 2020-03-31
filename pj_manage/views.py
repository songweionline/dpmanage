from django.shortcuts import render
from .forms import ProjectForm
# Create your views here.


def add_pj(request):
    if request.method == 'POST':
        formset = ProjectForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
    else:
        formset = ProjectForm()
    return render(request, 'pj_manage/add_test.html', {'formset': formset})