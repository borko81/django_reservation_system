from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def menu_index(request):
    context = {
        "title": "Floor menu",
        "menu_class": "active"
    }
    return render(request, template_name='floors/base.html', context=context)






