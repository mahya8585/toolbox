package com.example.recommender.model;

public class MarketTrend {
    private String id;
    private String name;
    private String direction;
    private String summary;
    private String impact;
    private String category;
    private double changePercent;
    private String lastUpdated;

    public MarketTrend() {}

    public MarketTrend(String id, String name, String direction, String summary,
                       String impact, String category, double changePercent, String lastUpdated) {
        this.id = id;
        this.name = name;
        this.direction = direction;
        this.summary = summary;
        this.impact = impact;
        this.category = category;
        this.changePercent = changePercent;
        this.lastUpdated = lastUpdated;
    }

    public String getId() { return id; }
    public void setId(String id) { this.id = id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getDirection() { return direction; }
    public void setDirection(String direction) { this.direction = direction; }

    public String getSummary() { return summary; }
    public void setSummary(String summary) { this.summary = summary; }

    public String getImpact() { return impact; }
    public void setImpact(String impact) { this.impact = impact; }

    public String getCategory() { return category; }
    public void setCategory(String category) { this.category = category; }

    public double getChangePercent() { return changePercent; }
    public void setChangePercent(double changePercent) { this.changePercent = changePercent; }

    public String getLastUpdated() { return lastUpdated; }
    public void setLastUpdated(String lastUpdated) { this.lastUpdated = lastUpdated; }
}
