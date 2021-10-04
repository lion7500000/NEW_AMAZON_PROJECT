# Created by Andrew at 8/8/2021
Feature: Amazon BestSellers Page
  # Enter feature description here

  Scenario: # Open the page and verify there ae 5 links
    # Enter steps here
    Given Open_BestSellers_Page https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers_8a080d3d7b55497ea1bdd97b7cff8b7b
    When veryfy the page has 5 links