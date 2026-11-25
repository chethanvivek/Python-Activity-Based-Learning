# Algorithm

1. Start.
2. Read the starting weekday.
3. Read the number of days in the month.
4. Check whether the starting weekday is between 1 and 7 and the number of days is between 28 and 31.
5. If the inputs are invalid:
   a. Display an invalid input message.
   b. Stop.
6. Display the weekday headings from Sunday to Saturday.
7. Set the current date to 1.
8. Set the first-week flag to TRUE.
9. Repeat while the current date is less than or equal to the total number of days:
   a. Repeat for seven weekdays:
   i. If it is the first week and the weekday position is before the starting weekday, display a blank space.
   ii. Otherwise, if the current date is within the month, display the date and increase it by 1.
   iii. Otherwise, display a blank space.
   b. Move to the next calendar row.
   c. Set the first-week flag to FALSE.
10. Stop.
