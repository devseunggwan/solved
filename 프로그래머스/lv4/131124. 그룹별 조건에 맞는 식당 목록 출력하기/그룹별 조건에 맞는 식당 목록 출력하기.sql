WITH CTE AS (
    SELECT
        MEMBER_ID
        , COUNT(*) AS REVIEW_COUNT
    FROM
        REST_REVIEW        
    GROUP BY
        MEMBER_ID
    HAVING
        REVIEW_COUNT = (
            SELECT
                COUNT(*) AS REVIEW_COUNT
            FROM
                REST_REVIEW
            GROUP BY
                MEMBER_ID
            ORDER BY
                REVIEW_COUNT DESC
            LIMIT 1
        )
)

SELECT
    P.MEMBER_NAME
    , R.REVIEW_TEXT
    , DATE_FORMAT(R.REVIEW_DATE, "%Y-%m-%d") AS REVIEW_DATE
FROM
    REST_REVIEW R
LEFT JOIN MEMBER_PROFILE P
    ON R.MEMBER_ID = P.MEMBER_ID
INNER JOIN CTE
    ON R.MEMBER_ID = CTE.MEMBER_ID
ORDER BY
    REVIEW_DATE ASC
    , R.REVIEW_TEXT ASC