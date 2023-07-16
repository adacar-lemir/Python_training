# Two ways of running fastapi
    1. uvicornmain:app
    2. Add the following code lines:
        if __name__=="__main__":
            uvicorn.run("main:app,port=8000)

        And then run main.py
