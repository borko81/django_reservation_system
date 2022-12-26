"""
All view use show and edint only. Not allowed del.
All instance is almost same. Maybe use func for refactor.
"""


from django.shortcuts import render, redirect
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
        instance = models.OwnerModel.objects.all().last()
    except:
        form = forms.OwnerDataForm(request.POST or None, request.FILES or None)
    else:
        form = forms.OwnerDataForm(
            request.POST or None, request.FILES or None, instance=instance or None
        )

    context = {"title": "Owner Data", "owner_class": "active", "form": form}

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("owner:owner")

    return render(request, template_name="owner/owner_data.html", context=context)


@login_required
def owner_bank_create_update(request):

    try:
        instance = models.OwnerBank.objects.all().last()
    except:
        form = forms.OwnerBankForm(request.POST or None)
    else:
        form = forms.OwnerBankForm(request.POST or None, instance=instance or None)

    context = {"title": "Owner Bank", "bank_class": "active", "form": form}

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("owner:owner")

    return render(request, template_name="owner/owner_bank.html", context=context)


@login_required
def owner_fak_id_update(request):
    try:
        instance = models.OwnerLastFakIdModel.objects.all().last()
    except:
        form = forms.OwnerLastFakIdForm(request.POST or None)
    else:
        form = forms.OwnerLastFakIdForm(request.POST or None, instance=instance or None)

    context = {"title": "Fak Number", "fak_class": "active", "form": form}

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("owner:owner")

    return render(request, template_name="owner/owner_fak_id.html", context=context)
