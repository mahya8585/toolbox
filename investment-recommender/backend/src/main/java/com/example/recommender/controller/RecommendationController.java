package com.example.recommender.controller;

import com.example.recommender.model.*;
import com.example.recommender.service.RecommendationService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api")
public class RecommendationController {

    private final RecommendationService service;

    public RecommendationController(RecommendationService service) {
        this.service = service;
    }

    /** 顧客情報を取得 */
    @GetMapping("/customers/{customerId}")
    public ResponseEntity<Customer> getCustomer(@PathVariable String customerId) {
        return ResponseEntity.ok(service.getCustomer(customerId));
    }

    /** 対象顧客へのおすすめ商品一覧（スコア順） */
    @GetMapping("/recommendations/{customerId}")
    public ResponseEntity<Map<String, Object>> getRecommendations(@PathVariable String customerId) {
        Customer customer = service.getCustomer(customerId);
        List<Recommendation> recommendations = service.getRecommendations(customerId);
        return ResponseEntity.ok(Map.of(
            "customer", customer,
            "recommendations", recommendations
        ));
    }

    /** 類似顧客の投資行動 */
    @GetMapping("/customers/{customerId}/similar")
    public ResponseEntity<List<SimilarCustomer>> getSimilarCustomers(@PathVariable String customerId) {
        return ResponseEntity.ok(service.getSimilarCustomers(customerId));
    }

    /** 市場トレンドとサマリー */
    @GetMapping("/market/trends")
    public ResponseEntity<List<MarketTrend>> getMarketTrends() {
        return ResponseEntity.ok(service.getMarketTrends());
    }

    /** ヘルスチェック */
    @GetMapping("/health")
    public ResponseEntity<Map<String, String>> health() {
        return ResponseEntity.ok(Map.of("status", "ok", "mode", "dummy-data"));
    }
}
