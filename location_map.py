# backend/flask-api/location_map.py

location_mapping = {
    "Delhi": 0,
    "Mumbai": 1,
    "Kolkata": 2,
    "Chennai": 3,
    # ... fill in all used during training
}

reverse_mapping = {v: k for k, v in location_mapping.items()}
crime_type_map = {
    0: "For Adoption",
    1: "For Camel racing",
    2: "For Illicit intercourse",
    3: "For Prostitution",
    4: "For marriage",
    5: "For Ransom",
    6: "For Revenge",
    7: "Others",
    8: "For Sale",
    9: "For Selling body parts"
}
