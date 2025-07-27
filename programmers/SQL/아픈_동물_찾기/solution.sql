-- solution.sql (정답 쿼리 작성용)
SELECT
    ANIMAL_ID,
    NAME
FROM
    ANIMAL_INS
WHERE
    INTAKE_CONDITION = 'Sick'
ORDER BY
    ANIMAL_ID ASC;