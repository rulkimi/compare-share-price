from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd

app = FastAPI()

def read_excel_to_json(file_path: str):
    data = pd.read_excel(file_path, engine='openpyxl')
    # Convert Timestamps to strings
    data = data.applymap(lambda x: x.isoformat() if isinstance(x, pd.Timestamp) else x)
    return data.to_dict(orient='records')

@app.get("/data")
async def get_data():
    file_path = 'aapl_data.xlsx'  # Path to your Excel file
    json_data = read_excel_to_json(file_path)
    return JSONResponse(content=json_data)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
