from app.utils.constants import REFERENCE_RANGES


def interpret_parameters(data: dict, gender: str = "male"):
    results = {}

    # 🩸 Hemoglobin (gender-specific)
    if "hemoglobin" in data:
        hb = data["hemoglobin"]
        ref = REFERENCE_RANGES["hemoglobin"].get(gender, (12, 16))

        if hb < ref[0]:
            results["hemoglobin"] = "Low"
        elif hb > ref[1]:
            results["hemoglobin"] = "High"
        else:
            results["hemoglobin"] = "Normal"

    # 🧬 RBC
    if "rbc" in data:
        rbc = data["rbc"]
        low, high = REFERENCE_RANGES["rbc"]

        if rbc < low:
            results["rbc"] = "Low"
        elif rbc > high:
            results["rbc"] = "High"
        else:
            results["rbc"] = "Normal"

    # 🧪 WBC
    if "wbc" in data:
        wbc = data["wbc"]
        low, high = REFERENCE_RANGES["wbc"]

        if wbc < low:
            results["wbc"] = "Low"
        elif wbc > high:
            results["wbc"] = "High"
        else:
            results["wbc"] = "Normal"

    # 🧩 Platelets
    if "platelets" in data:
        p = data["platelets"]
        low, high = REFERENCE_RANGES["platelets"]

        if p < low:
            results["platelets"] = "Low"
        elif p > high:
            results["platelets"] = "High"
        else:
            results["platelets"] = "Normal"

    return results
