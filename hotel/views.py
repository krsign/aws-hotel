from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from .models import Room, Category
from .forms import ContactUsForm

class CategoryList(View):

    def get(self, request, id=None):
        posts = Room.objects.all()
        if id:
            cat = Category.objects.get(id=id)
            rooms = Room.objects.filter(category = cat)
            return render(request, 'hotel/list.html',context={'rooms':rooms, 'categories':Category.objects.all()})
        categories = Category.objects.all()
        context = {'rooms':rooms, 'categories':categories}
        return render(request, 'hotel/list.html',context )
        

class HomeView(ListView):
    model = Room
    context_object_name = 'rooms'
    template_name = 'hotel/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context

    def get(self, request, id=None):
        rooms = Room.objects.all()
        if id:
            category = Category.objects.get(id=id)
            rooms = Room.objects.filter(category=category)
            return render(request, 'hotel/list.html', context={'rooms':rooms, 'categories':Category.objects.all()})
        categories = Category.objects.all()
        context = {'rooms':rooms, 'categories':categories}
        return render(request, 'hotel/list.html', context)


def customer_detail_form(request):
    if request.method == 'GET':
        form = ContactUsForm()
        return render(request, 'hotel/checkout.html', context={'form':form})
        
    else:
        print(request.POST)
        form = ContactUsForm(request.POST)
        if form.is_valid():
            return render(request, 'hotel/thankyou.html')
        else:
            print(form.errors)
            return render(request, 'hotel/checkout.html', context={'form':form})

class About(TemplateView):
    template_name = 'hotel/about.html'