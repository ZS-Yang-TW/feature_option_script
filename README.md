# Feature Option List 專案

本專案為一個簡易的「功能選項（Feature Option）」前後端系統，支援 API 抓取、版本比對、CSV 匯出、Markdown 複製等功能。

---

## 目錄結構

- backend/  
  Flask API server，負責抓取 feature options 並產生 CSV。
- frontend/  
  純 HTML/JS 前端，現代化 UI，支援表格顯示、欄寬調整、版本比較。
- requirements.txt  
  Python 依賴套件清單。
- backend/.env.example  
  API header 參數範本，請複製為 `.env` 並填入實際值。

---

## 安裝與啟用流程

1. **安裝 Python 套件**

   ```sh
   pip install -r requirements.txt
   ```

2. **設定 API header**

   - 複製 `backend/.env.example` 為 `backend/.env`。
   - 依照說明填入 `API_COOKIE`、`API_USER_AGENT` 等資訊。

3. **啟動後端 Flask 伺服器**

   ```sh
   cd backend
   python feature_option_server.py
   ```
   預設監聽 http://localhost:8000

4. **使用前端**

   - 直接瀏覽 `frontend/index.html` 或透過 Flask 伺服器存取首頁。
   - 主要功能：
     - 取得/選擇不同 CSV，顯示表格
     - 欄寬可拖曳調整
     - 支援版本比較、複製 Markdown

---

## 注意事項
- `.env` 請勿加入 git，僅供本地開發。
- 若 API 權限或 header 有異動，請重新填寫 .env。
- 產生的 CSV 會存於 `backend/csv/`。

---

## 需求/功能說明
請見 `./copilot/project_requirement.md`。
