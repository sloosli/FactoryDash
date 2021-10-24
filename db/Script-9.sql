create table calendar
(day_date date);

create or replace procedure fill_calendar
(date)
language plpgsql as 
$$declare
date_st alias for $1;
date_end date := date('01.01.2030');
date_cur date;
rec RECORD;
begin
	date_cur := date_st;
	while date_cur < date_end
	loop
		insert into calendar 
		values(date_cur);
		
		commit;
	
		date_cur := date_cur+1;
	end loop;
	
end;$$
;

call fill_calendar(date('01.01.2020'));


select min(day_date), max(day_date) from calendar;


select ke.index_id, ke.area_id, to_number(replace (val,'%',''),'999') val_percent, dt_metric 
from raw_kpe rk ,
--kpe_areas ka,
kpe_indexes ke
where 1=1
and rk.index_name  = ke.index_name
and ke.index_id = 95;

select * from kpe_indexes ke 
where 1=1
and ke.index_name = 'Следование календарному плану';

select distinct area_name , index_name from raw_kpe;