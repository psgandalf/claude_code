from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Home page demonstrating the modern stack."""
    return render(request, 'core/index.html')


def htmx_demo(request):
    """HTMX demo endpoint."""
    if request.method == 'POST':
        name = request.POST.get('name', 'World')
        return HttpResponse(f'<p class="text-green-600 font-semibold">Hello, {name}! 👋</p>')
    return HttpResponse('<p class="text-red-600">Invalid request</p>')
