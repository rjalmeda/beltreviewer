from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Users
from ..booksapp.models import Book, BookReviews

# Create your views here.
def index(request):
    if 'userid' in request.session:
        print 'already logged in'
        return redirect('/books')
    return render(request, 'mylogin/index.html')

def success(request):
    context = {}
    user = Users.objects.get(id=request.session['userid'])
    context['user'] = user
    return render(request, 'mylogin/success.html', context)

def displayall(request):
    context = {}
    allusers = Users.objects.all()
    print allusers
    context['allusers'] = allusers
    return render(request, 'mylogin/displayall.html', context)

def displayuser(request, targetid):
    context = {}
    targetuser = Users.objects.get(id=targetid)
    context['targetuser'] = targetuser
#    targetbooks = BookReviews.objects.filter(FK_userid=targetid)
#    context['targetbooks'] = targetbooks
    return render(request, 'mylogin/displayuser.html', context)

def register(request):
    if request.method == 'POST':
        print 'Posted'
        res = Users.objects.register(request.POST)
        if res['success']:
            user = Users.objects.get(email=request.POST['email'])
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            request.session['userid'] = user.id
            request.session['email'] = user.email
            for message in res['success']:
                messages.add_message(request, messages.SUCCESS, message)
            return redirect('/success')
        else:
            for message in res['errors']:
                messages.add_message(request, messages.ERROR, message)
            return redirect('/')
    else:
        return redirect('/')

def login(request):
    if request.method == 'POST':
        res = Users.objects.login(request.POST)
        if res['success']:
            user = Users.objects.get(email=request.POST['email'])
            print user
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            request.session['userid'] = user.id
            request.session['email'] = user.email
            for message in res['success']:
                messages.add_message(request, messages.SUCCESS, message)
            return redirect('/success')
        else:
            for message in res['errors']:
                messages.add_message(request, messages.ERROR, message)
            return redirect('/')
    else:
        return redirect('/')
    
def logout(request):
    request.session.clear()
    request.session.flush()
    return redirect('/login')
    
def delete(request, deleteid):
    print deleteid
    user = Users.objects.get(id=deleteid)
    print user
    user.delete()
    return redirect('/displayall')
    