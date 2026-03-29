import re

def parse_report(text):
    data = {}

    patterns = {
        "hemoglobin": r"Hemoglobin.*?(\d+\.?\d*)",
        "rbc": r"RBC.*?(\d+\.?\d*)",
        "wbc": r"WBC.*?(\d+)",
        "platelets": r"Platelet.*?(\d+)"
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            data[key] = float(match.group(1))

    return data
