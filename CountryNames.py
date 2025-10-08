import requests
import os
import re

APIurl = "https://restcountries.com/v3.1/all?fields=cca2,unMember,name"

os.chdir("CountryNamesAutomation/CountryImages")

cca2Country = dict()

try:
    response = requests.get(APIurl, timeout=10)
    response.raise_for_status() # in case the response is an error

    responseData = response.json()

    for countryData in responseData:
        countryName = countryData.get("name").get("common")
        countryCca2 = countryData.get("cca2").lower()

        isUnMember = countryData.get("unMember")

        if isUnMember:
            cca2Country[countryCca2] = countryName
    
    #### #### #### #### #### #### ### ## ### #### #### ### ## ### ### # # #### ## ### ### ## ### ### ## ### ### ### ## ## 

    # Now we go through each file name in the current directory, and see if it matches any in thecca2Country dictionary

    for fileName in os.listdir():
        trueFileName = fileName.split(".")

        cca2Code = trueFileName[0]
        fileExtension = trueFileName[1]

        if cca2Country.get(cca2Code):
            os.rename(fileName, cca2Country.get(cca2Code)+"."+fileExtension)
        else:
            os.remove(fileName)

except Exception:
    print("uh oh!")