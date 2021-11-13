from fastapi import FastAPI

app = FastAPI()


@app.get("/test")
async def root():
    return {"Hello": "World"}

@app.get("/stock/{stock_id}")
async def get_stock_score(stock_id):
    '''Function to get a score from all the signals
    '''
    # TODO: Get score from signals and aggregate it here
    return stock_id


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
    ret =  [
        "Signal A",
        "Signal B",
        "Signal C"
    ]

    return ret