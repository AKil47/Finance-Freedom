from fastapi import FastAPI
from pydantic import BaseModel

from typing import Optional, List

from fastapi.middleware.cors import CORSMiddleware

from signals import signals as signals

class StockSignal(BaseModel):
    signal: str
    weight: int

# Define types
class StockSignals(BaseModel):
    signals: List[StockSignal]

app = FastAPI()


#Testing Git so I'm adding an extra comment :)
#Enabled CORS!
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/test")
async def root():
    return {"Hello": "World"}

@app.post("/stock/{stock_id}")
async def get_stock_score(stock_id, signals_input:StockSignals):
    '''Function to get a score from all the signals
    '''
    # TODO: Get score from signals and aggregate it here

    ret = signals.get_score(stock_id, signals_input.signals)

    return ret


@app.get("/signal/{signal_id}")
async def get_signal_reccomendations(signal_id):
    '''Function to get the top stocks from a given signal
    '''
    #TODO: If statements to check for each signal id
    
    ret = {
        "signal_id": signal_id,
        "stocks": [
            "APPL",
            "GOOGLE"
        ]
    }

    return ret

@app.get("/signal")
async def get_signals():
    '''Returns all signals that are available
    '''

    # TODO: Get all signals
    ret =  signals.signals

    return ret
