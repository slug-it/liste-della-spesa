Feature: base list interactions

  Scenario: add item to a list
     Given we have an empty list
      when we add "Banana" to the list
      then the list contains "Banana"
