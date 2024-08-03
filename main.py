import yfinance as yf
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
import os

app = FastAPI()

def get_company_info(company: str):
    ticker = yf.Ticker(company)
    info = ticker.info  # Get the company info dictionary
    return info

def get_share_price(company: str):
    data = yf.download(company, start="2020-01-01", end="2021-01-01")
    file_path = 'aapl_data.xlsx'  # You might want to use a variable to set file name
    data.to_excel(file_path, engine='openpyxl')
    return file_path

def read_excel_to_json(file_path: str):
    data = pd.read_excel(file_path, engine='openpyxl')
    # Convert Timestamps to strings
    data = data.applymap(lambda x: x.isoformat() if isinstance(x, pd.Timestamp) else x)
    return data.to_dict(orient='records')

@app.get("/data")
async def get_data(company: str = "AAPL"):
    file_path = get_share_price(company)
    json_data = read_excel_to_json(file_path)
    os.remove(file_path)  # Clean up the file after reading
    return JSONResponse(content=json_data)

@app.get("/company/info")
async def get_info(company: str = "AAPL"):
    company_info = get_company_info(company)
    return JSONResponse(content=company_info)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
