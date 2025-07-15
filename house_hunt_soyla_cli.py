# house_hunt_soyla_cli.py
# 🧠 Soyla CLI House Hunter | Han Drolo CLI Mode

def simulated_llm_response(state, max_price, min_beds, min_baths):
    return [
        {
            "address": "123 Dream Ln, Austin, TX",
            "price": 275000,
            "beds": 3,
            "baths": 2,
            "link": "https://zillow.com/fake-listing1"
        },
        {
            "address": "456 Desert Rd, Tucson, AZ",
            "price": 290000,
            "beds": 4,
            "baths": 3,
            "link": "https://zillow.com/fake-listing2"
        }
    ]

def main():
    print("🧠 Soyla House Hunter (CLI Edition)")
    state = input("🌎 State (Texas/Arizona): ").strip()
    max_price = int(input("💲 Max Price: ").strip())
    min_beds = int(input("🛏  Min Beds: ").strip())
    min_baths = int(input("🛁  Min Baths: ").strip())

    print(f"🔍 Searching homes in {state} under ${max_price} with at least {min_beds} beds / {min_baths} baths...
")

    results = simulated_llm_response(state, max_price, min_beds, min_baths)
    for r in results:
        if r["price"] <= max_price and r["beds"] >= min_beds and r["baths"] >= min_baths:
            print(f"🏡 {r['address']} | 💲{r['price']} | 🛏 {r['beds']} | 🛁 {r['baths']}")
            print(f"🔗 {r['link']}
")

if __name__ == "__main__":
    main()
