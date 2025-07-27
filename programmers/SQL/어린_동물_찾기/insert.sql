-- insert.sql (데이터 삽입용)
INSERT INTO
    ANIMAL_INS (ANIMAL_ID, ANIMAL_TYPE, DATETIME, INTAKE_CONDITION, NAME, SEX_UPON_INTAKE)
VALUES
    ('A365172', 'Dog', '2014-08-26 12:53:00', 'Normal', 'Diablo', 'Neutered Male'),
    ('A367012', 'Dog', '2015-09-16 09:06:00', 'Sick', 'Miller', 'Neutered Male'),
    ('A365302', 'Dog', '2017-01-08 16:34:00', 'Aged', 'Minnie', 'Spayed Female'),
    ('A381217', 'Dog', '2017-07-08 09:41:00', 'Sick', 'Cherokee', 'Neutered Male'),
    ('A400001', 'Cat', '2016-03-21 11:30:00', 'Normal', 'Leo', 'Intact Male'),
    ('A400002', 'Dog', '2016-05-11 14:20:00', 'Aged', 'Granny', 'Spayed Female'),
    ('A400003', 'Cat', '2016-07-09 13:45:00', 'Sick', 'Momo', 'Spayed Female'),
    ('A400004', 'Dog', '2016-08-02 10:10:00', 'Normal', NULL, 'Neutered Male'),
    ('A400005', 'Cat', '2016-08-10 12:00:00', 'Aged', 'Oldie', 'Neutered Male'),
    ('A400006', 'Dog', '2016-09-01 09:00:00', 'Injured', 'Buddy', 'Intact Male');