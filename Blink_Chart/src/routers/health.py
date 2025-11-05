from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.get("/version")
def version_check():  
    return {"version": "1.0.0"} 
