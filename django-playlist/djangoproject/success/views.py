from django.shortcuts import render

def confirm_view(request):
    return render(request, 'success/confirm.html')
# Create your views here.
