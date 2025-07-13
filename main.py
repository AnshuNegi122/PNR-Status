import requests

url = "https://irctc-indian-railway-pnr-status.p.rapidapi.com/getPNRStatus/2335631036"

headers = {
    "X-RapidAPI-Key": "47aac8b746msh5c680def67275dfp1c2f42jsn019db75d486b",  # Replace with your actual RapidAPI key
    "X-RapidAPI-Host": "irctc-indian-railway-pnr-status.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
data = response.json()

if data.get("success"):
    pnr_data = data["data"]
    print("PNR Number:", pnr_data["pnrNumber"])
    print("Train:", pnr_data["trainNumber"], "-", pnr_data["trainName"])
    print("From:", pnr_data["boardingPoint"], "→ To:", pnr_data["destinationStation"])
    print("Journey Class:", pnr_data["journeyClass"])
    print("Chart Status:", pnr_data["chartStatus"])
    print("--------------------------------------------------")
    print("Passenger Statuses:")
    for passenger in pnr_data["passengerList"]:
        print(f" Passenger {passenger['passengerSerialNumber']}:")
        print("  Booking Status :", passenger["bookingStatusDetails"])
        print("  Current Status :", passenger["currentStatusDetails"])
        print()
else:
    print("Error:", data.get("message"))
