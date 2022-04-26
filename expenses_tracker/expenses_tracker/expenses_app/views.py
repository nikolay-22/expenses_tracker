from django.shortcuts import render, redirect

# Create your views here.
from expenses_tracker.expenses_app.forms import ProfileForm, ExpenseForm, DeleteExpenseForm
from expenses_tracker.expenses_app.models import Profile, Expense

def money_left():
    expenses = Expense.objects.all()
    budget = Profile.objects.all().first().budget
    if expenses:
        for expense in expenses:
            budget -= expense.price
        return budget

def index(request):
    person = Profile.objects.all().first()
    if request.method == 'GET':
        if person:
            expenses = Expense.objects.all()
            #if expenses:
            budget_left = money_left()
            context = {
                'person': person,
                'expenses': expenses,
                'budget_left': budget_left,
            }
            return render(request, 'home-with-profile.html', context)
            # else:
            #     context = {
            #         'person': person,
            #     }
            #     return render(request, 'home-with-profile.html', context)

        else:
            return render(request, 'home-no-profile.html')
    else:
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            expenses = Expense.objects.all().first()
            if not expenses:
                return render(request, 'home-with-profile.html')
            else:
                context = {
                    'expenses': expenses
                }
                return render(request, 'home-with-profile.html', context)


def profile(request):
    person = Profile.objects.all().first()
    budget_left = money_left()
    if request.method == 'GET':
        if person:
            context = {
                'person': person,
                'budget_left': budget_left
            }
            return render(request, 'profile.html', context)


# def edit_profile(request, pk):
#     person = Profile.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=person)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#         else:
#             context = {
#                 'form': form
#             }
#             return render(request, 'profile-edit.html', context)
#     else:
#         form = ProfileForm(initial=person.__dict__)
#         # form = ProfileForm(instance=person)
#         context = {
#             'form': form,
#         }
#         return render(request, 'profile-edit.html', context)
def edit_profile(request):
    person = Profile.objects.all().first()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=person)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context = {
                'form': form
            }
            return render(request, 'profile-edit.html', context)
    else:
        form = ProfileForm(initial=person.__dict__)
        # form = ProfileForm(instance=person)
        context = {
            'form': form,
        }
        return render(request, 'profile-edit.html', context)


def delete_profile(request):
    person = Profile.objects.all().first()
    if request.method == 'POST':
        # expenses = Expense.objects.all()
        # if expenses:
        #     for expense in expenses:
        #         expense.delete()
        ## A better way to delete the expenses:
        Expense.objects.all().delete()
        person.delete()
        return redirect('index')
    else:
        return render(request, 'profile-delete.html')


def create_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context = {
                'form': form
            }
            return render(request, 'expense-create.html', context)
    else:
        form = ExpenseForm()
        context = {
            'form': form
        }
        return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context = {
                'form': form
            }
            return render(request, 'expense-create.html', context)
    else:
        form = ExpenseForm(initial=expense.__dict__)
        context = {
            'form': form,
        }
        return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('index')
    else:
        expense = DeleteExpenseForm(initial=expense.__dict__)
        context = {
            'expense': expense,
        }
        return render(request, 'expense-delete.html', context)
