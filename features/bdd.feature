# Created by DESKTOP at 21/07/2022
Feature: Adder
  # Enter feature description here

  Scenario Outline: Adds two numbers
    Brief description

    Given the first number is <op1>
    And the second number is <op2>
    When I sum the two numbers
    Then the result must be <result>

    Examples:
    | op1 | op2 | result  |
    | 2   | 5   | 7       |
    | 12  | 35  | 47      |

  Scenario Outline: Multiplies two numbers

    Given the first number is <op1>
    And the second number is <op2>
    When I multiply the two numbers
    Then the result must be <result>

    Examples:
    | op1 | op2 | result |
    | 5   | 5   | 25     |

