-- 코드를 작성해주세요
WITH F_CODE AS (
    SELECT
        SUM(CODE) AS F_CODE
    FROM
        SKILLCODES
    WHERE
        CATEGORY = 'Front End'
), PY_CODE AS (
    SELECT
        CODE AS PY_CODE
    FROM
        SKILLCODES
    WHERE
        NAME = 'Python'
), CS_CODE AS (
    SELECT
        CODE AS CS_CODE
    FROM
        SKILLCODES
    WHERE
        NAME = 'C#'
), GRADES AS (
    SELECT
        CASE 
            WHEN SKILL_CODE & PY_CODE AND SKILL_CODE & F_CODE THEN 'A'
            WHEN SKILL_CODE & CS_CODE THEN 'B'
            WHEN SKILL_CODE & F_CODE THEN 'C'
        END AS GRADE,
        ID,
        EMAIL
    FROM
        DEVELOPERS, F_CODE, PY_CODE, CS_CODE
    ORDER BY
        1, 2
)
SELECT
    *
FROM
    GRADES
WHERE
    GRADE IS NOT NULL;