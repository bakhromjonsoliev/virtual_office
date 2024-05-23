from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MurojaatForm
from .models import Murojaat

from django.core.serializers.json import DjangoJSONEncoder
import json

from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count
from django.shortcuts import render
from .models import Murojaat

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import MurojaatSerializer

@login_required
def submit_murojaat(request):
    if request.method == 'POST':
        form = MurojaatForm(request.POST)
        if form.is_valid():
            murojaat = form.save(commit=False)
            murojaat.user = request.user
            murojaat.save()
            return redirect('murojaat_status')
    else:
        form = MurojaatForm()
    return render(request, 'murojaats/submit_murojaat.html', {'form': form})

# @login_required
def murojaat_status(request):
    murojaats = Murojaat.objects.filter(user=request.user)
    return render(request, 'murojaats/murojaat_status.html', {'murojaats': murojaats})

# @staff_member_required
# def analytics(request):
#     murojaat_count = Murojaat.objects.count()
#     status_count = Murojaat.objects.values('status').annotate(total=Count('status'))
#     return render(request, 'murojaats/analytics.html', {
#         'murojaat_count': murojaat_count,
#         'status_count': status_count,
#     })

class MurojaatViewSet(viewsets.ModelViewSet):
    serializer_class = MurojaatSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Murojaat.objects.filter(user=self.request.user)

def murojaat_index(request):
    return render(request,'murojaats/index.html')

def murojaat_about(request):
    return render(request,'murojaats/about.html')

def murojaat_contact(request):
    if request.method == 'POST':
        form = MurojaatForm(request.POST)
        if form.is_valid():
            murojaat = form.save(commit=False)
            murojaat.user = request.user
            murojaat.save()
            return redirect('murojaat_statistika')
    else:
        form = MurojaatForm()
    return render(request, 'murojaats/contact.html', {'form': form})
    # return render(request,'murojaats/contact.html')

def murojaat_statistika(request):
    murojaat_count = Murojaat.objects.count()
    status_count = Murojaat.objects.values('status').annotate(total=Count('status'))
    return render(request, 'murojaats/course.html', {
        'murojaat_count': murojaat_count,
        'status_count': status_count,
    })
