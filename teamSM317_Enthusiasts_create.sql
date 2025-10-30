CREATE TABLE Crime(Ward_Code CHAR(10), Major_Category VARCHAR(30), Value INT, Date CHAR(8));


CREATE TABLE Well_Being(New_Ward_Code CHAR(10), Borough VARCHAR(30),Year INT, Life_Expectancy FLOAT(53), Childhood_Obesity FLOAT(53), Incapacity_Benefit FLOAT(53), Unemployment FLOAT(53), Crime FLOAT(53), Deliberate_Fires FLOAT(53),
GCSE_points FLOAT(53), Unauthorised_Absence FLOAT(53), Dependent_children FLOAT(53), Public_Transport_Access FLOAT(53),
Homes_with_access FLOAT(53));

CREATE TABLE Housing(date CHAR(8), area VARCHAR(30), average_price INT, code VARCHAR(20), houses_sold INT);