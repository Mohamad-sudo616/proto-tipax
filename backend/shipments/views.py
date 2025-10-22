from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Package
from .forms import PackageForm


class SendPackageView(LoginRequiredMixin, CreateView):
    model = Package
    form_class = PackageForm
    template_name = 'send_package.html'
    success_url = reverse_lazy('send_package')

    def form_valid(self, form):
        package = form.save(commit=False)
        package.sender = self.request.user
        package.save()

        # Render same page showing tracking code
        return render(
            self.request,
            self.template_name,
            {
                'form': self.form_class(),  # empty new form
                'tracking_code': package.tracking_code,  # show tracking code
            }
        )
