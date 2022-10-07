from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

# Create your views here.
def index(request):
    review = Review.objects.order_by("-pk")
    context = {
        "review": review,
    }
    return render(request, "board/index.html", context)


def create(request):

    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect("board:index")
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form,
    }

    return render(request, "board/create.html", context=context)


def detail(request, pk):

    review = Review.objects.get(pk=pk)

    context = {
        "review": review,
    }

    return render(request, "board/detail.html", context)


def delete(request, pk):

    review = Review.objects.get(pk=pk)

    review.delete()

    return redirect("board:index")
