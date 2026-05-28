# 💎 AI投資商品レコメンドシステム

顧客ごとに最適な投資商品をAIが推薦するシステムです。  
フロントエンド（Vue.js）とバックエンド（Spring Boot）を **疎結合** に構成し、ローカル検証時はダミーデータを返却します。

---

## 🖥️ 画面要素

| 要素 | 説明 |
|------|------|
| 💎 おすすめ商品一覧 | AIスコア順で最適な投資商品を表示。推薦理由とExplainable AIの説明付き |
| 👥 類似顧客の投資行動 | プロファイルが類似した顧客の最近の購入商品を表示 |
| 🌍 市場トレンド | 最新の市場動向とAIサマリーを表示 |

---

## 🏗️ アーキテクチャ

```
┌─────────────────────────┐      HTTP/REST       ┌──────────────────────────┐
│  フロントエンド (Vue.js) │ ◄──────────────────► │  バックエンド (Spring Boot)│
│  http://localhost:5173   │                       │  http://localhost:8080    │
└─────────────────────────┘                       └────────────┬─────────────┘
                                                               │ (本番のみ)
                                                  ┌────────────▼─────────────┐
                                                  │  PostgreSQL               │
                                                  │  localhost:5432           │
                                                  └──────────────────────────┘
```

---

## 🚀 ローカル起動手順（ダミーデータモード）

### 前提条件
- Java 17+
- Maven 3.9+
- Node.js 20+

### バックエンド起動

```bash
cd investment-recommender/backend
mvn spring-boot:run
# → http://localhost:8080
```

### フロントエンド起動

```bash
cd investment-recommender/frontend
npm install
npm run dev
# → http://localhost:5173
```

ブラウザで `http://localhost:5173` にアクセスすると投資レコメンド画面が表示されます。

---

## 🐳 Docker Compose 起動（フルスタック）

```bash
cd investment-recommender
docker-compose up -d
```

| サービス   | URL                        |
|-----------|---------------------------|
| フロント   | http://localhost:5173      |
| バックエンド | http://localhost:8080    |
| PostgreSQL | localhost:5432             |

---

## 🔌 API エンドポイント

| メソッド | パス | 説明 |
|---------|------|------|
| `GET` | `/api/health` | ヘルスチェック |
| `GET` | `/api/customers/{customerId}` | 顧客情報取得 |
| `GET` | `/api/recommendations/{customerId}` | おすすめ商品一覧取得 |
| `GET` | `/api/customers/{customerId}/similar` | 類似顧客の投資行動 |
| `GET` | `/api/market/trends` | 市場トレンド |

### レスポンス例 `GET /api/recommendations/C001`

```json
{
  "customer": {
    "id": "C001",
    "name": "田中 花子",
    "age": 35,
    "riskTolerance": "中",
    "investmentGoal": "老後資産形成",
    "preferredCategory": "株式"
  },
  "recommendations": [
    {
      "product": {
        "id": "P007",
        "name": "バランスファンド（株式50/債券50）",
        "type": "投資信託",
        "expectedReturn": 4.8,
        "riskLevel": "中",
        "description": "株式と債券を50:50で保有。",
        "category": "バランス",
        "currency": "JPY"
      },
      "score": 0.93,
      "reasons": ["株式と債券の最適バランス", "類似顧客に最も人気", "相場変動に強い"],
      "scenarioType": "SIMILAR_CUSTOMER",
      "aiExplanation": "バランスファンドは、お客様と同じ中リスク..."
    }
  ]
}
```

---

## 🧪 テスト

### バックエンドテスト

```bash
cd investment-recommender/backend
mvn test
```

### フロントエンドテスト

```bash
cd investment-recommender/frontend
npm test
```

---

## 📁 ディレクトリ構成

```
investment-recommender/
├── backend/                         # Spring Boot バックエンド
│   ├── src/main/java/com/example/recommender/
│   │   ├── RecommenderApplication.java
│   │   ├── config/CorsConfig.java   # CORS 設定
│   │   ├── controller/RecommendationController.java
│   │   ├── service/RecommendationService.java
│   │   └── model/                   # Product, Customer, Recommendation, ...
│   ├── src/main/resources/application.properties
│   ├── Dockerfile
│   └── pom.xml
├── frontend/                        # Vue.js フロントエンド
│   ├── src/
│   │   ├── views/Dashboard.vue      # メイン画面
│   │   ├── components/
│   │   │   ├── ProductList.vue      # おすすめ商品一覧
│   │   │   ├── SimilarCustomers.vue # 類似顧客
│   │   │   └── MarketTrends.vue     # 市場トレンド
│   │   ├── services/api.js          # axios API クライアント
│   │   └── assets/global.css        # かわいいパステルテーマ
│   ├── Dockerfile
│   ├── nginx.conf
│   └── package.json
├── db/
│   └── init.sql                     # PostgreSQL スキーマ & シードデータ
└── docker-compose.yml
```

---

## 🌸 シナリオ例

| シナリオ | 動作 |
|---------|------|
| 類似顧客が購入 | `SIMILAR_CUSTOMER` シナリオとして類似顧客の購入データに基づく銘柄を推薦 |
| 金利上昇 | `MARKET_TREND` シナリオとして債券商品や金利連動商品を提示 |

---

## 🔧 本番環境（PostgreSQL 接続）での起動

`docker-compose.yml` の `backend` サービスのコメントを外してください：

```yaml
environment:
  SPRING_PROFILES_ACTIVE: prod
  DB_HOST: db
  DB_PORT: 5432
  DB_NAME: investment_db
  DB_USER: investment_user
  DB_PASSWORD: investment_pass
depends_on:
  db:
    condition: service_healthy
```
