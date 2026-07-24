print("=" * 45)
print("   SOUTH AFRICAN FUEL COST CALCULATOR   ")
print("=" * 45)

# 1. Ask the user for inputs (handling typed 'R' symbols gracefully)
distance_km = float(input("Enter distance to drive (in kilometers): "))

petrol_input = input("Enter current petrol price per liter (e.g. 26.10): ")
# Strips 'R' or spaces if the user types them (e.g. "R26.10" -> "26.10")
petrol_price = float(petrol_input.upper().replace("R", "").strip())

# 2. Formula: Assume 1L for every 10 km driven
liters_needed = distance_km / 10

# 3. Calculate total cost
total_cost = round(liters_needed * petrol_price, 2)

# 4. Output results
print("\n" + "=" * 45)
print(f"Distance:      {distance_km} km")
print(f"Fuel Needed:   {round(liters_needed, 2)} L")
print(f"Total Cost:    R{total_cost:.2f}")
print("=" * 45)