# Created by 16468 at 8/27/2021
Feature: Test Scenarios for Amazon shopping cart functionality
  # Enter feature description here

  Scenario: User has empty shopping cart
    # Enter steps here
    Given Open Amazon Main Page
    When Click on cart icon
    Then Shopping cart is empty
