from django.shortcuts import render, redirect
from django.db.models import Avg, Max
from django.contrib import messages
from .models import Book, BookReviews
from ..mylogin.models import Users
# Create your views here.

def index(request):
    clearmessages = messages.get_messages(request)
    for message in clearmessages:
        print 'message cleared'
    del clearmessages
    context = {}
    allbooks = Book.objects.all().order_by('-id')
    bookcount = allbooks.count()
    if bookcount < 3:
        context['recentbooks'] = allbooks
        context['otherbooks'] = []
    else:
        context['recentbooks'] = allbooks[:3]
        context['otherbooks'] = allbooks[3:]
    return render(request, 'booksapp/index.html', context)

def addbook(request):
    return render(request, 'booksapp/addbook.html')

def createbook(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        review = request.POST['review']
        stars = request.POST['stars']
        targetbook = Book.objects.create(title=title,author=author)
        print targetbook
        user = Users.objects.get(id=request.session['userid'])
        print user
        targetreview = BookReviews.objects.create(FK_userid=user, FK_book=targetbook, review=review, stars=stars)
        print targetreview
        return redirect('/books')
    return redirect('/booksapp/addbook')

def bookreviews(request, bookid):
    targetbook = Book.objects.get(id=bookid)
    print targetbook
    return render(request, 'booksapp/bookreviews.html')

def addreview(request, booksid):
    if request.method == 'POST':
        returnaddress = '/booksapp/booksreviews/'+str(booksid)
        return redirect(returnaddress)
    
def displayallbooks(request):
    context = {}
    allbooks = Book.objects.all().order_by('-id')
    context['allbooks'] = allbooks
    return render(request, 'booksapp/displayallbooks.html', context)