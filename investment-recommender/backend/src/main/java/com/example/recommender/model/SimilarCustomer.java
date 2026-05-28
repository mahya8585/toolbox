package com.example.recommender.model;

import java.util.List;

public class SimilarCustomer {
    private String id;
    private String name;
    private int age;
    private double similarity;
    private String investmentStyle;
    private List<Product> recentPurchases;

    public SimilarCustomer() {}

    public SimilarCustomer(String id, String name, int age, double similarity,
                           String investmentStyle, List<Product> recentPurchases) {
        this.id = id;
        this.name = name;
        this.age = age;
        this.similarity = similarity;
        this.investmentStyle = investmentStyle;
        this.recentPurchases = recentPurchases;
    }

    public String getId() { return id; }
    public void setId(String id) { this.id = id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }

    public double getSimilarity() { return similarity; }
    public void setSimilarity(double similarity) { this.similarity = similarity; }

    public String getInvestmentStyle() { return investmentStyle; }
    public void setInvestmentStyle(String investmentStyle) { this.investmentStyle = investmentStyle; }

    public List<Product> getRecentPurchases() { return recentPurchases; }
    public void setRecentPurchases(List<Product> recentPurchases) { this.recentPurchases = recentPurchases; }
}
