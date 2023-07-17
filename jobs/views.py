from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView
from django.db.models import Q



class JobsDetailView(DetailView):
    model = Articles
    template_name = 'jobs/detail.html'
    context_object_name = 'article'


def jobs(request):
    jobs = Articles.objects.order_by('-data')
    return render(request, 'jobs/jobs.html', {'jobs': jobs})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobs')
        else:
            error = 'Fill Forms correctly'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'jobs/create.html', data)

def search(request):
    search_term = ""
    results = []

    if request.method == 'POST':
        search_term = request.POST['search']
        results = Articles.objects.filter(title__icontains=search_term)
        return render(request, 'jobs/search.html', {'search': search_term, 'results': results})
    else:
        return render(request, 'jobs/search.html')