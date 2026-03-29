from fastapi import APIRouter, UploadFile, File
from app.services.ocr import extract_text
from app.services.parser import parse_report
from app.services.model1_interpreter import interpret_parameters
from app.services.model2_risk import assess_risk
from app.services.model3_context import contextual_analysis
from app.services.synthesizer import synthesize
from app.services.recommendations import generate_recommendations
from app.services.validator import validate_and_standardize

router = APIRouter()

@router.post("/analyze")
async def analyze_report(file: UploadFile = File(...)):
    contents = await file.read()

upload.py, line 17
text = extract_text(contents)from fastapi import APIRouter...
from typing import Optional

from app.services.ocr import extract_text
from app.services.parser import parse_report
from app.services.validator import validate_and_standardize
from app.services.model1_interpreter import interpret_parameters
from app.services.model2_risk import assess_risk
from app.services.model3_context import contextual_analysis
from app.services.synthesizer import synthesize
from app.services.recommendations import generate_recommendations

router = APIRouter(prefix="/api", tags=["Analysis"])


@router.post("/analyze")
async def analyze_report(
    file: UploadFile = File(...),
    age: Optional[int] = None,
    gender: Optional[str] = None
):
    try:
        # 📥 Step 1 — Read file
        contents = await file.read()

        if not contents:
            raise HTTPException(status_code=400, detail="Empty file uploaded")

        # 🔍 Step 2 — OCR Extraction
        text = extract_text(contents)

        if not text or len(text.strip()) == 0:
            raise HTTPException(status_code=400, detail="Could not extract text from report")

        # 🧾 Step 3 — Parse Report
        structured_data = parse_report(text)

        if not structured_data:
            raise HTTPException(status_code=400, detail="Failed to parse report data")

        # 🧪 Step 4 — Validation & Standardization
        validated_data, validation_errors = validate_and_standardize(structured_data)

        # 🧠 Step 5 — Model 1 (Parameter Interpretation)
        model1_results = interpret_parameters(validated_data)

        # ⚠️ Step 6 — Model 2 (Risk Assessment)
        model2_results = assess_risk(validated_data)

        # 🧠 Step 7 — Model 3 (Contextual Analysis)
        model3_results = contextual_analysis(validated_data, age=age, gender=gender)

        # 🧩 Step 8 — Synthesis
        summary = synthesize(model1_results, model2_results, model3_results)

        # 💡 Step 9 — Recommendations
        recommendations = generate_recommendations(summary)

        # ✅ Final Response
        return {
            "status": "success",
            "filename": file.filename,
            "validated_data": validated_data,
            "validation_errors": validation_errors,
            "analysis": summary,
            "recommendations": recommendations
        }

    except HTTPException as http_err:
        raise http_err

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )
    structured_data = parse_report(text)

    model1 = interpret_parameters(structured_data)
    model2 = assess_risk(structured_data)
    model3 = contextual_analysis(structured_data)

    summary = synthesize(model1, model2, model3)
    recommendations = generate_recommendations(summary)

    return {
        "data": structured_data,
        "validation_errors": validation_errors,
        "analysis": summary,
        "recommendations": recommendations
    }
