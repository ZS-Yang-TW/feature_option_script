# Feature Option Script

## Backend

- Python 3, Flask, requests
- Run server: `pip install flask requests` then `python feature_option_server.py`
- Endpoints:
  - `POST /fetch_features`：抓取 API 並存成 csv
  - `GET /list_csvs`：取得所有 csv 檔名
  - `GET /csv/<filename>`：下載 csv

## Frontend

- 開啟 `frontend/index.html`，即可操作
- 需確保前端能連到 backend（預設 http://localhost:8000）

## 說明

- 按「取得 Feature Options」會抓取所有分頁資料並存成 csv
- 下拉選單可選擇不同 csv，表格會自動更新
- csv 檔名格式：`{時間}_feature_option_list.csv`

## 注意

- 若要跨網域，請於 backend 加入 CORS 支援
- 若要部署，請依需求調整 host/port
