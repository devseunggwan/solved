SELECT
    H.HISTORY_ID
    , ROUND(C.DAILY_FEE * H.DURATION * ((100-IF(P.DISCOUNT_RATE IS NULL, 0, P.DISCOUNT_RATE))/100), 0) AS FEE
FROM
    (
        SELECT
            *
            , DATEDIFF(END_DATE, START_DATE) + 1 AS DURATION
            , CASE
                WHEN DATEDIFF(END_DATE, START_DATE) + 1 >= "90" THEN "90일 이상"
                WHEN DATEDIFF(END_DATE, START_DATE) + 1 >= "30" THEN "30일 이상"
                WHEN DATEDIFF(END_DATE, START_DATE) + 1 >= "7" THEN "7일 이상"
                ELSE 0
            END AS DURATION_TYPE
        FROM
            CAR_RENTAL_COMPANY_RENTAL_HISTORY
    ) AS H
LEFT JOIN CAR_RENTAL_COMPANY_CAR C 
    ON H.CAR_ID = C.CAR_ID
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN P 
    ON H.DURATION_TYPE = P.DURATION_TYPE AND C.CAR_TYPE = P.CAR_TYPE
WHERE
    C.CAR_TYPE = "트럭"
ORDER BY
    FEE DESC, H.HISTORY_ID DESC