def interpret_parameters(data):
    results = {}

    if "hemoglobin" in data:
        hb = data["hemoglobin"]
        if hb < 12:
            results["hemoglobin"] = "Low"
        elif hb > 17:
            results["hemoglobin"] = "High"
        else:
            results["hemoglobin"] = "Normal"

    if "platelets" in data:
        p = data["platelets"]
        if p < 150000:
            results["platelets"] = "Low"
        elif p > 410000:
            results["platelets"] = "High"
        else:
            results["platelets"] = "Normal"

    return results
