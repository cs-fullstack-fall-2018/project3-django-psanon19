from django.shortcuts import render, get_object_or_404, redirect
from .models import ExpenseModel, TransactionModel
from .forms import ExpenseForm, UserForm, DepositForm, WithdrawForm
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def index(request):
    form_list = ExpenseModel.objects.all()
    context = {'form_list': form_list}
    return render(request, 'ExpenseApp/index.html', context)


@login_required
def userindex(request):
    form_list = ExpenseModel.objects.filter(username=request.user)
    # post = get_object_or_404(TransactionModel, pk=pk)
    print(form_list)
    context = {'form_list': form_list, }
    return render(request, 'ExpenseApp/index.html', context)


def createUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            User.objects.create_user(request.POST.get("first_name"), request.POST.get("email"),
                                     request.POST.get("password"), )
            return redirect('index')
    else:
        form = UserForm()
        return render(request, 'ExpenseApp/createUser.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(ExpenseModel, pk=pk)
    transactions = (post.transactionmodel_set.all())
    context = {'post': post, 'transactions': transactions}
    return render(request, 'ExpenseApp/detail.html', context)


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


def deposit(request, pk):
    the_model = get_object_or_404(ExpenseModel, pk=pk)
    print("first cookie")
    if request.method == "POST":
        print("second cookie")
        print(request.POST['trans_value'])
        deposit_amt = float(request.POST['trans_value'])

        # UPDATE THE RUNNING BALANCE
        deposit_amt: float = deposit_amt
        the_model.current_balance += deposit_amt

        the_model.save()
        print("ALL FOR COOKIE")
        # NOW UPDATE TRANSACTION HISTORY
        print(the_model)
        thist = TransactionModel(id=None, deposits=deposit_amt, withdraws=0, date_Submittd=datetime.now(), expenseFK=the_model)
        thist.save()
        return redirect('userindex')
    else:
        print('THE WARP cookie')
    return render(request, 'ExpenseApp/deposit.html')


def withdraw(request, pk):
    the_model = get_object_or_404(ExpenseModel, pk=pk)
    print("first cookie")
    if request.method == "POST":
        print("second cookie")
        print(request.POST['trans_value'])
        withdraw_amt = float(request.POST['trans_value'])

        # UPDATE THE RUNNING BALANCE
        withdraw_amt: float = withdraw_amt
        the_model.current_balance -= withdraw_amt

        the_model.save()
        print("ALL FOR COOKIE")
        # NOW UPDATE TRANSACTION HISTORY
        print(the_model)
        thist = TransactionModel(id=None, deposits=0, withdraws=withdraw_amt, date_Submittd=datetime.now(), expenseFK=the_model)
        thist.save()
        return redirect('userindex')
    else:
        print('THE WARP cookie')
    return render(request, 'ExpenseApp/withdraw.html')
