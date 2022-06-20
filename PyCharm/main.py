import fastapi
import uvicorn

app = FastAPI()


@app.get('/')
def index():
    x = {
        "Name": 'Vignesh',
        "DOB": "26-05-2002",
        "Blood Group": "O+ve"
    }

    return x
