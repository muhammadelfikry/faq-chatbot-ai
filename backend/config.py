from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    # Frontend origin for CORS
    FRONTEND_ORIGIN = os.getenv("PRODUCTION_ORIGIN") or os.getenv("DEVELOPMENT_ORIGIN")

    # Groq API configuration
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GROQ_MODEL = os.getenv("GROQ_MODEL")
    
    @classmethod
    def validate(cls):
        missing_vars = []
        
        if not cls.FRONTEND_ORIGIN:
            missing_vars.append("FRONTEND_ORIGIN")
        
        if not cls.GROQ_API_KEY:
            missing_vars.append("GROQ_API_KEY")

        if not cls.GROQ_MODEL:
            missing_vars.append("GROQ_MODEL")

        if missing_vars:
            raise ValueError(f"Missing environment variables: {', '.join(missing_vars)}")