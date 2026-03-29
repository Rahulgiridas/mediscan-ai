from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import Optional

# 🔧 Services
from app.services.ocr import extract_text
from app.services.parser import parse_report
from app.services.validator import validate_and_standardize
from app.services.model1_interpreter import interpret_parameters
from app.services.model2_risk import assess_risk
from app.services.model3_context import contextual_analysis
from app.services.synthesizer import synthesize
from app.services.recommendations import generate_recommendations

# 🚀 Router
router = APIRouter(prefix="/api", tags=["Analysis"])


@router.post("/analyze")
async def analyze_report(
    file: UploadFile = File(...),
    age: Optional[int] = None,
    gender: Optional[str] = None
):
    try:
        # 📥 Read file
        contents = await file.read()

        if not contents:
            raise HTTPException(status_code=400, detail="Empty file uploaded")

        # 🔍 OCR
        text = extract_text(contents)

        if not text or len(text.strip()) == 0:
            raise HTTPException(status_code=400, detail="Could not extract text from report")

        # 🧾 Parse
        structured_data = parse_report(text)

        if not structured_data:
            raise HTTPException(status_code=400, detail="Failed to parse report data")

        # 🧪 Validate
        validated_data, validation_errors = validate_and_standardize(structured_data)

        # 🧠 Model 1
        model1_results = interpret_parameters(validated_data, gender=gender or "male")

        # ⚠️ Model 2
        model2_results = assess_risk(validated_data)

        # 🧠 Model 3
        model3_results = contextual_analysis(validated_data, age=age, gender=gender)

        # 🧩 Combine
        summary = synthesize(model1_results, model2_results, model3_results)

        # 💡 Recommendations
        recommendations = generate_recommendations(summary)

        # ✅ Response
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
