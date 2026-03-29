from fastapi import APIRouter, UploadFile, File, HTTPException
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
        contents = await file.read()

        if not contents:
            raise HTTPException(status_code=400, detail="Empty file uploaded")

        text = extract_text(contents)

        if not text or len(text.strip()) == 0:
            raise HTTPException(status_code=400, detail="Could not extract text")

        structured_data = parse_report(text)

        if not structured_data:
            raise HTTPException(status_code=400, detail="Parsing failed")

        validated_data, validation_errors = validate_and_standardize(structured_data)

        model1 = interpret_parameters(validated_data, gender=gender or "male")
        model2 = assess_risk(validated_data)
        model3 = contextual_analysis(validated_data, age=age, gender=gender)

        summary = synthesize(model1, model2, model3)
        recommendations = generate_recommendations(summary)

        return {
            "status": "success",
            "data": validated_data,
            "errors": validation_errors,
            "analysis": summary,
            "recommendations": recommendations
        }

    except HTTPException as e:
        raise e

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
