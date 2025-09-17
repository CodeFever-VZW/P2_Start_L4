from fastapi import FastAPI

# Run je code door in de terminal dit te typen: uvicorn 0_main:app --reload
# Surf dan in je browser naar http://127.0.0.1:8000/
# Je kan ook documentatie zien voor je api op http://127.0.0.1:8000/docs

# Maak een API-robot
app = FastAPI()

# Als iemand de startpagina opent, zegt onze robot "Welkom!"
@app.get("/")
def startpagina():
    return {"bericht": "Welkom bij mijn API!"}