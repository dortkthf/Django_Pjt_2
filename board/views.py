from django.shortcuts import render
from .models import Review
# Create your views here.
def index(request):
    review = Review.objects.order_by('-pk')
    context = {
        'review' : review,
    }
    return render(request,'board/index.html',context)