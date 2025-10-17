# tracking/views.py
from django.shortcuts import render
from .forms import TrackingForm
from .models import Package

def track_package(request):
    form = TrackingForm(request.GET or None)
    package = None
    not_found = False

    if form.is_valid():
        code = form.cleaned_data['tracking_code']
        try:
            package = Package.objects.prefetch_related('events').get(tracking_code__iexact=code)
        except Package.DoesNotExist:
            not_found = True

    context = {
        'form': form,
        'package': package,
        'not_found': not_found,
    }
    return render(request, 'tracking/track.html', context)
