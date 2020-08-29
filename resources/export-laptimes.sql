-- Export your times with SQLite
.open dirtrally-laptimes.db
attach 'dirtrally-lb.db' as base;
.separator ";"
.headers on
.once snapshot.csv
select t.name as Track,
		c.name as Car,
		strftime('%Y-%m-%d %H:%M:%S', datetime(l.timestamp, 'unixepoch', 'localtime')) as Date,
		strftime('%M:%f', l.time, 'unixepoch') as Time,
		l.topspeed as Topspeed
from base.tracks t, base.cars c, laptimes l
where t.id=l.track and c.id=l.car;
