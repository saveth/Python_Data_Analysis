/*
Project: Restaurants
*/

/* 1. Examine DataTable
 	Database Schema--column names */
PRAGMA table_info(table_name);

/* 2. Distinct Neighborhood */
select distinct neighborhood
from nomnom;

/*3. Distinc Cusine */
select distinct cuisine
from nomnom;

/* 4. Options for Chinese Cusine */
select name
from nomnom
where cuisine = 'Chinese';

/* 5. Reviews at/above 4 */
select name, review
from nomnom
where review >= 4
order by review desc;

/* 6. Expensive Italian Places */
select name, price
from nomnom
where price == '$$$';

/* 7. A place named meatball */
select name
from nomnom
where name like '%meatball%';

/* 8. Delivery from selected location */
select name, neighborhood
from nomnom
where neighborhood='Midtown' or neighborhood='Downtown' or neighborhood='Chinatown'
order by neighborhood;

/* 9. Missing health score */
select name, health
from nomnom
where health is null;

/* 10. Top 10 Restaurants */
select name, review
from nomnom
where review >= 4
order by review desc
limit 10;

/* 11. New Variable */
select name, review,
case
	when review >= 4.5 then 'Extraordinary'
	when review >= 4 and review < 4.5 then 'Excellent'
	when review >= 3 and review < 4 then 'Good'
	when review >=2 and review < 3 then 'Fair'
else 'Poor'
end review2
from nomnom
order by review desc;