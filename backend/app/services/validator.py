def validate_and_standardize(data):
    cleaned = {}
    errors = []

    # Standard reference ranges (can move to constants.py later)
    ranges = {
        "hemoglobin": (5, 25),      # g/dL realistic bounds
        "rbc": (1, 10),             # million cells
        "wbc": (1000, 20000),       # cells
        "platelets": (10000, 1000000)
    }

    for key, value in data.items():

        # ❌ Missing or invalid
        if value is None:
            errors.append(f"{key} missing")
            continue

        # ❌ Negative values
        if value < 0:
            errors.append(f"{key} has negative value")
            continue

        # ⚠️ Out-of-range (possible OCR error)
        if key in ranges:
            low, high = ranges[key]
            if not (low <= value <= high):
                errors.append(f"{key} out of realistic range ({value})")

        # ✅ Normalize (example: platelets in lakhs → convert)
        if key == "platelets" and value < 1000:
            value = value * 1000  # convert to standard unit

        cleaned[key] = value

    return cleaned, errors
