SELECT dialogue, `name char`  FROM starwarsscr.dialogue
INNER JOIN `char`
ON `char_idchar` = `idchar`
WHERE `name char` = 'YODA'; 