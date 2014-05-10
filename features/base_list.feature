Feature: base list interactions

  Scenario: add one item to a list
     Given we have an empty list
         when we add "Banana" to the list
         then the list contains "Banana"
         and the list contains 1 item

  Scenario: add two items to a list
     Given we have an empty list
         when we add "Banana" to the list
         and we add "Apricot" to the list
         then the list contains "Apricot" and "Banana" in this order

  Scenario: Bob adds and one item to a list
     Given we have an empty list created by Bob
         when Bob adds "Banana" to the list
         then the item "Banana" is marked as added by Bob

  Scenario: Bob adds and two items to a list
     Given we have an empty list created by Bob
         when Bob adds "Banana" to the list
         and Bob adds "Milk" to the list
         then the item "Banana" is marked as added before than "Milk"

  Scenario: Alice adds one item to an existing list
     Given we have a list created by Alice containing "Blue socks"
         when she types "blue"
         then the suggestion is "Blue socks"



