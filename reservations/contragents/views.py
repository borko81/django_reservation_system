from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


from . import forms
from . import models


@login_required
def menu(request):
    context = {"title": "Menu"}
    return render(request, template_name="contragents/base.html", context=context)


@login_required
def contragents(request):
    contragents = models.FirmModel.objects.all().order_by('-is_active')
    
    query_parameter = request.GET.get('show')
    if query_parameter:
        contragents = models.FirmModel.objects.filter(is_active=request.GET.get('show'))

        
    context = {"title": "Contragents", "contragents": contragents, "owner_class": "active"}
    return render(request, template_name="contragents/show_all.html", context=context)


@login_required
def create(request):
    form = forms.ContragentForm(request.POST or None )
    context = {"title": "Create", "form": form, "form_create_class": "active"}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('contragent:menu')
    return render(request, template_name="contragents/create.html", context=context)


@login_required
def edit(request, id):
    contract = get_object_or_404(models.FirmModel, id=id)
    form = forms.ContragentForm(request.POST or None, instance=contract or None )
    context = {"title": "Edit", "contract": contract, 'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('contragent:menu')
    return render(request, template_name="contragents/create.html", context=context)

