data = {
    "Declared_Income": [5, 8, 12, 15, 20, 50, 10],   # X-Axis
    "Luxury_Cars": [0, 1, 1, 2, 2, 5, 4],            # Y-Axis
    "Properties_Owned": [1, 1, 1, 2, 2, 4, 10],      # Z-Axis (The 3rd physical dimension)
    "data": [{
    "Declared_Income": [5, 8, 12, 15, 20, 50, 10],   # X-Axis
    "Luxury_Cars": [0, 1, 1, 2, 2, 5, 4],            # Y-Axis
    "Properties_Owned": [1, 1, 1, 2, 2, 4, 10],      # Z-Axis (The 3rd physical dimension)
    "Risk_Level": ["Safe", "Safe", "Safe", "Safe", "Monitor", "Safe", "CRITICAL FRAUD"]}]
}

# for ids in data['extra_data']:
# 	print(ids['Risk_Level'][-1])

data1 = data['data'][0]['Risk_Level'][-1]
print(data1)

