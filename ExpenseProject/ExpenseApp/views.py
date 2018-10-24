from django.shortcuts import render, get_object_or_404, redirect
from .models import ExpenseModel, TransactionModel
from .forms import ExpenseForm, UserForm, TransactionForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def index(request):
    form_list = ExpenseModel.objects.all()
    context = {'form_list': form_list}
    return render(request, 'ExpenseApp/index.html', context)


@login_required
def userindex(request):
    form_list = ExpenseModel.objects.filter(username=request.user)
    print(form_list)
    context = {'form_list': form_list,}
    return render(request, 'ExpenseApp/index.html', context)


def userindex_Transaction(request):
    form_list = ExpenseModel.objects.filter(username=request.user)
    history
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
    return render(request, 'ExpenseApp/detail.html', {'post': post})


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





