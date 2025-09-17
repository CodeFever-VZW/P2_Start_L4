from fastapi import FastAPI, Body

# Run je code door in de terminal dit te typen: uvicorn 2_emoji_vertaler:app --reload
# Surf dan in je browser naar http://127.0.0.1:8000/translate
# Je kan ook documentatie zien voor je api op http://127.0.0.1:8000/docs

emoji_map = {
    "i": "I",
    "love": "❤️",
    "pizza": "🍕",
    "cat": "🐱",
    "dog": "🐶",
    "school": "🏫",
    "happy": "😊",
    "sad": "😢",
    "fire": "🔥",
    "cool": "😎",
    "party": "🎉",
    "hate": "💔",
    "python": "🐍",
    "coding": "💻",
    "fever": "🤒",
    "code": "👨‍💻",
    "codefever": "👨‍💻🤒"
}
