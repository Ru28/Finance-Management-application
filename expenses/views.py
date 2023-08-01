from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .forms import CreateExpenseForm
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import CreateExpenseForm,SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate 

def login_view(request):
    # Implement your login logic here
    # You can use Django's built-in authentication views or a third-party package for login functionality.  
    if request.method == 'POST':

        #AuthenticationForm_can_also_be_used__

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request,user)
            messages.success(request, f' wecome {username} !!')
            return redirect('view_expenses')
        else:
            messages.info(request, f'account does not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form,'title':'log in'})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request,"Registration successful.")
            return redirect('view_expenses')
        messages.error(request,"Unsuccessful registration. Invalid information")
    form=SignUpForm()
    return render(request, 'signup.html', {'form': form})

def logout_request(request):

	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("signup_view")

@login_required
def create_expense(request):
    if request.method == 'POST':
        form = CreateExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.created_by = request.user
            expense.save()
            messages.success(request, 'Expense created successfully!')
            return redirect('view_expenses')
        else:
            messages.error(request, 'Expense create request failed.')
    else:
        form = CreateExpenseForm()
    return render(request, 'create_expense.html', {'form': form})


@login_required
def view_expenses(request):
    if request.user.is_superuser:
        expenses = Expense.objects.all()
    else:
        expenses = Expense.objects.filter(created_by=request.user)
    return render(request, 'view_expenses.html', {'expenses': expenses})


@login_required
def update_expense(request, expense_id):
    if request.user.is_superuser:
        expense=get_object_or_404(Expense,id=expense_id)
    else:
        expense = get_object_or_404(Expense, id=expense_id, created_by=request.user)
    if request.method == 'POST':
        form = CreateExpenseForm(request.POST or None, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('view_expenses')
    else:
        form = CreateExpenseForm(instance=expense)
    return render(request, 'edit_expense.html', {'form': form, 'expense': expense})


@login_required
def delete_expense(request, expense_id):
    if request.user.is_superuser:
        expense=get_object_or_404(Expense,id=expense_id)
    else:
        expense = get_object_or_404(Expense, id=expense_id, created_by=request.user )
    if request.method == 'POST':
        expense.delete()
        return redirect('view_expenses')
    return render(request, 'delete_expense.html', {'expense': expense})