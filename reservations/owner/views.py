from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from . import models
from . import forms


@login_required
def owner_index(request):

    context = {
        "title": "owner",
        "menu_class": "active",
    }
    return render(request, template_name="owner/base.html", context=context)


def owner_create_update(request):
    try:
        instance = models.OwnerModel.objects.get(id=1)
    except:
        form = forms.OwnerDataForm(request.POST or None, request.FILES or None)
    else:
        form = forms.OwnerDataForm(request.POST or None, request.FILES or None, instance=instance or None)

    context = {"title": "Owner Data", "owner_class": "active", "form": form}
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('owner:owner')
    
    return render(request, template_name="owner/owner_data.html", context=context)


def owner_bank_create_update(request):
    context = {
        "title": "Owner Bank",
        "bank_class": "active",
    }
    return render(request, template_name="owner/owner_bank.html", context=context)


def owner_fak_id_update(request):
    context = {"title": "Owner Fak Id", "fak_class": "active"}
    return render(request, template_name="owner/owner_fak_id.html", context=context)
