from django.views.generic.base import TemplateView
from django.views.generic import ListView
from reviews.forms import ReviewForm
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from .models import ReviewModel


# Create your views here.


def index(request):
    # if request.method=="POST":
    #     print(request.POST['username'])
    #     if request.POST['username']=="":
    #         return render(request,"reviews/index.html",{
    #             "has_error":True
    #         })
    #     redirect_path=reverse("thanks")
    #     return HttpResponseRedirect(redirect_path)
    # return render(request,"reviews/index.html",{
    #     "has_error":False
    # })
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            redirect_path = reverse("thanks")
            return HttpResponseRedirect(redirect_path)
    else:
        form = ReviewForm()
    return render(request, "reviews/index.html", {
        "form": form
    })

class Index(View):
    def get(self,request):
        form = ReviewForm()
        return render(request, "reviews/index.html", {
            "form": form
        })

    def post(self,request):
        form = ReviewForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            redirect_path = reverse("thanks")
            return HttpResponseRedirect(redirect_path)


def thank_you(request):
    return render(request, "reviews/thank_you.html")

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

class AllReviewsView(TemplateView):
    template_name = "reviews/all_reviews.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews= ReviewModel.objects.all()
        context["reviews"] = reviews
        return context

class ReviewsListView(ListView):
    model = ReviewModel
    template_name = "reviews/all_reviews.html"
    context_object_name="reviews"
  

class ReviewView(TemplateView):
    template_name = "reviews/single_review.html"
    def get_context_data(self,id, **kwargs):
        print(id)
        context = super().get_context_data(**kwargs)
        review= ReviewModel.objects.get(pk=id)
        context["review"] = review
        return context