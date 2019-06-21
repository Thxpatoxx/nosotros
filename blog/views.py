from django.shortcuts import render, get_object_or_404
from .models import Diagnostico,Paciente
from .forms import DiagnosticoForm,PacienteForm
from django.shortcuts import redirect
from django.contrib.auth.models import User

def post_list(request):
    Diagnosticos = Diagnostico.objects.all()
    return render(request, 'blog/post_list.html', {'Diagnosticos': Diagnosticos})
def post_list_pacient(request):
    Pacientes = Paciente.objects.all()
    return render(request, 'blog/post_list_pacient.html', {'Pacientes': Pacientes})
#########################################################################################
def intro(request):
    return render(request, 'blog/intro.html')
def user_list(request):
    users = User.objects.all()
    return render(request, 'blog/user_list.html',{'users': users})
#########################################################################################
def post_detail(request, pk):
    Diagnosticos = get_object_or_404(Diagnostico, pk=pk)
    return render(request, 'blog/post_detail.html', {'Diagnosticos': Diagnosticos})
def post_detail_pacient(request, pk):
    Pacientes = get_object_or_404(Paciente, pk=pk)
    Diagnosticos = Diagnostico.objects.all()
    return render(request, 'blog/post_detail_pacient.html',{'Diagnosticos': Diagnosticos,'Pacientes': Pacientes})
#########################################################################################
def post_new(request):
    if request.method == "POST":
        form = DiagnosticoForm(request.POST)
        if form.is_valid():
            Diagnostico = form.save(commit=False)
            Diagnostico.author = request.user
            Diagnostico.save()
            return redirect('post_detail', pk=Diagnostico.pk)
    else:
        form = DiagnosticoForm()
    return render(request, 'blog/post_edit.html', {'form': form})
def post_edit(request, pk):
    Diagnosticos = get_object_or_404(Diagnostico, pk=pk)
    if request.method == "POST":
        form = DiagnosticoForm(request.POST, instance=Diagnosticos)
        if form.is_valid():
            Diagnosticos = form.save(commit=False)
            Diagnosticos.author = request.user
            Diagnosticos.save()
            return redirect('post_detail', pk=Diagnosticos.pk)
    else:
        form = DiagnosticoForm(instance=Diagnosticos)
    return render(request, 'blog/post_edit.html', {'form': form})
def post_new_pacient(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            Paciente = form.save(commit=False)
            Paciente.author = request.user
            Paciente.save()
            return redirect('post_detail_pacient', pk=Paciente.pk)
    else:
        form = PacienteForm()
    return render(request, 'blog/post_edit_pacient.html', {'form': form})
def post_edit_pacient(request, pk):
    Pacientes = get_object_or_404(Paciente, pk=pk)
    if request.method == "POST":
        form = PacienteForm(request.POST, instance=Pacientes)
        if form.is_valid():
            Pacientes = form.save(commit=False)
            Pacientes.author = request.user
            Pacientes.save()
            return redirect('post_detail_pacient', pk=Pacientes.pk)
    else:
        form = PacienteForm(instance=Pacientes)
    return render(request, 'blog/post_edit_pacient.html', {'form': form})