from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import (
    Pessoa,
    Veiculo,
    MovimentoRot,
    MovimentoMens,
    Mensalista
)
from .forms import (
    PessoaForm,
    VeiculoForm,
    MovRotForm,
    MensalistaForm,
    MovMensForm
)

def home(request): 
    return render(request,'core/index.html')


@login_required
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    context = {'pessoas':pessoas,'form': form}
    return render(request,'core/lista_pessoas.html',context)


@login_required
def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


@login_required
def pessoa_update(request,id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request,'core/update_pessoa.html',data)


@login_required
def pessoa_delete(request,id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request,'core/delete_confirm.html',{'obj':pessoa})


@login_required
def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    context = {'mensalistas':mensalistas,'form':form}
    return render(request,'core/lista_mensalistas.html',context)


@login_required
def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalistas')


@login_required
def mensalista_update(request,id):
    data = {}
    mensalista = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalista)
    data['mensalista'] = mensalista
    data['form'] = form

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalistas')
    else:    
        return render(request,'core/update_mensalista.html',data)  


@login_required
def mensalista_delete(request,id):
    mensalista = Mensalista.objects.get(id=id)
    if request.method == 'POST':
        mensalista.delete()
        return redirect('core_lista_mensalistas')
    else:
        return render(request,'core/delete_confirm.html',{'obj':mensalista})


@login_required
def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    context = {'veiculos':veiculos,'form':form}
    return render(request,'core/lista_veiculos.html',context)


@login_required
def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


@login_required
def veiculo_update(request,id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    #Instancia o veiculo escolhido para o formulário
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request,'core/update_veiculo.html',data)


@login_required
def veiculo_delete(request,id):
    veiculo = Veiculo.objects.get(id=id)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request,'core/delete_confirm.html',{'obj':veiculo})


@login_required
def lista_mov_rot(request):
    mov_rot = MovimentoRot.objects.all()
    form = MovRotForm()
    context = {'movRot':mov_rot,'form':form}
    return render(request,'core/lista_mov_rot.html',context)


@login_required
def mov_rot_novo(request):
    form = MovRotForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mov_rot')


@login_required
def mov_rot_update(request,id):
    data = {}
    movRot = MovimentoRot.objects.get(id=id)
    form = MovRotForm(request.POST or None, instance=movRot)
    data['movRot'] = movRot
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mov_rot')
    else:
        return render(request,'core/update_mov_rot.html',data)


@login_required
def mov_rot_delete(request,id):
    movRot = MovimentoRot.objects.get(id=id)
    if request.method == 'POST':
        movRot.delete()
        return redirect('core_lista_mov_rot')
    else:
        return render(request,'core/delete_confirm.html',{'obj':movRot})


@login_required
def lista_mov_mens(request):
    mov_mens = MovimentoMens.objects.all()
    form = MovMensForm()
    context = {'movMens':mov_mens,'form':form}
    return render(request,'core/lista_mov_mens.html',context)


@login_required
def mov_mens_novo(request):
    form = MovMensForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mov_mens')


@login_required
def mov_mens_update(request,id):
    data = {}
    movMens = MovimentoMens.objects.get(id=id)
    form = MovMensForm(request.POST or None, instance=movMens)
    data['movMens'] = movMens
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mov_mens')
    else:
        return render(request,'core/update_mov_mens.html',data)


@login_required
def mov_mens_delete(request,id):
    movMens = MovimentoMens.objects.get(id=id)
    if request.method == 'POST':
        movMens.delete()
        return redirect('core_lista_mov_mens')
    else:
        return render(request,'core/delete_confirm.html',{'obj':movMens})