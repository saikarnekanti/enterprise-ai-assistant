from fastapi import FastAPI
app=FastAPI(title="Enterprise AI Assistant") #this creates our application#
@app.get("/health") #get means we are asking the server to give us information about the health of server #
def health_check(): # healtcheck is a function that performs the task #
    return {
        "status":"healthy",
        "service":"Enterprise AI Assistant"
    }



