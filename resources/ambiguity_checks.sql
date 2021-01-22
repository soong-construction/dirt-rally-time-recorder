-- Cars with identical RPMs
select c1.name, c2.name
from cars c1 join cars c2 
on c1.id < c2.id and c1.idlerpm = c2.idlerpm and c1.maxrpm = c2.maxrpm
join controls co1 on c1.id = co1.id
join controls co2 on c2.id = co2.id
-- with equal top gear
and co1.topgear = co2.topgear
-- with equal shifting
-- and co1.shifting = co2.shifting
;

-- Tracks with similar length
select * 
from tracks t1 
inner join tracks t2 on abs(t1.length-t2.length) < .001 
where t1.id < t2.id;