from django.shortcuts import render, redirect, get_object_or_404
from .forms import MurojaatForm
from .models import Murojaat
from django.db.models import Count

from django.core.serializers.json import DjangoJSONEncoder
import json

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import MurojaatSerializer
from django.utils import timezone
from datetime import timedelta


def murojaat_status(request):
    murojaats = Murojaat.objects.filter(user=request.user)
    return render(request, 'murojaats/murojaat_status.html', {'murojaats': murojaats})

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
        form = MurojaatForm(request.POST, request.FILES)
        if form.is_valid():
            murojaat = form.save(commit=False)
            murojaat.save()
            return redirect('murojaat_statistika_id', id=murojaat.id)
        else:
            print('Form is not valid:', form.errors)
    else:
        form = MurojaatForm()
    return render(request, 'murojaats/contact.html', {'form': form})


def murojaat_statistika(request, id=None):
    murojaat_count = Murojaat.objects.count()
    status_count = list(Murojaat.objects.values('status').annotate(total=Count('status')))
    murojaat_turi_count = list(Murojaat.objects.values('murojaat_turi').annotate(total=Count('murojaat_turi')))

    now = timezone.now()
    one_week_ago = now - timedelta(days=7)

    accepted_last_week = list(Murojaat.objects.filter(
        # status='accepted',
        created_at__gte=one_week_ago
    ).values('murojaat_turi').annotate(total=Count('murojaat_turi')))

    hudud_count = list(Murojaat.objects.values('hudud').annotate(total=Count('hudud')))

    status_count_json = json.dumps(status_count, cls=DjangoJSONEncoder)
    murojaat_turi_count_json = json.dumps(murojaat_turi_count, cls=DjangoJSONEncoder)
    accepted_last_week_json = json.dumps(accepted_last_week, cls=DjangoJSONEncoder)
    hudud_count_json = json.dumps(hudud_count, cls=DjangoJSONEncoder)

    murojaat = None
    status = None

    if id:
        murojaat = get_object_or_404(Murojaat, id=id)
        status = murojaat.get_status_display()

    return render(request, 'murojaats/course.html', {
        'murojaat_count': murojaat_count,
        'status_count': status_count,
        'status_count_json': status_count_json,
        'murojaat_turi_count': murojaat_turi_count,
        'murojaat_turi_count_json': murojaat_turi_count_json,
        'accepted_last_week': accepted_last_week,
        'accepted_last_week_json': accepted_last_week_json,
        'hudud_count': hudud_count,
        'hudud_count_json': hudud_count_json,
        'murojaat_id': id,
        'status': status,
    })

def check_status(request):
    id = request.GET.get('id')
    murojaat = None
    status = None
    answer = None
    error_message = None

    if id:
        try:
            murojaat = Murojaat.objects.get(id=id)
            status = murojaat.get_status_display()
            answer = murojaat.answer
        except Murojaat.DoesNotExist:
            error_message = "Mavjud bo'lmagan raqam"

    return render(request, 'murojaats/check_status.html', {
        'murojaat_id': id,
        'status': status,
        'answer': answer,
        'error_message': error_message,
    })