# Problem 2
Using the data model provided by Open Brewery DB, write a mock SQL query finding all microbreweries in Canada. You can assume that brewery data is stored in a table called “breweries”.

# Solution and Comments
We can assume that breweries located in Canada would have the `country` attribute set to 'Canada'
We also assume that we want all columns

## Query
```sql
SELECT *
FROM breweries
WHERE country='Canada';
```