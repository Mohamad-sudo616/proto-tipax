from django.views.generic.edit import FormView
from django.shortcuts import render
from .forms import TrackingForm
from .models import Package

class TrackPackageView(FormView):
    template_name = 'tracking/track.html'
    form_class = TrackingForm

    def form_valid(self, form):
        code = form.cleaned_data['tracking_code']
        package = None
        not_found = False

        try:
            package = Package.objects.prefetch_related('events').get(tracking_code__iexact=code)
        except Package.DoesNotExist:
            not_found = True

        # Pass the results to the template
        return self.render_to_response(self.get_context_data(
            form=form,
            package=package,
            not_found=not_found
        ))
