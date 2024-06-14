from django.shortcuts import render
import requests
import datetime

def HomePage(request):

    if 'city' in request.POST:
        city = request.POST['city']

    else:
        city = 'Surat'
        

    APID = 	"23b13ccd851a8d0d83fbc512055340fa"
    URL = "https://api.openweathermap.org/data/2.5/weather"
    PARAMS = {'q':city,'appid':APID,'units':'Metric'}
    r = requests.get(url=URL , params=PARAMS)
    res  = r.json()
    # description = res['weather'][0]['description']
    # icon = res['weather'][0]['icon']
    # main = res['weather'][0]['main']
    temp = res['main']['temp']
    humidity = res['main']['humidity']
    wind = res['wind']['speed']
    
    day = datetime.date.today()
   

    return render(request,'index.html',{'temp':temp,'day':day,'city':city,'humidity':humidity, 'wind':wind})



