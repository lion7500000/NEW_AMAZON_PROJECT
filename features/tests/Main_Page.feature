# Created by Andrew at 8/14/2021
Feature: Amazon Main Page

  Scenario: Amazon search returns correct result

      Given Open Amazon Main Page
      Then  Input Dress into Amazon serch field
      And   Click on Amazon serch icon
      Then Search result Dress is shown


  Scenario: Amazon users see Sigh up button
      # Enter steps here
      Given Open Amazon Main Page
      Then Verify Sigh In is visible
      When Waite 5 sec
      Then Verify Sigh In is visible
      And Verify Sing In disappears


  Scenario: Logged out user sees Sign in page when clicking Orders
      Given Open Amazon Main Page
      When Click Amazon Orders link
      Then Verify Sign In page is opened


  Scenario: 'Your Shopping Cart is empty' shown if no product added
      Given Open Amazon Main Page
      When Click on cart icon
      Then Verify 'Your Amazon Cart is empty' text present


