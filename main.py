import yfinance as yf
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd

app = FastAPI()

def get_company_info(company: str):
    ticker = yf.Ticker(company)
    info = ticker.info
    return info

def get_share_price(company: str):
    data = yf.download(company, start="2020-01-01", end="2021-01-01")
    return data

def dataframe_to_json(data: pd.DataFrame):
    data.reset_index(inplace=True)  # reset the index to include the Date column
    data['Date'] = data['Date'].apply(lambda x: x.isoformat() if isinstance(x, pd.Timestamp) else x)  # convert Timestamps to strings
    return data.to_dict(orient='records')

@app.get("/data")
async def get_data(company: str = "AAPL"):
    data = get_share_price(company)
    json_data = dataframe_to_json(data)
    return JSONResponse(content=json_data)

@app.get("/company/info")
async def get_info(company: str = "AAPL"):
    company_info = get_company_info(company)
    return JSONResponse(content=company_info)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
