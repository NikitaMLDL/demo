from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.db.models import Sum
from .form import *
# Create your views here.
def calc_discount(q):
    if q > 300000:
        d = 15
    elif q >= 50000:
        d = 10
    elif q >= 10000:
        d = 5
    else:
        d = 0
    return d

def partners_list(request):
    partners = Partners.objects.all()
    data = []
    for partner in partners:
        q = Sales.objects.filter(partnerid=partner).aggregate(total_sum=Sum('quantity'))['total_sum'] or 0
        data.append({'partner': partner, 'discount': calc_discount(q)})
    return render(request, 'list_partners.html', {'partners': data})

def add_partner(request):
    if request.method == 'POST':
        form = PartnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('partners_list')
    else:
        form = PartnerForm()
        return render(request, 'form.html', {'form': form, 'mode': 'Добавление'})

def edit_partner(request, partnerid):
    partner = get_object_or_404(Partners, partnerid=partnerid)
    if request.method == 'POST':
        form = PartnerForm(request.POST, instance=partner)
        if form.is_valid():
            form.save()
            return redirect('partners_list')
    else:
        form = PartnerForm(instance=partner)
        return render(request, 'form.html', {'form': form, 'mode': 'Изменение'})

def history_partner(request, partnerid):
    partner = get_object_or_404(Partners, partnerid=partnerid)
    sales = Sales.objects.filter(partnerid=partner).select_related('productid')
    return render(request, 'history.html', {'partner': partner, 'sales': sales})