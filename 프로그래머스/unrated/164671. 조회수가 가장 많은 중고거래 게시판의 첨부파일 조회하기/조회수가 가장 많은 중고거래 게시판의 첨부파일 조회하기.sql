SELECT
    CONCAT_WS(
        "/"
        , "/home/grep/src"
        , B.BOARD_ID
        , CONCAT(F.FILE_ID, F.FILE_NAME, F.FILE_EXT)) AS FILE_PATH
FROM
    USED_GOODS_FILE F
LEFT JOIN
    USED_GOODS_BOARD B ON F.BOARD_ID = B.BOARD_ID
WHERE
    B.VIEWS IN (
        SELECT 
            MAX(VIEWS)
        FROM
            USED_GOODS_BOARD
    )
ORDER BY
    F.FILE_ID DESC