from django.shortcuts import redirect, render
from .models import CurrentBalance, TrackingHistory


def index(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = float(request.POST.get('amount'))
        
        current_balance, _ = CurrentBalance.objects.get_or_create(id=1)
        expense_type ='CREDIT'

        if float(amount) < 0:
            current_balance.current_balance += amount
            expense_type = 'DEBIT'

        tracking_history = TrackingHistory.objects.create(
            current_balance = current_balance ,
            amount = amount,
            expense_type= expense_type,
            description = description)
        
        current_balance.current_balance += amount

        current_balance.save()
        return redirect('/')
    return render(request, 'index.html')






