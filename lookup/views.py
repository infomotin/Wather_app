from django.shortcuts import render
import json
import requests


# Create your views here.
def home(request):

    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=D58CEED4-3471-41C0-8F18-73012733C6BF")
    # http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=D58CEED4-3471-41C0-8F18-73012733C6BF
   # print(api_request.status_code)
    # api = json.load(api_request)
    # print(api)
   # print((api_request.content))
    #wine api Key = "PQ6vkMk4UEyza7XXdaAwhht7q1dtW4wD"

    try:
        api = json.loads(api_request.content)
        #print(api)
    except Exception as error:
        api = 'Error ----'
    context = {
        'api': api,
    }

    return render(request, 'lookup/home.html', context)


def about(request):
    return render(request, 'lookup/about.html')
