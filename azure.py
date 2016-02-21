import urllib2
# If you are using Python 3+, import urllib instead of urllib2

import json 
import ast

def recommendMusic():

  data =  {

          "Inputs": {

                  "input1":
                  {
                      "ColumnNames": ["rock", "jazz", "pop", "metal", "classical", "country", "folk", "genre"],
                      "Values": [ [ "0", "0", "0", "0", "0", "0", "0", "value" ], [ "0", "0", "0", "0", "0", "0", "0", "value" ], ]
                  },        },
              "GlobalParameters": {
  }
      }

  body = str.encode(json.dumps(data))

  url = 'https://ussouthcentral.services.azureml.net/workspaces/077c4b47af9645da91235dfe53ee81c7/services/d0c6924ceb834a72ae320ce038319ea0/execute?api-version=2.0&details=true'
  api_key = '5fztg0GIUsGILZbbsKRZLpRJjmJiobh9vJPHP3o+di9BJVjW/iHQKTKOsSsMt1E3S24vIcI26plm6DSokmxtlQ==' # Replace this with the API key for the web service
  headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

  req = urllib2.Request(url, body, headers) 

  try:
      response = urllib2.urlopen(req)

      # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
      # req = urllib.request.Request(url, body, headers) 
      # response = urllib.request.urlopen(req)

      result = response.read()
      temp =  ast.literal_eval(result)
      return temp['Results']['output1']['value']['Values'][0][-1]
  except urllib2.HTTPError, error:
      print("The request failed with status code: " + str(error.code))

      # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
      print(error.info())

      print(json.loads(error.read()))   