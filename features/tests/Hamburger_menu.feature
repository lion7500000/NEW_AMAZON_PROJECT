# Created by 16468 at 9/13/2021
Feature: #Enter feature name here
  # Enter feature description here

  Scenario: Amazom Music has 9 menu items
    # Enter steps here"ul.hmenu-visible a:not(.hmenu-back-button)"
    Given Open Amazon Main Page
    When Click to open Hamburger Menu
    Then Click on Music Menu item
    Then Check 66 Menue items are present