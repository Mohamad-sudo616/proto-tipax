from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PackageForm

@login_required
def send_package(request):
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            package = form.save(commit=False)
            package.sender = request.user
            package.save()
            messages.success(request, 'بسته شما با موفقیت ثبت شد!')
            return redirect('send_package')
            tracking_code = package.tracking_code 
    else:
        form = PackageForm()

    return render(request, 'send_package.html', {'form': form})
