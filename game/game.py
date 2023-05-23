import requests

with open('api-data-url.txt','r') as file:
    api_data_url = file.read()
API = requests.get(api_data_url)

hi = API.json()['Messages']['hi']
print(hi)


name = input("what is your name ")
print(f"hi {name}")
q = int(input("what is 1+1="))

if(q == 2):
    print("yes")

if not(q == 2):
    print("no")

