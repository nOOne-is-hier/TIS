-- solution.sql (정답 쿼리 작성용)
SELECT
    COUNT(*) AS USERS
FROM
    USER_INFO
WHERE
    YEAR (JOINED) = '2021'
    AND AGE BETWEEN 20 AND 29;