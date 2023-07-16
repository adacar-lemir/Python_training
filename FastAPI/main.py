from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/welcome")
def welcome():
    return("Welcome")

@app.post("/withParam")
def withParam(user):
    print(user)
    return True

if __name__=="__main__":
    uvicorn.run("main:app", port=8000, reload=True)
