# from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import Http404, HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

challenges_map={
    "january":"Drink more water",
    "february":"Brush your teeth twice a day",
    "march":"Eat an extra serve of vegetables each day",
    "april":"Ban added sugar",
    "may":"Eat home-cooked meals",
    "june":"10,000 steps every day",
    # "july":"Get 8 hours sleep",
    "july":None,
    "august":"Take the stairs (up and down)",
    "september":"Read every day",
    "october":"Follow a productivity system",
    "november":"Set 3 priorities each day and achieve them",
    "december":"Learn to meditate"
}

def jan(request):
    return HttpResponse("This is January")


def feb(request):
    return HttpResponse("This is February")

def home(request):
    html_list_tag=""
    month_list=list(challenges_map.keys())
    # for month in month_list:
    #     redirect_path=reverse("monthly_challenges",args=[month])
    #     html_list_tag+=f"<li><a href=\"{redirect_path}\">{month.capitalize()}</li>"
    # response_data=f"<ul>{html_list_tag}</ul>"
    # return HttpResponse(response_data)
    return render(request,"challenges_list/index.html",{
        "months":month_list
    })

def monthly_challenges_by_number(request,month):
    print(month)
    month_list=list(challenges_map.keys())
    if len(month_list)<month:
        return HttpResponseNotFound("This is not a valid month")
    corresponding_month=month_list[month-1]
    redirect_path=reverse("monthly_challenges",args=[corresponding_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenges(request,month):
    try:
        responseText=challenges_map[month]
        # return HttpResponse(responseText)
        # return HttpResponse(render_to_string("challenges_list/challenge.html"))
        return render(request,"challenges_list/challenge.html",{
            "challenge":responseText,
            "month_name":month
        })
    except:
        raise Http404
        # responseData=render_to_string("404.html")
        # return HttpResponseNotFound(responseData)