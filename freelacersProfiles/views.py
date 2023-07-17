from django.shortcuts import render, redirect
from .models import Freelancer
from .forms import FreelancerForm

def freelancer_list(request):
    freelancers = Freelancer.objects.all()
    return render(request, 'profiles/freelancer_list.html', {'freelancers': freelancers})



def freelancer_create(request):
    if request.method == 'POST':
        form = FreelancerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FreelancerForm()
    return render(request, 'profiles/freelancer_create.html', {'form': form})

