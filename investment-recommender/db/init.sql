-- ============================================================
-- Investment Recommender – PostgreSQL schema & seed data
-- (Used when SPRING_PROFILES_ACTIVE=prod)
-- ============================================================

CREATE TABLE IF NOT EXISTS customers (
    id               VARCHAR(20) PRIMARY KEY,
    name             VARCHAR(100) NOT NULL,
    age              INT NOT NULL,
    risk_tolerance   VARCHAR(10) NOT NULL CHECK (risk_tolerance IN ('低', '中', '高')),
    investment_goal  VARCHAR(100),
    preferred_category VARCHAR(50),
    created_at       TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS products (
    id               VARCHAR(20) PRIMARY KEY,
    name             VARCHAR(200) NOT NULL,
    type             VARCHAR(50) NOT NULL,
    expected_return  DECIMAL(5,2),
    risk_level       VARCHAR(10) NOT NULL CHECK (risk_level IN ('低', '中', '高')),
    description      TEXT,
    category         VARCHAR(50),
    currency         VARCHAR(10) DEFAULT 'JPY',
    created_at       TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS market_trends (
    id              VARCHAR(20) PRIMARY KEY,
    name            VARCHAR(200) NOT NULL,
    direction       VARCHAR(10) NOT NULL CHECK (direction IN ('UP', 'DOWN', 'STABLE')),
    summary         TEXT,
    impact          TEXT,
    category        VARCHAR(50),
    change_percent  DECIMAL(6,2),
    last_updated    DATE,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS recommendations (
    id              SERIAL PRIMARY KEY,
    customer_id     VARCHAR(20) REFERENCES customers(id),
    product_id      VARCHAR(20) REFERENCES products(id),
    score           DECIMAL(4,3) NOT NULL,
    scenario_type   VARCHAR(50),
    ai_explanation  TEXT,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS recommendation_reasons (
    id                 SERIAL PRIMARY KEY,
    recommendation_id  INT REFERENCES recommendations(id),
    reason             TEXT NOT NULL
);

-- ── Seed data ────────────────────────────────────────────────────────

INSERT INTO customers (id, name, age, risk_tolerance, investment_goal, preferred_category)
VALUES
    ('C001', '田中 花子', 35, '中', '老後資産形成', '株式'),
    ('C002', '山田 太郎', 52, '低', '安定運用', '債券'),
    ('C003', '鈴木 美咲', 28, '高', '資産増加', '株式'),
    ('C004', '佐藤 健一', 45, '中', '分散投資', 'バランス')
ON CONFLICT (id) DO NOTHING;

INSERT INTO products (id, name, type, expected_return, risk_level, description, category, currency)
VALUES
    ('P001', 'グローバル株式ファンド',           '投資信託', 7.20, '中', '世界中の優良企業に分散投資。長期的な資産成長を目指します。',            '株式',     'JPY'),
    ('P002', '国内債券ファンド',                 '投資信託', 2.10, '低', '日本国債を中心に安定運用。元本保全を重視する方向け。',                  '債券',     'JPY'),
    ('P003', '米国テクノロジー株ETF',             'ETF',     12.50, '高', 'GAFAMを中心とした米国テック企業への集中投資。',                        '株式',     'USD'),
    ('P004', '新興国株式ファンド',               '投資信託', 9.80, '高', 'アジア・中南米の成長市場に投資。高リターンを狙います。',                '株式',     'JPY'),
    ('P005', '先進国債券ファンド',               '投資信託', 3.40, '低', '米国・欧州の国債に分散投資。為替ヘッジあり。',                          '債券',     'JPY'),
    ('P006', '不動産投資信託（J-REIT）',          'REIT',    5.60, '中', '国内商業施設・オフィスに投資。安定した配当を目指します。',              '不動産',   'JPY'),
    ('P007', 'バランスファンド（株式50/債券50）', '投資信託', 4.80, '中', '株式と債券を50:50で保有。リスクとリターンのバランス型。',              'バランス', 'JPY'),
    ('P008', '金・コモディティETF',              'ETF',     6.10, '中', '金・原油などコモディティに連動。インフレヘッジに最適。',                'コモディティ','JPY'),
    ('P009', 'ESG先進国株式ファンド',            '投資信託', 8.30, '中', '環境・社会・ガバナンスを重視した企業に投資するESGファンド。',          '株式',     'JPY'),
    ('P010', '短期国内社債ファンド',             '投資信託', 1.80, '低', '国内優良企業の短期社債に投資。流動性が高く安全性重視。',                '債券',     'JPY')
ON CONFLICT (id) DO NOTHING;

INSERT INTO market_trends (id, name, direction, summary, impact, category, change_percent, last_updated)
VALUES
    ('T001', '金利上昇トレンド',       'UP',     '米FRBの利上げを背景に金利が上昇傾向にあります。債券価格に下押し圧力。',              '債券価格が下落傾向にあるため、短期債や変動金利商品が有利です。',             '債券',   0.25, '2026-05-28'),
    ('T002', 'AI・テクノロジー株高騰', 'UP',     '生成AIブームにより米国テック企業の株価が急上昇しています。',                       'テクノロジーセクターへの投資家注目度が高まっており、ETF需要も増加。',        '株式',  15.30, '2026-05-28'),
    ('T003', '新興国通貨安',           'DOWN',   'ドル高の影響で新興国通貨が対ドルで軟調に推移しています。',                         '新興国株式・債券は為替リスクに注意が必要です。',                              '新興国',-3.20, '2026-05-28'),
    ('T004', 'ESG投資拡大',            'UP',     '機関投資家を中心にESG投資への資金流入が継続しています。',                          'ESGファンドへの長期的な資金流入が見込まれ、安定した成長が期待されます。',    '株式',   8.70, '2026-05-28'),
    ('T005', '日本不動産市場堅調',     'STABLE', 'インバウンド需要回復と企業のオフィス需要安定により、J-REIT市場が堅調です。',       '安定した配当利回りが期待でき、インカムゲイン目的の投資家に適しています。',   '不動産', 1.20, '2026-05-28')
ON CONFLICT (id) DO NOTHING;
