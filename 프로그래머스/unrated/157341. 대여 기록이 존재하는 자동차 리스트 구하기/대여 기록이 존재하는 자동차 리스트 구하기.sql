SELECT
    DISTINCT A.CAR_ID
FROM
    CAR_RENTAL_COMPANY_RENTAL_HISTORY A
LEFT JOIN
    CAR_RENTAL_COMPANY_CAR B ON A.CAR_ID = B.CAR_ID
WHERE
    B.CAR_TYPE = "세단"
    AND MONTH(A.START_DATE) = "10"
ORDER BY
    A.CAR_ID DESC