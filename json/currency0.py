import requests

def main():
    res = requests.get(f"http://data.fixer.io/latest?access_key=b1d838edcf954525e53384e43f3b10b0")
    if res.status_code != 200:
        raise Exception("Error: harsh API request unsuccessfull")
    data = res.json()
    rupees = data['rates']['INR']
    usd = data['rates']['USD']
    ou = usd/rupees
    print(f"1 rupee is {ou} dollars")

if __name__ == "__main__":
    main()