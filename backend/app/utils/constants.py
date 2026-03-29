# ================================
# 📊 Standard Reference Ranges
# ================================

REFERENCE_RANGES = {
    "hemoglobin": {
        "male": (13.0, 17.0),
        "female": (12.0, 15.0)
    },
    "rbc": (4.5, 5.5),          # million cells / µL
    "wbc": (4000, 11000),       # cells / µL
    "platelets": (150000, 410000)
}


# ================================
# ⚠️ Realistic Bounds (Validation)
# ================================

REALISTIC_LIMITS = {
    "hemoglobin": (5, 25),
    "rbc": (1, 10),
    "wbc": (1000, 20000),
    "platelets": (10000, 1000000)
}


# ================================
# 🧠 Risk Rules (Model 2)
# ================================

RISK_RULES = {
    "anemia": {
        "condition": lambda data: data.get("hemoglobin", 15) < 12,
        "message": "Possible Anemia"
    },
    "low_platelets": {
        "condition": lambda data: data.get("platelets", 200000) < 150000,
        "message": "Low Platelet Risk"
    }
}


# ================================
# 💡 Recommendations Map
# ================================

RECOMMENDATIONS_MAP = {
    "Possible Anemia": [
        "Increase iron-rich foods (spinach, dates, red meat)",
        "Consider iron supplements (consult doctor)",
        "Get ferritin test"
    ],
    "Low Platelet Risk": [
        "Avoid alcohol",
        "Eat vitamin B12 and folate-rich foods",
        "Consult a healthcare provider"
    ]
}


# ================================
# 🧾 Supported File Types
# ================================

ALLOWED_FILE_TYPES = [
    "image/jpeg",
    "image/png",
    "application/pdf"
]


# ================================
# ⚙️ OCR Settings
# ================================

OCR_CONFIG = {
    "lang": "eng",
    "config": "--psm 6"
}
