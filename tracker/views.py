from django.shortcuts import get_object_or_404, redirect, render
from .models import CurrentBalance, TrackingHistory
# from django.db.models import Sum
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = float(request.POST.get('amount'))
        
        current_balance, _ = CurrentBalance.objects.get_or_create(id=1)
        expense_type ='CREDIT'

        if float(amount) < 0:
            expense_type = 'DEBIT'

        if float(amount) ==0:
            messages.success(request, "Amount cannot be zero")
            return redirect('/')

        tracking_history = TrackingHistory.objects.create(
            current_balance = current_balance ,
            amount = amount,
            expense_type= expense_type,
            description = description)
        
        current_balance.current_balance = current_balance.current_balance + amount

        current_balance.save()
        return redirect('/')
    current_balance, _ = CurrentBalance.objects.get_or_create(id=1)
    income =0
    expense = 0

    for tracking_history in TrackingHistory.objects.all():
        if tracking_history.expense_type == "CREDIT":
            income += tracking_history.amount
        else:
            expense += tracking_history.amount  


    context = {'income':income, 'expense':expense, 'transactions': TrackingHistory.objects.all(), 'current_balance': current_balance}
    return render(request, 'index.html', context)


def delete_transaction(request, id):
    tracking_history = TrackingHistory.objects.filter(id=id)

    if tracking_history.exists():
      current_balance, _ = CurrentBalance.objects.get_or_create(id=1)
      tracking_history = get_object_or_404(TrackingHistory, id=id)
      current_balance.current_balance = current_balance.current_balance - tracking_history.amount
      current_balance.save() 
      
      

    tracking_history.delete()
    return redirect('/')
    





