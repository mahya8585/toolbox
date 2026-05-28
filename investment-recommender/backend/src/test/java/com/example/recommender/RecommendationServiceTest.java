package com.example.recommender;

import com.example.recommender.model.Recommendation;
import com.example.recommender.model.MarketTrend;
import com.example.recommender.model.SimilarCustomer;
import com.example.recommender.service.RecommendationService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
class RecommendationServiceTest {

    @Autowired
    private RecommendationService service;

    @Test
    void getRecommendations_highRiskCustomer_returnsHighRiskProducts() {
        List<Recommendation> result = service.getRecommendations("C003");
        assertFalse(result.isEmpty());
        assertTrue(result.stream().anyMatch(r -> r.getScore() >= 0.9));
        result.forEach(r -> assertFalse(r.getReasons().isEmpty()));
    }

    @Test
    void getRecommendations_lowRiskCustomer_returnsLowRiskProducts() {
        List<Recommendation> result = service.getRecommendations("C002");
        assertFalse(result.isEmpty());
        result.forEach(r -> {
            assertEquals("低", r.getProduct().getRiskLevel());
        });
    }

    @Test
    void getSimilarCustomers_returnsNonEmptyList() {
        List<SimilarCustomer> result = service.getSimilarCustomers("C001");
        assertFalse(result.isEmpty());
        result.forEach(sc -> assertTrue(sc.getSimilarity() > 0.7));
    }

    @Test
    void getMarketTrends_returnsExpectedTrends() {
        List<MarketTrend> result = service.getMarketTrends();
        assertFalse(result.isEmpty());
        assertTrue(result.stream().anyMatch(t -> "UP".equals(t.getDirection())));
    }
}
