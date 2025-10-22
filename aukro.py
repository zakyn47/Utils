import requests

def check_highest_bidder(offer_id, expected_bidder, currency="CZK"):
    """Checks if the highest bidder on a given auction offer matches the expected one."""
    url = f"https://aukro.cz/backend-web/api/offers/{offer_id}/offerDetail/short"
    headers = {"X-Accept-Currency": currency}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        bidder_login = data["highestBidderAnonymizedLogin"]
        if not bidder_login:
            print("Warning: No highest bidder information found.")
            return

        if bidder_login != expected_bidder:
            print(f"ALERT:>> someone overbid u <<:ALERT '{bidder_login}'")
        else:
            print(f"OK: Highest bidder = {expected_bidder}")

    except Exception as e:
        print(f"error: {e}")

check_highest_bidder(offer_id="7099446878", expected_bidder="t...8")
