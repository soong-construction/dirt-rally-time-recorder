-- Export your times with SQLite  
.open dirtrally-laptimes.db
attach 'dirtrally-lb.db' as base;
.once snapshot.csv
select t.name, 
		c.name, 
		strftime('%Y-%m-%d %H:%M:%S', datetime(l.timestamp, 'unixepoch', 'localtime')) as timestamp,
		strftime('%M:%f', l.time, 'unixepoch'),
		l.topspeed
from base.tracks t, base.cars c, laptimes l
where t.id=l.track and c.id=l.car;
