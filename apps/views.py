from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio


# def say_hello(request):
#     return HttpResponse("Hi How are you man !")

# rooms = [
#     {'id': 1, 'name': 'Lets learn python!'},
#     {'id': 2, 'name': 'Design with me'},
#     {'id': 3, 'name': 'Frontend developers'},
# ]

# context = {
#      "data": [1, 2, 3, 4, 5, 6, 7, 8,],
# }
    #context = Portfolio.objects.filter(description='Artificial Intelligence and Machine Learning')
    #context = Portfolio.objects.exclude(description='Machine')
    #context = Portfolio.objects.order_by('description')
    #context = Portfolio.objects.order_by('?')
    #context = Portfolio.objects.order_by('description', 'date')
    #context = Portfolio.objects.reverse()[0:2]
    #context = Portfolio.objects.all().values()
    #context = Portfolio.objects.order_by('id').reverse()
    #context = Portfolio.objects.values()
    #context = Portfolio.objects.values('name', 'description')
    #context = Portfolio.objects.values_list('id', 'name', named=True)
    #context = Portfolio.objects.using('default')
# Create your views here.
def home(request, check):
    return render(request, 'enroll/home.html', {'ch':check})


# def show(request, my_id):
#     student = {'id':my_id}
#     return render(request, 'enroll/show.html', student)#{'id':my_id}

def show(request, my_id=1):
    if my_id == 1:
        student = {'id':my_id, 'name':'Hridoy'}
    if my_id == 2:
        student = {'id':my_id, 'name':'Rahial'}
    if my_id == 3:
        student = {'id':my_id, 'name':'Noble'}

    return render(request, 'enroll/show.html', student)


def show_subdetail(request, my_id, my_subid):
    if my_id == 1 and my_subid == 5:
        student = {'id':my_id, 'name':'Hridoy', 'info':'sub detail'}
    if my_id == 2 and my_subid == 6:
        student = {'id':my_id, 'name':'Rahial', 'info':'Web developers'}
    if my_id == 3 and my_subid == 7:
        student = {'id':my_id, 'name':'Noble', 'info':'Python django'}

    return render(request, 'enroll/show.html', student)
