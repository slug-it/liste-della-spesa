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
    Given we have a list created by Alice containing
        |    item    |
        | Blue socks |
        | T-shirt    |
      when she types "blue"
      then the suggestion is "Blue socks"

  Scenario: Alice renames and element added by Bob
    Given we have a list created by Bob containing
        |  item  |
        | Lemons |
        | Apples |
      when Alice replaces "Lemons" with "Organic Lemons"
      then the list is
        |      item      |
        | Apples         |
        | Organic Lemons |
      and the item "Organic Lemons" is marked as added by Alice
      and the original of "Organic Lemons" is "Lemons" and marked as added by Bob

  Scenario: Alice removes one item from an existing list
    Given we have a list created by Alice containing
        |    item    |
        | Blue socks |
        | Oranges    |
        | T-shirt    |
      when she removes "Oranges"
      then the list is
        |    item    |
        | Blue socks |
        | T-shirt    |

  Scenario: Bob postpones one item
    Given we have a list created by Bob containing
        |   item   |
        | Lemons   |
        | Apples   |
        | Tomatoes |
      when he postpones by 7 days the item "Apples"
      then the list does not contains "Apples"
      then the list contains "Apples"

  Scenario: Bob postpones one item
    Given we have a list created by Bob containing
        |   item   |
        | Lemons   |
        | Apples   |
        | Tomatoes |
      and 4 days ago he postponed by 7 days the item "Apples"
      then the list does not contains "Apples"
      then the list contains "Apples"

  Scenario: Bob postpones one item
    Given we have a list created by Bob containing
        |   item   |
        | Lemons   |
        | Apples   |
        | Tomatoes |
      and 6 days ago he postponed by 7 days the item "Apples"
      then the list contains "Apples"
