package com.example.recommender.model;

public class Customer {
    private String id;
    private String name;
    private int age;
    private String riskTolerance;
    private String investmentGoal;
    private String preferredCategory;

    public Customer() {}

    public Customer(String id, String name, int age, String riskTolerance,
                    String investmentGoal, String preferredCategory) {
        this.id = id;
        this.name = name;
        this.age = age;
        this.riskTolerance = riskTolerance;
        this.investmentGoal = investmentGoal;
        this.preferredCategory = preferredCategory;
    }

    public String getId() { return id; }
    public void setId(String id) { this.id = id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }

    public String getRiskTolerance() { return riskTolerance; }
    public void setRiskTolerance(String riskTolerance) { this.riskTolerance = riskTolerance; }

    public String getInvestmentGoal() { return investmentGoal; }
    public void setInvestmentGoal(String investmentGoal) { this.investmentGoal = investmentGoal; }

    public String getPreferredCategory() { return preferredCategory; }
    public void setPreferredCategory(String preferredCategory) { this.preferredCategory = preferredCategory; }
}
