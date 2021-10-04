# Created by Andrew at 8/30/2021
Feature: Test Scenarios for Amazom main pag
  # Enter feature description here

  Scenario: Sign-In popup disappears
    # Enter steps here
    Given Open Amazon Main Page
    Then Sign_In popup is present and clickable
    When Sign_in popup disappears

  Scenario: Bestsellers links can be opened
    # Enter steps here
    Given Open Amazon Bestsellers Page
    Then User can click through top links and verify it


