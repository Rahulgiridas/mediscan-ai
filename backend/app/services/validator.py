from app.utils.constants import REALISTIC_LIMITS


def validate_and_standardize(data: dict):
    cleaned = {}
    errors = []

    for key, value in data.items():

        # ❌ Missing value
        if value is None:
            errors.append(f"{key} missing")
            continue

        # ❌ Invalid type
        if not isinstance(value, (int, float)):
            errors.append(f"{key} invalid type")
            continue

        # ❌ Negative values
        if value < 0:
            errors.append(f"{key} has negative value")
            continue

        # ⚠️ Out-of-range check
        if key in REALISTIC_LIMITS:
            low, high = REALISTIC_LIMITS[key]
            if not (low <= value <= high):
                errors.append(f"{key} out of realistic range ({value})")

        # 🔄 Unit normalization
        if key == "platelets" and value < 1000:
            value = value * 1000  # convert to standard count

        cleaned[key] = value

    return cleaned, errors
