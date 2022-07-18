# 1. Get all countries that speak Slovene. Return country name, language, and language percentage. Order by decreasing language percentage.
-- SELECT name, language, percentage FROM countries
-- LEFT JOIN languages on countries.id = languages.country_id WHERE language="Slovene"
-- ORDER BY percentage DESC

# 2. Display the total number of cities for each country. Return name of the country and total number of cities. Arrange result by the number of cities in descending order.
-- SELECT countries.name, count(cities.name) as cities FROM countries
-- LEFT JOIN cities on countries.id = cities.country_id
-- GROUP BY countries.name
-- ORDER BY cities DESC

# 3. Get all cities in Mexico with a population of greater than 500,000. Arrange result by population in descending order.
-- SELECT name, population, country_id FROM cities WHERE population > 500000 AND country_id = 136
-- ORDER BY population DESC

-- SELECT cities.name, cities.populatiom FROM cities
-- JOIN countries ON cities.country_id = countries.id
-- WHERE countries.name = "Mexico" and cities.population > 500000
-- ORDER BY cities.population DESC

# 4. Get all languages in each country with a percentage greater than 89%. Arrange result by percentage in descending order.
-- SELECT countries.name, languages.language, languages.percentage FROM countries
-- JOIN languages ON languages.country_id = countries.id
-- WHERE languages.percentage > 89
-- ORDER BY languages.percentage DESC

# 5. Get all countries with Surface Area below 501 and Population greater than 100,000.
-- SELECT name, surface_area, population FROM countries WHERE surface_area < 501 and population > 100000

# 6. Get countries with only Constitutional Monarchy with a capital greater than 200 and a life expectancy greater than 75 years.
-- SELECT name, government_form, capital, life_expectancy FROM countries
-- WHERE government_form = "Constitutional Monarchy" AND capital > 200 AND life_expectancy > 75

# 7. Get all cities of Argentina inside Buenos Aires district and have population greater than 500,000. Return Country Name, City Name, District, and Population.
-- SELECT countries.name as country, cities.name as city, cities.district, cities.population FROM countries
-- JOIN cities ON cities.country_id = countries.id
-- WHERE countries.name = "Argentina" AND cities.district = "Buenos Aires" AND cities.population > 500000

#8. Summarize the number of countries in each region. Return the name of the region and the number of countries. Arrange the result by number of countries in descending order. 
-- SELECT countries.region, count(countries.name) FROM countries
-- GROUP BY countries.region ORDER BY count(countries.name) DESC