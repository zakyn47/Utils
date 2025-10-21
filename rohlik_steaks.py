import requests
from bs4 import BeautifulSoup
import re

URL = "https://www.rohlik.cz/zachran-a-usetri/c300103000-maso-a-ryby"

def parse_discount(text):
    match = re.search(r"-(\d+)\s*%", text)
    return int(match.group(1))

def find_discounted_steaks(min_discount=25):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(URL, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    steak_pattern = re.compile(r"(steak|rib\s*eye|rump|hovězí)", re.IGNORECASE)

    results = []
    for a in soup.find_all("a", href=True):
        text = " ".join(filter(None, [
            a.get("aria-label", ""),
            a.get_text(strip=True)
        ]))
        if steak_pattern.search(text):
            discount = parse_discount(text)
            if discount >= min_discount:
                name_match = re.search(r"([A-ZÁČĎÉĚÍŇÓŘŠŤÚŮÝŽa-záčďéěíňóřšťúůýž0-9!.,\- ]+)", text)
                name = name_match.group(1).strip()
                price_match = re.search(r"(\d+,\d+)\s*Kč", text)
                price = price_match.group(1) + " Kč" if price_match else "N/A"
                url = "https://www.rohlik.cz" + a["href"]
                results.append((name, f"-{discount} %", price, url))

    seen = set()
    unique = []
    for r in results:
        if r[3] not in seen:
            seen.add(r[3])
            unique.append(r)
    return unique

if __name__ == "__main__":
    steaks = find_discounted_steaks()
    print(f"Found {len(steaks)} discounted steaks:\n")
    for name, discount, price, url in steaks:
        print(f"{name} — {price} ({discount})")
        print(f"{url}\n")
