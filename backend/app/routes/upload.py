from fastapi import APIRouter, UploadFile, File
from app.services.ocr import extract_text
from app.services.parser import parse_report
from app.services.model1_interpreter import interpret_parameters
from app.services.model2_risk import assess_risk
from app.services.model3_context import contextual_analysis
from app.services.synthesizer import synthesize
from app.services.recommendations import generate_recommendations

router = APIRouter()

@router.post("/analyze")
async def analyze_report(file: UploadFile = File(...)):
    contents = await file.read()

    text = extract_text(contents)
    structured_data = parse_report(text)

    model1 = interpret_parameters(structured_data)
    model2 = assess_risk(structured_data)
    model3 = contextual_analysis(structured_data)

    summary = synthesize(model1, model2, model3)
    recommendations = generate_recommendations(summary)

    return {
        "data": structured_data,
        "analysis": summary,
        "recommendations": recommendations
    }
