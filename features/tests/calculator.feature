Feature: Tests for Calculator application

Scenario Outline: Simple Operations
    Given I want to do a "<OPERATION>"
    When I perform the operation between "<FIRST NUM>" and "<SECOND NUM>"
    Then the result must be "<RESULT>"
    
    Examples:
        | FIRST NUM | OPERATION | SECOND NUM | RESULT |
        | 10        | sum       | 20         | 30     |
        | 20        | sum       | 10         | 30     |
        | 10        | sum       | 10         | 20     |
        | 20        | sum       | 20         | 40     |
        | 20        | sub       | 10         | 10     |
        | 10        | sub       | 10         | 0      |
        | 20        | sub       | 20         | 0      |