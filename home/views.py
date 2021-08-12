from django.shortcuts import render

# Create your views here.


def index(request):
    """ 
    * A view to return the index page.
    ! asdasd
    ? render home/index.html page
    TODO turn into a view?    
    """

    return render(request, 'home/index.html')
