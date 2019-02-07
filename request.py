import requests

API = "https://dolar.melizeche.com/api/1.0/"
# make a request
response = requests.get(API).json()
type(response)
precio_venta = response["dolarpy"]["bcp"]["venta"]
toyota_corolla=21300
print("precio en dolares:", toyota_corolla )

print("precio en guaranies:", int(toyota_corolla*precio_venta ))