-- insert.sql (데이터 삽입용)
INSERT INTO
    DEVELOPER_INFOS (ID, FIRST_NAME, LAST_NAME, EMAIL, SKILL_1, SKILL_2, SKILL_3)
VALUES
    (
        'D165',
        'Jerami',
        'Edwards',
        'jerami_edwards@grepp.co',
        'Java',
        'JavaScript',
        'Python'
    ),
    ('D161', 'Carsen', 'Garza', 'carsen_garza@grepp.co', 'React', NULL, NULL),
    ('D164', 'Kelly', 'Grant', 'kelly_grant@grepp.co', 'C#', NULL, NULL),
    ('D163', 'Luka', 'Cory', 'luka_cory@grepp.co', 'Node.js', NULL, NULL),
    (
        'D162',
        'Cade',
        'Cunningham',
        'cade_cunningham@grepp.co',
        'Vue',
        'C++',
        'Python'
    );