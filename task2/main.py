from fastapi import FastAPI


app = FastAPI()


@app.get("/calculate")
def calculate(feets: float = 0):
    if feets < 0:
        return {"error": "feets cannot be less than 0."}

    inches = feets * 12
    yards = feets / 3
    miles = feets / 5280

    return {"result": f"{feets} футів дорівнює: {inches} дюймів; {yards} ярдів; {miles} миль."}