# Created by Andrew at 8/4/2021
Feature: Amazon Order button
  # Enter feature description here

  Scenario: Click Order button and verify Sign in page
    # Enter steps here
    Given Open Amazon site https://www.amazon.com
    When  Click Orders
    Then  Verify Sign-In page opened
