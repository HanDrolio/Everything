# house_hunt_soyla_gui.py
# 🧠 Myth.OS x Soyla GUI + CLI Zillow Simulation

import ipywidgets as widgets
from IPython.display import display, clear_output

# Simulated LLM response (Soyla AI)
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

# GUI elements
state_dropdown = widgets.Dropdown(
    options=["Texas", "Arizona"],
    value="Texas",
    description="State:"
)

max_price_input = widgets.IntText(value=300000, description="Max Price:")
min_beds_input = widgets.IntText(value=3, description="Min Beds:")
min_baths_input = widgets.IntText(value=2, description="Min Baths:")
search_button = widgets.Button(description="Search Homes")

output = widgets.Output()

def on_search_click(b):
    with output:
        clear_output()
        state = state_dropdown.value
        max_price = max_price_input.value
        min_beds = min_beds_input.value
        min_baths = min_baths_input.value
        print(f"🔍 Searching in {state}...")
        listings = simulated_llm_response(state, max_price, min_beds, min_baths)
        for listing in listings:
            print(f"🏡 {listing['address']} | 💲{listing['price']} | 🛏 {listing['beds']} | 🛁 {listing['baths']}")
            print(f"🔗 {listing['link']}\n")

search_button.on_click(on_search_click)

# Display GUI
display(state_dropdown, max_price_input, min_beds_input, min_baths_input, search_button, output)
