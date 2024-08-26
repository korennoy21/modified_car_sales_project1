
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Car, Seller, Buyer, Sale
from .forms import CarForm, SellerForm, BuyerForm, SaleForm

class CarListView(View):
    def get(self, request):
        cars = Car.objects.all()
        return render(request, 'catalog/car_list.html', {'cars': cars})

class CarDetailView(View):
    def get(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        return render(request, 'catalog/car_detail.html', {'car': car})

class CarCreateView(View):
    def get(self, request):
        form = CarForm()
        return render(request, 'catalog/car_form.html', {'form': form})

    def post(self, request):
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('car_list')
        return render(request, 'catalog/car_form.html', {'form': form})

class CarUpdateView(View):
    def get(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        form = CarForm(instance=car)
        return render(request, 'catalog/car_form.html', {'form': form})

    def post(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_detail', pk=car.pk)
        return render(request, 'catalog/car_form.html', {'form': form})

class CarDeleteView(View):
    def get(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        return render(request, 'catalog/car_confirm_delete.html', {'car': car})

    def post(self, request, pk):
        car = get_object_or_404(Car, pk=pk)
        car.delete()
        return redirect('car_list')
