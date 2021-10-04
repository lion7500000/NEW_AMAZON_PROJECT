# Created by 16468 at 9/16/2021
Feature: Test prverify_size_tooltipoduct page
  # Enter feature description here

  Scenario: Size tooltip is show upon hovers over
    # Enter steps here
    Given Open amazon product B098QQFMFV
    When Hover over Add to Cart button
    Then Verify Size selection tooltip is show

    
  Scenario: New Arrivals has the deals
    Given Open amazon product B074TBCSC8
    When Hover over New Arrivals
    Then Verify New Arrivals is show

  @smoke
  Scenario: Verify user can select and search in an department
    Given Open Amazon Main Page
    When Selected books department
    And Search for Faust
    Then Verify Books department is selected