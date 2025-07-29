# 📚 DataStructure_LineBot

這是一個以 Python Flask 撰寫的 LINE Bot Webhook Demo，作為資料結構輔助學習的互動原型。使用者可以透過 LINE 聊天介面與機器人互動，查詢各章節內容、請求 GPT 回答問題。這個專案主要用於展示 Webhook 與 LINE 開發平台的串接實作。

---

## 🛠 使用技術

| 類別       | 技術                     |
|------------|--------------------------|
| 後端框架   | Python Flask                    |
| 串接 API   | LINE Messaging API、OpenAI GPT |
| 伺服器連線 | ngrok (本地 Webhook 測試) |
| 環境管理   | `.env` + `os.getenv()`   |

---

## 📦 專案功能介紹

- ✅ **LINE Bot 串接 Webhook**
  - 使用 Flask 接收 `/callback` 路徑的 LINE Webhook 請求
  - 自動驗證簽章、觸發事件處理器

- ✅ **聊天互動邏輯**
  - 支援關鍵字判斷（例如：「鏈結串列」、「堆疊與佇列」）
  - 使用 LINE 的 QuickReply 快速選單功能，引導使用者選擇問題類型

- ✅ **GPT 整合回應**
  - 若輸入格式為 `To GPT : 問題`，將問題轉發給 OpenAI 並在 250 字內生成回覆
  - 回覆文字將以 LINE 訊息回傳給使用者

---

## 📂 專案架構概覽

```
DS_LineBot/
├── LineBot_DS.py # 主程式，包含 webhook、訊息處理邏輯
├── .env # 儲存 API 金鑰（不會上傳）
├── .gitignore # 忽略敏感與暫存檔案
├── README.md # 專案說明文件
```


---

## ⚙️ 如何啟動本地測試

1. 建立 `.env` 檔案，內容如下：

```env
OPENAI_API_KEY=your_openai_key
LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_token
LINE_CHANNEL_SECRET=your_line_channel_secret

pip install flask line-bot-sdk openai

python LineBot_DS.py

ngrok http 5000
```

將 ngrok 提供的網址設定到 LINE Developers 平台中的 Webhook URL（例如：https://xxxxxx.ngrok.io/callback）

## 🚧 開發說明
此專案為 DEMO 範例，因此未使用資料庫，也無前端頁面

所有互動皆透過 LINE Bot 完成

每個資料結構章節都設計了多個問題選項，由 GPT 回答

