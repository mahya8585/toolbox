package com.example.recommender.service;

import com.example.recommender.model.*;
import org.springframework.stereotype.Service;

import java.util.Arrays;
import java.util.List;
import java.util.Map;

/**
 * Investment recommendation service.
 * Returns dummy data for local development. In production, this service
 * integrates with PostgreSQL and ML models via JPA repositories.
 */
@Service
public class RecommendationService {

    // ── Dummy master data ───────────────────────────────────────────────

    private static final List<Product> ALL_PRODUCTS = Arrays.asList(
        new Product("P001", "グローバル株式ファンド", "投資信託", 7.2, "中",
            "世界中の優良企業に分散投資。長期的な資産成長を目指します。", "株式", "JPY"),
        new Product("P002", "国内債券ファンド", "投資信託", 2.1, "低",
            "日本国債を中心に安定運用。元本保全を重視する方向け。", "債券", "JPY"),
        new Product("P003", "米国テクノロジー株ETF", "ETF", 12.5, "高",
            "GAFAMを中心とした米国テック企業への集中投資。", "株式", "USD"),
        new Product("P004", "新興国株式ファンド", "投資信託", 9.8, "高",
            "アジア・中南米の成長市場に投資。高リターンを狙います。", "株式", "JPY"),
        new Product("P005", "先進国債券ファンド", "投資信託", 3.4, "低",
            "米国・欧州の国債に分散投資。為替ヘッジあり。", "債券", "JPY"),
        new Product("P006", "不動産投資信託（J-REIT）", "REIT", 5.6, "中",
            "国内商業施設・オフィスに投資。安定した配当を目指します。", "不動産", "JPY"),
        new Product("P007", "バランスファンド（株式50/債券50）", "投資信託", 4.8, "中",
            "株式と債券を50:50で保有。リスクとリターンのバランス型。", "バランス", "JPY"),
        new Product("P008", "金・コモディティETF", "ETF", 6.1, "中",
            "金・原油などコモディティに連動。インフレヘッジに最適。", "コモディティ", "JPY"),
        new Product("P009", "ESG先進国株式ファンド", "投資信託", 8.3, "中",
            "環境・社会・ガバナンスを重視した企業に投資するESGファンド。", "株式", "JPY"),
        new Product("P010", "短期国内社債ファンド", "投資信託", 1.8, "低",
            "国内優良企業の短期社債に投資。流動性が高く安全性重視。", "債券", "JPY")
    );

    private static final Map<String, Customer> CUSTOMERS = Map.of(
        "C001", new Customer("C001", "田中 花子", 35, "中", "老後資産形成", "株式"),
        "C002", new Customer("C002", "山田 太郎", 52, "低", "安定運用", "債券"),
        "C003", new Customer("C003", "鈴木 美咲", 28, "高", "資産増加", "株式"),
        "C004", new Customer("C004", "佐藤 健一", 45, "中", "分散投資", "バランス")
    );

    // ── Public API ───────────────────────────────────────────────────────

    public Customer getCustomer(String customerId) {
        return CUSTOMERS.getOrDefault(customerId,
            new Customer(customerId, "ゲスト顧客", 40, "中", "資産運用", "バランス"));
    }

    public List<Recommendation> getRecommendations(String customerId) {
        Customer customer = getCustomer(customerId);
        return buildRecommendations(customer);
    }

    public List<SimilarCustomer> getSimilarCustomers(String customerId) {
        return Arrays.asList(
            new SimilarCustomer("S001", "A・Kさん (35歳)", 35, 0.92, "成長重視",
                Arrays.asList(ALL_PRODUCTS.get(0), ALL_PRODUCTS.get(2))),
            new SimilarCustomer("S002", "M・Tさん (38歳)", 38, 0.87, "バランス型",
                Arrays.asList(ALL_PRODUCTS.get(6), ALL_PRODUCTS.get(8))),
            new SimilarCustomer("S003", "Y・Sさん (33歳)", 33, 0.81, "安定成長",
                Arrays.asList(ALL_PRODUCTS.get(4), ALL_PRODUCTS.get(5)))
        );
    }

    public List<MarketTrend> getMarketTrends() {
        return Arrays.asList(
            new MarketTrend("T001", "金利上昇トレンド", "UP",
                "米FRBの利上げを背景に金利が上昇傾向にあります。債券価格に下押し圧力。",
                "債券価格が下落傾向にあるため、短期債や変動金利商品が有利です。",
                "債券", 0.25, "2026-05-28"),
            new MarketTrend("T002", "AI・テクノロジー株高騰", "UP",
                "生成AIブームにより米国テック企業の株価が急上昇しています。",
                "テクノロジーセクターへの投資家注目度が高まっており、ETF需要も増加。",
                "株式", 15.3, "2026-05-28"),
            new MarketTrend("T003", "新興国通貨安", "DOWN",
                "ドル高の影響で新興国通貨が対ドルで軟調に推移しています。",
                "新興国株式・債券は為替リスクに注意が必要です。",
                "新興国", -3.2, "2026-05-28"),
            new MarketTrend("T004", "ESG投資拡大", "UP",
                "機関投資家を中心にESG投資への資金流入が継続しています。",
                "ESGファンドへの長期的な資金流入が見込まれ、安定した成長が期待されます。",
                "株式", 8.7, "2026-05-28"),
            new MarketTrend("T005", "日本不動産市場堅調", "STABLE",
                "インバウンド需要回復と企業のオフィス需要安定により、J-REIT市場が堅調です。",
                "安定した配当利回りが期待でき、インカムゲイン目的の投資家に適しています。",
                "不動産", 1.2, "2026-05-28")
        );
    }

    // ── Private helpers ──────────────────────────────────────────────────

    private List<Recommendation> buildRecommendations(Customer customer) {
        return switch (customer.getRiskTolerance()) {
            case "高" -> Arrays.asList(
                new Recommendation(ALL_PRODUCTS.get(2), 0.95,
                    Arrays.asList("類似顧客の93%が購入", "テクノロジーセクターが好調", "高リターンを目指すプロファイルに適合"),
                    "SIMILAR_CUSTOMER", "お客様と同じ高リスク許容度を持つ類似顧客の購入データを分析した結果、米国テクノロジー株ETFが最も高いスコアを獲得しました。AI銘柄の成長トレンドとの相関も高く、リターン最大化に貢献する可能性があります。"),
                new Recommendation(ALL_PRODUCTS.get(3), 0.88,
                    Arrays.asList("新興国市場が回復基調", "ポートフォリオ分散効果が高い", "長期投資に最適"),
                    "MARKET_TREND", "新興国株式市場の回復トレンドをAIが検出。お客様の年齢・投資目標を考慮すると、長期保有による資産成長が期待されます。"),
                new Recommendation(ALL_PRODUCTS.get(8), 0.82,
                    Arrays.asList("ESGトレンドに沿った投資", "機関投資家の資金流入継続", "リスク調整後リターンが優秀"),
                    "MARKET_TREND", "ESG投資への資金流入トレンドをAIが検知。社会的責任投資と高リターンを両立できる銘柄です。")
            );
            case "低" -> Arrays.asList(
                new Recommendation(ALL_PRODUCTS.get(1), 0.96,
                    Arrays.asList("元本保全を重視したプロファイルに最適", "金利上昇局面で有利", "類似顧客の安定運用ポートフォリオ上位"),
                    "SIMILAR_CUSTOMER", "お客様と同様に安全性を重視する顧客層において、国内債券ファンドは最も選ばれている商品です。現在の金利上昇局面でも安定した利回りを確保できます。"),
                new Recommendation(ALL_PRODUCTS.get(4), 0.89,
                    Arrays.asList("為替ヘッジで安定運用", "先進国国債で信用リスク低", "定期的な利息収入"),
                    "MARKET_TREND", "先進国の国債金利上昇により、ファンドの利回りが改善しています。為替ヘッジ付きのため、円安局面でも安心して保有できます。"),
                new Recommendation(ALL_PRODUCTS.get(9), 0.83,
                    Arrays.asList("流動性が高い", "短期運用に最適", "優良企業の社債で安全性確保"),
                    "SIMILAR_CUSTOMER", "短期国内社債ファンドは、元本保全を重視しつつも普通預金より高い利回りを確保できます。類似顧客の安定運用層に人気の商品です。")
            );
            default -> Arrays.asList(
                new Recommendation(ALL_PRODUCTS.get(6), 0.93,
                    Arrays.asList("株式と債券の最適バランス", "類似顧客に最も人気", "相場変動に強い"),
                    "SIMILAR_CUSTOMER", "バランスファンドは、お客様と同じ中リスク許容度の顧客層で最も支持されている商品です。市場の変動を抑えながら安定した成長を目指せます。"),
                new Recommendation(ALL_PRODUCTS.get(0), 0.87,
                    Arrays.asList("グローバル分散で安定成長", "長期投資に適した商品", "老後資産形成に人気"),
                    "MARKET_TREND", "グローバル株式市場の長期的な成長トレンドに乗ることができます。世界中の優良企業に分散投資するため、特定地域のリスクを軽減できます。"),
                new Recommendation(ALL_PRODUCTS.get(5), 0.80,
                    Arrays.asList("安定した配当収入", "インフレヘッジ効果", "不動産市場が堅調"),
                    "MARKET_TREND", "日本の不動産市場の堅調さをAIが検知。J-REITは安定した分配金を提供し、インフレに対するヘッジ効果も期待できます。")
            );
        };
    }
}
