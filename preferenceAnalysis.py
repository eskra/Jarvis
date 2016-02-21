import json
import urllib.request


TRIPADVISOR_KEY= "E985153E657E44DB94018B68469080F5"

def TravelAnalysis(Object,APIKEY,command):

    if command=="trip" or command=="nice" or command=="suprise":

        TravelLocation=Object["travel"][0]

        searchurl="https://api.tripadvisor.com/api/partner/2.0/search/"+TravelLocation+"?key="+TRIPADVISOR_KEY+"&category=hotels"

        response = urllib.request.urlopen(searchurl)


        responsestring = response.read().decode('utf-8')
        json_obj = json.loads(responsestring)

        Address = json_obj["hotels"][0]["address_obj"]["street1"]
        City=json_obj["hotels"][0]["address_obj"]["city"]
        HotelName=json_obj["hotels"][0]["name"]
        StringStatement="What about "+HotelName+"at "+Address+" "+City;
        return (StringStatement,True)

    else:
        return ("Could you please repeat that?",False)


def RestaurantAnalysis(userObj,Foodtype,APIKEY):

   Location="Montreal"

   searchurl="https://api.tripadvisor.com/api/partner/2.0/search/"+Foodtype+" "+Location+"?key="+TRIPADVISOR_KEY+"&category=hotels"

   response = urllib.request.urlopen(searchurl)

   responsestring = response.read().decode('utf-8')
   json_obj = json.loads(responsestring)

   Address=json_obj["restaurants"][0]["address_obj"]["street1"]
   Restaurant=json_obj["restaurants"][0]["name"]

   return ("How about "+Restaurant+" at "+Address+" in "+"Montreal")