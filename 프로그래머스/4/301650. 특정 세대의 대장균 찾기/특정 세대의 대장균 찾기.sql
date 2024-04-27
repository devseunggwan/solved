-- 코드를 작성해주세요

SELECT
    P3.ID
FROM
    (
        SELECT 
            *
        FROM
            ECOLI_DATA
        WHERE
            PARENT_ID IS NULL
    ) P1
LEFT JOIN
    ECOLI_DATA P2
    ON P1.ID = P2.PARENT_ID
LEFT JOIN
    ECOLI_DATA P3
    ON P2.ID = P3.PARENT_ID
WHERE
    P3.ID IS NOT NULL
ORDER BY
    1
