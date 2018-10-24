from django.shortcuts import render, get_object_or_404, redirect
from .models import ExpenseModel, TransactionModel
from .forms import ExpenseForm, UserForm, DepositForm, WithdrawForm
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
    context = {'form_list': form_list,}
    return render(request, 'ExpenseApp/index.html', context)


def createUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            User.objects.create_user(request.POST.get("first_name"), request.POST.get("email"), request.POST.get("password"), )
            return redirect('index')
    else:
        form = UserForm()
        return render(request, 'ExpenseApp/createUser.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(ExpenseModel, pk=pk)
    transactions = (post.transactionmodel_set.all())
    context = {'post': post, 'transactions':transactions}
    return render(request, 'ExpenseApp/detail.html', context)


def edit(request, pk):
    the_model = get_object_or_404(ExpenseModel, pk=pk)
    form = ExpenseForm(request.POST, instance=the_model)
    print(form.is_valid())
    if form.is_valid():
        print("edit test")
        form.save()
        return redirect("userindex")
    else:
        the_model = get_object_or_404(ExpenseModel, pk=pk)
        form = ExpenseForm(instance=the_model)
    return render(request, 'ExpenseApp/input.html', {'form': form})


def deposit(request, pk):
    # the_model = get_object_or_404(TransactionModel, pk=pk)
    the_model2 = get_object_or_404(ExpenseModel, pk=pk)
    # form = DepositForm(request.POST, instance=the_model)
    # form2 = ExpenseForm(request.POST, instance=the_model2)
    # print("Forms printing")
    # print(form)
    # print("2")
    # print(form2)
    if request.method == "POST":
        print("Kenn's Hello")
        form2 = ExpenseForm(request.POST, instance=the_model2)
        print(form2.is_valid())
        if form2.is_valid():
            # form.save()
            new_deposit = form2.save(False)
            new_deposit.save()
            print("hello")
            return redirect("userindex")
    else:
        # # the_model = get_object_or_404(TransactionModel, pk=pk)
        # the_model2 = get_object_or_404(ExpenseModel, pk=pk)
        print("good bye")
        # form = DepositForm(instance=the_model)
        form2 = ExpenseForm(instance=the_model2)
    return render(request, 'ExpenseApp/deposit.html', {'form2': form2})


def withdraw(request, pk):
    the_model = get_object_or_404(ExpenseModel, pk=pk)
    form = ExpenseForm(request.POST, instance=the_model)
    if form.is_valid():
        form.save()
        return redirect("userindex")
    else:
        the_model = get_object_or_404(ExpenseModel, pk=pk)
        form = ExpenseForm(instance=the_model)
    return render(request, 'ExpenseApp/input.html', {'form': form})
