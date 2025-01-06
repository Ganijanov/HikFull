# B.R.R
from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from main.models import Income, Expense, PayHis, Pupil

class BudgetView(View):
    @method_decorator(login_required)
    def get(self, request):
        incomes = Income.objects.all()
        expenses = Expense.objects.all()
        pays = PayHis.objects.all()
        total_income = sum(income.amount for income in incomes)
        total_expense = sum(expense.amount for expense in expenses)
        total_pays = sum(pay.summa for pay in pays)
        balance = total_income + total_pays - total_expense
        total_pupil = Pupil.objects.all()

        context = {
            'incomes': incomes,
            'expenses': expenses,
            'total_income': total_income,
            'total_expense': total_expense,
            'balance': balance,
            'pupil' : total_pupil.count()
        }
        return render(request, 'budget/budget_summary.html', context)


class AddIncomeView(View):
    @method_decorator(login_required)
    def get(self, request):
        
        return render(request, 'budget/add_income.html', {'pupils': Pupil.objects.all()})

    @method_decorator(login_required)
    def post(self, request):
        title = request.POST.get('title')
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        status = True if request.POST.get('status') is not None else False
        Income.objects.create(title=title, amount=amount, description=description, status=status)
        return redirect('budget_summary')


class AddExpenseView(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'budget/add_expense.html')

    @method_decorator(login_required)
    def post(self, request):
        title = request.POST.get('title')
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        status = True if request.POST.get('status') is not None else False


        Expense.objects.create(title=title, amount=amount, description=description, status=status)
        return redirect('budget_summary')


class PaymentHistoryView(View):
    @method_decorator(login_required)
    def get(self, request):
        payments = PayHis.objects.all()
        context = {
            'payments': payments
        }
        return render(request, 'budget/payment_history.html', context)


class AddPaymentView(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'budget/add_payment.html')

    @method_decorator(login_required)
    def post(self, request):
        parent_id = request.POST.get('parent_id')
        pupil_id = request.POST.get('pupil_id')
        summa = request.POST.get('summa')
        paymon = request.POST.get('paymon')
        salesum = request.POST.get('salesum')
        aboutsale = request.POST.get('aboutsale')
        status = True if request.POST.get('status') is not None else False
        
        PayHis.objects.create(
            payer=parent_id,
            pupil_id=pupil_id,
            summa=summa,
            paymon=paymon,
            salesum=salesum,
            aboutsale=aboutsale,
            status=status
        )
        return redirect('payment_history')