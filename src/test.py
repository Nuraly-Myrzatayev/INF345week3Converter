import requests
import os

passedTests = 0
amountOfTests = 3
#Ending is the postfix after the url
#What i'm trying to get here is just the python equivalent of
#curl 0.0.0.0:(port:8080)/ending
def getRequestText(ending):
    return requests.get(f"http://127.0.0.1:{os.environ.get("PORT", "8080")}{ending}").text
    

if getRequestText("/") == "Celsius to Fahrenheit converter":
    passedTests += 1
if getRequestText("/healthz") == "ok":
    passedTests += 1
if "celsius is" in getRequestText("/converter"):
    passedTests += 1

print(f"TESTS: {passedTests}/{amountOfTests}")
