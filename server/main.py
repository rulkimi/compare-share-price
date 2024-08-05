import yfinance as yf
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Define the list of allowed origins (you can add more if needed)
origins = [
    "http://localhost",
    "http://localhost:5173",
]

# Add CORS middleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

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
