import requests

def main():
    res = requests.get(f"http://data.fixer.io/latest?access_key=b1d838edcf954525e53384e43f3b10b0")
    if res.status_code != 200:
        raise Exception("Error: harsh API request unsuccessfull")
    data = res.json()

    one = input("Enter First Cureency: ")
    two = input("Enter Second Currency: ")

    first = data['rates'][one.upper()]
    sec = data['rates'][two.upper()]
    
    sec /=first

    print(f"1 {one} is {sec} two")

if __name__ == "__main__":
    main()