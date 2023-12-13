from django.shortcuts import render, HttpResponse
import requests
import datetime


def home(request):
    city = "Hyderabad"

    if request.method == "POST":
        city = request.POST.get("city", "Hyderabad")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d5ca3789784a8a6c693bd593535bbbe3"
    PARAMS = {"units": "metric"}
    response = requests.get(url, params=PARAMS)
    data = response.json()

    # Check if the 'main' key exists in the response
    if "main" in data:
        temp = data["main"]["temp"]
    else:
        temp = "N/A"

    description = data.get("weather", [{}])[0].get("description", "N/A")
    icon = data.get("weather", [{}])[0].get("icon", "N/A")
    day = datetime.date.today()

    return render(
        request,
        "index.html",
        {
            "description": description,
            "icon": icon,
            "temp": temp,
            "day": day,
            "city": city,
        },
    )
