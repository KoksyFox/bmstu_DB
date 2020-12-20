SELECT DISTINCT Visitors.name,Visitors.sex,Visitors.age, Abonements.type
    FROM Visitors JOIN Abonements ON Abonements.ID = Visitors.IDcard
    WHERE Visitors.sex = 'f' AND Visitors.age > 25