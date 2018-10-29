from django.shortcuts import render, get_object_or_404, redirect
from .models import ExpenseModel, TransactionModel, UserSetup
from .forms import ExpenseForm, UserForm, DepositForm, WithdrawForm
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    form_list = ExpenseModel.objects.all()
    context = {'form_list': form_list}
    return render(request, 'ExpenseApp/index.html', context)


@login_required
def userindex(request):
    form_list = ExpenseModel.objects.filter(username=request.user)
    # post = get_object_or_404(TransactionModel, pk=pk)
    context = {'form_list': form_list, }
    return render(request, 'ExpenseApp/index.html', context)


def createUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            User.objects.create_user(request.POST.get("first_name"), request.POST.get("email"),
                                     request.POST.get("password"), )
            form.save()
            return redirect('userindex')
    else:
        form = UserForm()
        return render(request, 'ExpenseApp/createUser.html', {'form': form})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(ExpenseModel, pk=pk)
    transactions = (post.transactionmodel_set.all())
    context = {'post': post, 'transactions': transactions}
    return render(request, 'ExpenseApp/detail.html', context)

@login_required
def edit(request, pk):
    the_model = get_object_or_404(ExpenseModel, pk=pk)
    form = ExpenseForm(request.POST, instance=the_model)
    if form.is_valid():
        form.save()
        return redirect("userindex")
    else:
        the_model = get_object_or_404(ExpenseModel, pk=pk)
        form = ExpenseForm(instance=the_model)
    return render(request, 'ExpenseApp/input.html', {'form': form})

@login_required
def deposit(request, pk):
    the_model = get_object_or_404(ExpenseModel, pk=pk)

    if request.method == "POST":

        deposit_amt = float(request.POST['trans_value'])
        checking_acc = request.POST['trans_check']

        # UPDATE THE RUNNING BALANCE

        if checking_acc != 'SAVINGS':
            deposit_amt: float = deposit_amt
            the_model.current_balance += deposit_amt
        if checking_acc == 'SAVINGS':
            deposit_amt: float = deposit_amt
            the_model.emergency_fund += deposit_amt
        else:
            print("it worked")

        the_model.save()

        # NOW UPDATE TRANSACTION HISTORY

        setValue = TransactionModel(id=None, deposits=deposit_amt, withdraws=0, date_Submittd=datetime.now(), expenseFK=the_model)
        setValue.save()
        return redirect('userindex')
    else:
        print('THE WARP cookie')
    return render(request, 'ExpenseApp/deposit.html')

@login_required
def withdraw(request, pk):
    the_model = get_object_or_404(ExpenseModel, pk=pk)

    if request.method == "POST":

        withdraw_amt = float(request.POST['trans_value'])
        checking_acc = request.POST['trans_check']

        # UPDATE THE RUNNING BALANCE

        if checking_acc != 'SAVINGS':
            withdraw_amt: float = withdraw_amt
            the_model.current_balance -= withdraw_amt
        if checking_acc == 'SAVINGS':
            withdraw_amt: float = withdraw_amt
            the_model.emergency_fund -= withdraw_amt
        else:
            print("it worked")

        the_model.save()

        # NOW UPDATE TRANSACTION HISTORY

        setValue = TransactionModel(id=None, deposits=0, withdraws=withdraw_amt, date_Submittd=datetime.now(), expenseFK=the_model)
        setValue.save()
        return redirect('userindex')
    else:
        print('THE WARP cookie')
    return render(request, 'ExpenseApp/withdraw.html')


def edit_Account(request, pk):
    the_model = get_object_or_404(UserSetup, pk=pk)
    form = UserForm(request.POST, instance=the_model)
    if form.is_valid():
        form.save()
        return redirect("userindex")
    else:
        the_model = get_object_or_404(UserSetup, pk=pk)
        form = UserForm(instance=the_model)
    return render(request, 'ExpenseApp/input.html', {'form': form})


def post_new(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.username = request.user
            newpost.save()
            return redirect('userindex')
    else:
        form = ExpenseForm()
    return render(request,'ExpenseApp/new.html', {'form': form})