package com.example.recommender.model;

public class Product {
    private String id;
    private String name;
    private String type;
    private double expectedReturn;
    private String riskLevel;
    private String description;
    private String category;
    private String currency;

    public Product() {}

    public Product(String id, String name, String type, double expectedReturn,
                   String riskLevel, String description, String category, String currency) {
        this.id = id;
        this.name = name;
        this.type = type;
        this.expectedReturn = expectedReturn;
        this.riskLevel = riskLevel;
        this.description = description;
        this.category = category;
        this.currency = currency;
    }

    public String getId() { return id; }
    public void setId(String id) { this.id = id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getType() { return type; }
    public void setType(String type) { this.type = type; }

    public double getExpectedReturn() { return expectedReturn; }
    public void setExpectedReturn(double expectedReturn) { this.expectedReturn = expectedReturn; }

    public String getRiskLevel() { return riskLevel; }
    public void setRiskLevel(String riskLevel) { this.riskLevel = riskLevel; }

    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }

    public String getCategory() { return category; }
    public void setCategory(String category) { this.category = category; }

    public String getCurrency() { return currency; }
    public void setCurrency(String currency) { this.currency = currency; }
}
