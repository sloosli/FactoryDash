select * from kpe_fact;

select * from kpe_indexes;

select * from kpe_areas;

select * from shops;

delete from shops where 1=1
and shop_id = 106;
commit;

select * from aggregates;

select * from raw_swod rs ;

select * from aggregates_loadup_swod;

select * from res_groups;

alter table res_groups rename column res_group_id to res_group_Src_id;

alter table res_groups add res_group_id int;

update res_groups 
set res_group_id = nextval('base_seq')
where 1=1;

select * from resources;

alter table

alter table resources rename column res_id to res_Src_id;

alter table resources add res_id int;

update resources 
set res_id = nextval('base_seq')
where 1=1;

select * from raw_swod_det rsd ;

select * from aggregates_loadup_det;

update aggregates_loadup_det
set res_id = 

alter table aggregates
add shop_id int;

select a.agregate_id , a.agregate_name, a.shop_id -- , s.shop_id--, s.shop_name 
from aggregates a,
shops s 
where 1=1
and a.shop_id = s.shop_id
--and a.shop_id  = /*вставить текст*/
;


delete from aggregates a 
where 1=1
and shop_id = 106
;



update aggregates a
set shop_id = (select distinct s.shop_id 
from 
--aggregates a,
raw_swod rs,
shops s 
where 1=1
and a.agregate_name  = rs."name" 
and rs.shop_name = s.shop_name)
where 1=1;

--добавить в agregates shop_id
select distinct a.agregate_id, s.shop_id 
from 
aggregates a,
raw_swod rs,
shops s 
where 1=1
and a.agregate_name  = rs."name" 
and rs.shop_name = s.shop_name;

-----------------------------------
-----------------------------------
-----------------------------------

select a.agregate_id , a.agregate_name-- , s.shop_id--, s.shop_name 
from aggregates a,
shops s 
where 1=1
and a.shop_id = s.shop_id 
and a.agregate_id  = /*вставить текст*/;


select * from aggregates_loadup_det als ;


select * from kpe_fact;

select * from kpe_indexes;

select * from kpe_areas;

select * from shops;

select * from aggregates;

select * from aggregates_loadup_swod;

select * from res_groups;

select * from resources;

select plan_for_day,  avg(occupied_percentage) occ, avg(unavailable_percentage) unav
from aggregates_loadup_det
where 1=1
and res_id = 149
and dt_plan = date ('07.10.2021')
group by plan_for_day
order by plan_for_day
;

select ald.plan_for_day, ald.duration_in_days, 
ald.occupied_percentage occ, ald.unavailable_percentage unav
from aggregates_loadup_det ald
where 1=1
and res_id = 149
and dt_plan = date ('07.10.2021')
and duration_in_days = 1
order by plan_for_day
;

select * from resources ;


insert into aggregates_loadup_det 
select shop_id, res_id, c.day_date, 1 , occupied_percentage, unavailable_percentage, dt_plan
from aggregates_loadup_det ald,
calendar c
where 1=1
--and res_id = 150
and ald.duration_in_days > 1
--and dt_plan = date('07.10.2021')
and ald.plan_for_day <= c.day_date
and ald.plan_for_day + ald.duration_in_days > c.day_date
order by day_date
;

select * from raw_kpe;

select * from kpe_fact;

select * from kpe_areas;

select * from kpe_indexes;

select * from shops;

select * from aggregates;

select * from aggregates_loadup_swod;

select * from res_groups;

select * from resources;

select * from aggregates_loadup_det;

create unique index pk_kpe_fact
on kpe_fact(index_id, area_id, dt_metric);

create unique index pk_kpe_areas
on kpe_areas(area_id);

create unique index pk_shops
on shops(shop_id);

create unique index pk_aggregtes
on aggregates(agregate_id);

create unique index pk_aggregates_loadup_swod
on aggregates_loadup_swod(agregate_id, shop_id, dt_swod);

create unique index pk_res_groups
on res_groups(res_group_id);

create unique index pk_resources
on resources(res_id);

create unique index pk_aggregates_loadup_det
on aggregates_loadup_det(shop_id, res_id,plan_for_day, duration_in_days, dt_plan);





select ald.plan_for_day, res.res_name, 
ald.occupied_percentage occ, ald.unavailable_percentage unav
from aggregates_loadup_det ald,
resources res
where 1=1
and ald.res_id = 149
and ald.res_id = res.res_id
and ald.dt_plan = date ('07.10.2021')
and ald.plan_for_day >= date('01.11.2021')
and ald.plan_for_day <= date('01.12.2021') 
and ald.duration_in_days = 1
order by ald.plan_for_day
;


select * from raw_remains;

create table storages
as; 


select distinct id storage_src_id, name storage_name
from raw_remains;


select * from raw_kpe
where 1=1
and dt_metric = date('06.10.2021');


create table raw_kpi_limits
(area_name varchar(100), 
index_name varchar(200),
target_val float,
warning_val float,
if_more int);

select * from raw_kpi_limits;

select * from kpe_indexes ki ;

create table kpi_limits 
(index_id int, target_val int, warning_val int, if_more int);

select * from kpe_fact kf ;

alter table kpe_fact 
add st_color varchar(10);

update kpe_fact src
set st_color = (select case when if_more = 0
then 
case when val_percent < target_val then '#5ECD4C'
when val_percent < warning_val then '#FFC121'
else '#5ECD4C' end
when if_more = 1
then 
case when val_percent > target_val then '#5ECD4C'
when val_percent > warning_val then '#FFC121'
else '#5ECD4C' end
end
from kpe_fact kf ,
kpi_limits kl
where 1=1
and kf.index_id =src.index_id 
and kf.dt_metric = src.dt_metric 
and kf.index_id = kl.index_id)
where 1=1;

select * from kpi_limits;

select * from kpe_fact;

select kf.area_id, kf.val_percent, kf.dt_metric, ki.index_name, kf.st_color, kl.target_val, kl.warning_val, kl.if_more
from kpe_fact kf,
kpe_indexes ki,
kpi_limits kl
where 1=1
and kf.area_id = 82
and kf.index_id = ki.index_id 
and kf.dt_metric = (select max(dt_metric) from kpe_fact)
and kf.index_id = kl.index_id;

select * from kpe_indexes ki ;

select * from kpe_areas;

select * from raw
case when if_more = 0
then 
case when val_percent < target_val then 'gr'
when val_percent < warning_val then 'ye'
else 'rd' end
when if_more = 1
then 
case when val_percent > target_val then 'gr'
when val_percent > warning_val then 'ye'
else 'rd' end
end
from kpe_fact kf ,
kpi_limits kl
where 1=1
and kf.index_id = kl.index_id;

insert into kpi_limits
select ki.index_id, target_val, warning_val, if_more
from raw_kpi_limits rl ,
kpe_indexes ki ,
kpe_areas ka 
where 1=1
and rl.area_name = ka.area_name 
and rl.index_name = ki.index_name
and ka.area_id  = ki.area_id ;

select * from raw_res_storage rrs ;

select * from raw_remains rr ;

select * from shops s 
where 1=1;

select * from aggregates a 
where 1=1;

select * from kpi_limits;

update kpi_limits 
set warning_val = 3
where 1=1
and index_id = 102;


select * from kpe_indexes ki ;

select kf.area_id, kf.val_percent, kf.dt_metric, ki.index_name, kf.st_color, kl.target_val, kl.warning_val, kl.if_more
from kpe_fact kf,
kpe_indexes ki,
kpi_limits kl
where 1=1
and kf.area_id = 82
and kf.index_id = ki.index_id 
and kf.dt_metric = (select max(dt_metric) from kpe_fact)
and kf.index_id = kl.index_id;


(area_name, index_name, target_val, warning_val, if_more)

insert into raw_kpi_limits (area_name, index_name, target_val, warning_val, if_more) values('Прием заказов', 'Заказы не прошедшие проверку на техническую исполнимость', 1, 2, 0); 
insert into raw_kpi_limits (area_name, index_name, target_val, warning_val, if_more) values('Управление квотами', '% заполнения квот', 80, 72, 1); 
insert into raw_kpi_limits (area_name, index_name, target_val, warning_val, if_more) values('Календарное планирование', 'Загрузка оборудования', 85, 76.5, 1); 
insert into raw_kpi_limits (area_name, index_name, target_val, warning_val, if_more) values('Календарное планирование', 'Плановый OTIF', 90, 81, 1); 
insert into raw_kpi_limits (area_name, index_name, target_val, warning_val, if_more) values('Календарное планирование', 'Нарушение уровней запасов', 15, 16.5, 0); 
insert into raw_kpi_limits (area_name, index_name, target_val, warning_val, if_more) values('Календарное планирование', 'Загрузка кампаний', 80, 72, 1); 
insert into raw_kpi_limits (area_name, index_name, target_val, warning_val, if_more) values('Календарное планирование', 'Обязательный горячий посад, %', 80, 72, 1); 
insert into raw_kpi_limits (area_name, index_name, target_val, warning_val, if_more) values('Комбинирование заказов', 'Формирование и передача комбинаций', 90, 99, 0); 
insert into raw_kpi_limits (area_name, index_name, target_val, warning_val, if_more) values('Графикование конверторов', 'Составление и передача серий', 80, 72, 1); 
insert into raw_kpi_limits (area_name, index_name, target_val, warning_val, if_more) values('Графикование конверторов', 'Следование календарному плану', 70, 77, 0); 
insert into raw_kpi_limits (area_name, index_name, target_val, warning_val, if_more) values('Графикование горячих цехов', 'Составление и передача монтажей', 70, 77, 0); 
insert into raw_kpi_limits (area_name, index_name, target_val, warning_val, if_more) values('Графикование горячих цехов', 'Следование календарному плану', 70, 77, 0); 
insert into raw_kpi_limits (area_name, index_name, target_val, warning_val, if_more) values('Графикование горячих цехов', 'Уровень резервирования', 80, 72, 1); 
insert into raw_kpi_limits (area_name, index_name, target_val, warning_val, if_more) values('Составление сменно-суточных заданий', '% составления ССЗ', 50, 55, 0); 
insert into raw_kpi_limits (area_name, index_name, target_val, warning_val, if_more) values('Составление сменно-суточных заданий', 'Уровень резервирования', 80, 72, 1); 
insert into raw_kpi_limits (area_name, index_name, target_val, warning_val, if_more) values('Составление сменно-суточных заданий', '% составления заданий через контур системы', 80, 72, 1); 