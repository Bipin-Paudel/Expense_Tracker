from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        print(description)
        return redirect('/')

    return render(request, 'index.html')
