# Feature Option List 專案需求紀錄

## 主要需求

- 後端：
  - 以 Flask + requests 實作 API 分頁抓取，支援自訂 cookie、user-agent 等 header（從 .env 讀取）。
  - 整理 API 回傳資料，欄位包含 Feature Name、Feature Description、Hidden、Shadow、Feature Preview、Enable、Lock。
  - 狀態欄位 true 顯示「✅」、false 顯示空白。
  - 產生 CSV 檔，檔名含時間戳，存於 backend/csv/。
  - 提供 fetch_features、list_csvs、csv 檔案下載等 API。
  - 加入 debug log，方便追蹤 API 抓取與資料轉換數量。
  - 敏感 header 參數改用 .env 管理，並提供 .env.example。
  - **支援動態 Account ID**：fetch_features API 接受 POST body 傳入 account_id 參數，不需重啟後端即可查詢不同帳號。

- 前端：
  - 純 HTML/JS，無框架。
  - 可取得/選擇不同 CSV，顯示表格。
  - 支援顯示/隱藏 Feature Description。
  - 表格欄位寬度優化，Feature Description 欄變寬，五個狀態欄等寬且較窄。
  - 支援欄寬拖曳調整（JS 實作 resizer）。
  - 支援「比較版本」功能，能選兩個 CSV，顯示新增、刪除、狀態變動（狀態變動顯示「❌→✅」等）。
  - 支援複製主表格/比較結果為 Markdown，內容自動處理換行與 | 跑版問題。
  - 介面現代化（卡片、圓角、陰影、漸層按鈕、RWD）。
  - 狀態欄標題自動換行。
  - **Account ID 輸入與顯示**：
    - 提供 Account ID 輸入框，使用者可輸入後點擊「取得新的 CSV」按鈕。
    - 在總數量上方顯示當前 CSV 的 Account ID。
    - 比較模式會顯示兩個版本的 Account ID 對照資訊，若不同則顯示警告。
  - **正確解析 CSV**：過濾掉註釋行（以 # 開頭），避免解析錯誤。
  - **比較邏輯優化**：
    - 使用 `.trim()` 處理字段值，避免空白字符導致的誤判。
    - 版本選擇標籤改為「舊版本 (從)」和「新版本 (到)」，讓使用者更清楚選擇順序。

- 其他：
  - README.md 詳細說明操作方式與注意事項。
  - .gitignore 忽略 .env、csv、__pycache__ 等。
  - requirements.txt 列出所有 Python 依賴。
  - 專案初始化即建立 master branch 並 commit。

## 已完成
- 所有功能皆已多次根據需求調整與優化，現已達成所有指定目標。
- 2026/01/15 新增：
  - 支援動態 Account ID 輸入與顯示
  - 修復 CSV 解析問題（過濾註釋行）
  - 修復比較邏輯的空白字符處理問題
  - 優化版本選擇界面標籤
- 若需進一步美化、功能擴充或 bug 修正，請再提出。
