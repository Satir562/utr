from django.shortcuts import render, redirect
from .models import Story
from .forms import StoryForm
from django.views.generic import DetailView, UpdateView, DeleteView

def catalog_home(request):
    story = Story.objects.order_by('-date_publisher')
    return render(request, 'my_catalog/catalog_main.html', {'story': story})


class StoryDetailView(DetailView):
    model = Story
    template_name = 'my_catalog/detailview.html'
    context_object_name = 'post'


class StoryUpdateView(UpdateView):
    model = Story
    template_name = 'my_catalog/create.html'
    form_class = StoryForm


class StoryDeleteView(DeleteView):
    model = Story
    success_url = '/catalog/'
    template_name = 'my_catalog/story-delete.html'




def create(request):
    error = ''
    if request.method == 'POST':
        form = StoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog_home')

        else:
            error = 'Форма заполнена не корректно!'

    form = StoryForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'my_catalog/create.html', data)