-- insert.sql (데이터 삽입용)
INSERT INTO
    ANIMAL_INS (ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE)
VALUES
    ('A365172', 'Dog', '2014-08-26 12:53:00', 'Normal', 'Diablo', 'Neutered Male'),
    ('A367012', 'Dog', '2015-09-16 09:06:00', 'Sick', 'Miller', 'Neutered Male'),
    ('A365302', 'Dog', '2017-01-08 16:34:00', 'Aged', 'Minnie', 'Spayed Female'),
    ('A381217', 'Dog', '2017-07-08 09:41:00', 'Sick', 'Cherokee', 'Neutered Male'),
    ('A390001', 'Cat', '2018-02-11 10:25:00', 'Normal', 'Tom', 'Intact Male'),
    ('A390002', 'Dog', '2018-02-12 11:10:00', 'Injured', 'Lucy', 'Spayed Female'),
    ('A390003', 'Cat', '2018-02-13 09:15:00', 'Sick', 'Luna', 'Spayed Female'),
    ('A390004', 'Dog', '2018-02-14 08:45:00', 'Sick', NULL, 'Neutered Male'),
    ('A390005', 'Dog', '2018-02-15 07:50:00', 'Normal', 'Buddy', 'Neutered Male'),
    ('A390006', 'Cat', '2018-02-16 12:00:00', 'Normal', 'Nabi', 'Intact Female');