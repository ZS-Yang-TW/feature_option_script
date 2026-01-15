|  | **isStaff** | **! isStaff** |
| --- | --- | --- |
| **管理員** | ✅ 有開課入口按鈕
- 進入開課畫面 → 正常顯示 | ✅ 有開課入口按鈕
- 已登入，透過連結進入開課畫面 → UnauthorizedPage 
- 重新登入，進入開課畫面 → 403 空白頁 |
| **教師** | ✅ 有開課入口按鈕
- 已登入，透過連結進入開課畫面 → 正常顯示
- 重新登入，透過連結進入開課畫面 → 正常顯示 | ❌「沒有」開課入口按鈕
- 已登入，透過連結進入開課畫面 → UnauthorizedPage 
- 重新登入，透過連結進入開課畫面 → 403 空白頁 |
| **學生** | ❌「沒有」開課入口按鈕 
- 已登入，透過連結進入開課畫面 → UnauthorizedPage 
- 重新登入，透過連結進入開課畫面 → 403 空白頁 | ❌「沒有」開課入口按鈕
- 已登入，透過連結進入開課畫面 → UnauthorizedPage 
- 重新登入，透過連結進入開課畫面 → 403 空白頁 |

我有一個 API 叫做 https://cool.testing.dlc.ntu.edu.tw/api/v1/accounts/1/features?hide_inherited_enabled=true&per_page=50&page=1

其中有幾個資訊是我在意的，他們的判斷方式是：

```json
  {
    "feature": "outcome_gradebook",
    "applies_to": "Course",
    "root_opt_in": false,
    "type": "setting",
    "display_name": "Learning Mastery Gradebook",
    "description": "Learning Mastery Gradebook provides a way for teachers to quickly view student and course\nprogress on course learning outcomes. Outcomes are presented in a Gradebook-like\nformat and student progress is displayed both as a numerical score and as mastered/near\nmastery/remedial.",
    "feature_flag": {
      "context_id": 2,
      "context_type": "Account",
      "feature": "outcome_gradebook",
      "state": "off",
      "locking_account_id": null,
      "transitions": {
        "on": {
          "locked": false
        },
        "allowed": {
          "locked": false
        },
        "allowed_on": {
          "locked": false
        }
      },
      "locked": true,
      "hidden": false,
      "parent_state": "off"
    }
  },
```

其中有幾個資訊是我在意的，他們的判斷方式是：

```json
Hidden： featureOption.hidden === true

Shadow： featureOption.shadow === true

Feature Preview - featureOption.beta === true

Enable - featureOption.sate === “on”

Lock - featureOption.locked === true
```

還有一些資訊我想取得：

```json
Feature Name：featureOption.display_name

Feature Description：featureOption.description
```

以下幾個需求請幫我完成：

1. 應該要有一個網頁，可以按「取的 Feature Options」按鈕，就能幫我透過改 page 的參數，直到回傳是空陣列，取得所有 featureOptions。
2. 利用這些 featureOptions，幫我整理表格：

| Feature Name | Feature Description | Hidden | Shadow | Feature Preview | Enable | Lock

1. 這個表格要存成 .csv，檔名為{時間_feature_option_list}
2. 介面上要有一個選單，可以選擇不同時間 .csv，並更新表格。

因為我想要保持使用簡單，所以前端盡量保持簡單不要用太多框架。
取得資料的邏輯可以用 python 實作