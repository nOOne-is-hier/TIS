-- insert.sql (데이터 삽입용)
INSERT INTO
    ANIMAL_INS (ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE)
VALUES
    ('A349996', 'Cat', '2018-01-22 14:32:00', 'Normal', 'Sugar', 'Neutered Male'),
    ('A350276', 'Cat', '2018-01-23 14:32:00', 'Normal', 'Jewel', 'Spayed Female'),
    ('A350375', 'Cat', '2018-01-24 14:32:00', 'Normal', 'Meo', 'Neutered Male'),
    ('A352555', 'Dog', '2018-01-25 14:32:00', 'Normal', 'Harley', 'Spayed Female'),
    ('A352713', 'Dog', '2018-01-26 14:32:00', 'Normal', 'Gia', 'Spayed Female'),
    (
        'A352872',
        'Dog',
        '2018-01-27 14:32:00',
        'Normal',
        'Peanutbutter',
        'Spayed Female'
    ),
    ('A353259', 'Dog', '2018-01-28 14:32:00', 'Normal', 'Bj', 'Neutered Male');