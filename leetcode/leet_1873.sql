SELECT employee_id, if(
    name NOT LIKE "M%" and employee_id % 2 = 1,
    salary,0) AS bonus 
    FROM Employees
;