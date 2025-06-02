# pip install fastapi uvicorn

from fastapi import FastAPI

app = FastAPI()


indian_places = {
    'delhi': ['red fort', 'india gate', 'qutub minar'],
    'mumbai': ['gateway of india', 'marine drive', 'elephanta caves'],
    'jaipur': ['hawa mahal', 'amer fort', 'city palace'],
    'varanasi': ['ghats', 'kashi vishwanath temple', 'sarnath'],
    'goa': ['beaches', 'basilica of bom jesus', 'fort aguada'],
}


@app.get('/get_items/{place}')
async def root(place):
    return indian_places.get(place)

