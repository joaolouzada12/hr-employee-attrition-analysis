-- HR ATTRITION ANALYSIS (SQL)

-- 1. Attrition by Salary Band
SELECT 
    CASE 
        WHEN MonthlyIncome < 4000 THEN 'Low'
        WHEN MonthlyIncome BETWEEN 4000 AND 7000 THEN 'Medium'
        ELSE 'High'
    END AS salary_band,
    ROUND(AVG(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100, 2) AS attrition_rate
FROM employees
GROUP BY salary_band;


-- 2. Attrition by OverTime
SELECT 
    OverTime,
    ROUND(AVG(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100, 2) AS attrition_rate
FROM employees
GROUP BY OverTime;


-- 3. Salary + OverTime (Main Insight)
SELECT 
    CASE 
        WHEN MonthlyIncome < 4000 THEN 'Low'
        WHEN MonthlyIncome BETWEEN 4000 AND 7000 THEN 'Medium'
        ELSE 'High'
    END AS salary_band,
    OverTime,
    ROUND(AVG(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100, 2) AS attrition_rate
FROM employees
GROUP BY salary_band, OverTime;


-- 4. Attrition by Department
SELECT 
    Department,
    ROUND(AVG(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100, 2) AS attrition_rate
FROM employees
GROUP BY Department;


-- 5. Attrition by Job Satisfaction
SELECT 
    JobSatisfaction,
    ROUND(AVG(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100, 2) AS attrition_rate
FROM employees
GROUP BY JobSatisfaction;


-- 6. Attrition by Tenure
SELECT 
    CASE 
        WHEN YearsAtCompany <= 2 THEN 'Early'
        WHEN YearsAtCompany BETWEEN 3 AND 7 THEN 'Mid'
        ELSE 'Senior'
    END AS tenure_group,
    ROUND(AVG(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100, 2) AS attrition_rate
FROM employees
GROUP BY tenure_group;