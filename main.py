import yfinance as yf
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd

app = FastAPI()

def get_company_info(company_ticker: str):
    ticker = yf.Ticker(company_ticker)
    info = ticker.info
    return info

def get_share_price(company_ticker: str, start_date: str, end_date: str):
    data = yf.download(company_ticker, start=start_date, end=end_date)
    return data

def dataframe_to_json(data: pd.DataFrame):
    data.reset_index(inplace=True)  # reset the index to include the Date column
    data['Date'] = data['Date'].apply(lambda x: x.isoformat() if isinstance(x, pd.Timestamp) else x)  # convert Timestamps to strings
    return data.to_dict(orient='records')

@app.get("/share_price/{company_ticker}")
async def get_data(start_date: str, end_date: str, company_ticker: str = "AAPL"):
    data = get_share_price(company_ticker, start_date, end_date)
    json_data = dataframe_to_json(data)
    return JSONResponse(content=json_data)

@app.get("/company_info/{company_ticker}")
async def get_profile(company_ticker: str):
    company_info = get_company_info(company_ticker)
    return JSONResponse(content=company_info)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
