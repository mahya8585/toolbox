package com.example.recommender.model;

import java.util.List;

public class Recommendation {
    private Product product;
    private double score;
    private List<String> reasons;
    private String scenarioType;
    private String aiExplanation;

    public Recommendation() {}

    public Recommendation(Product product, double score, List<String> reasons,
                          String scenarioType, String aiExplanation) {
        this.product = product;
        this.score = score;
        this.reasons = reasons;
        this.scenarioType = scenarioType;
        this.aiExplanation = aiExplanation;
    }

    public Product getProduct() { return product; }
    public void setProduct(Product product) { this.product = product; }

    public double getScore() { return score; }
    public void setScore(double score) { this.score = score; }

    public List<String> getReasons() { return reasons; }
    public void setReasons(List<String> reasons) { this.reasons = reasons; }

    public String getScenarioType() { return scenarioType; }
    public void setScenarioType(String scenarioType) { this.scenarioType = scenarioType; }

    public String getAiExplanation() { return aiExplanation; }
    public void setAiExplanation(String aiExplanation) { this.aiExplanation = aiExplanation; }
}
