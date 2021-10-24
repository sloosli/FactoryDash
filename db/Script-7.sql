select * from raw_kpe;

create table kpe_areas
as select nextval('base_seq') area_id, gg.area_name 
from
(
select distinct area_name 
from raw_kpe) gg;

alter table kpe_areas 
rename column nextval to area_id ;

select * from raw_kpe;

select * from kpe_areas;

select * from kpe_indexes ;

select * from kpe_fact;


create table kpe_fact
as select ke.index_id, ke.area_id, to_number(replace (val,'%',''),'999') val_percent, dt_metric 
from raw_kpe rk ,
--kpe_areas ka,
kpe_indexes ke
where 1=1
and rk.index_name  = ke.index_name;


select * from raw_swod;


select ke.index_id, ke.area_id, to_number(replace (val,'%',''),'999'), dt_metric 
from raw_kpe rk ,
--kpe_areas ka,
kpe_indexes ke
where 1=1
and rk.index_name  = ke.index_name;

--drop table kpe_areas;

create table kpe_indexes
as 
select nextval('base_seq') index_id, gg.index_name, gg.area_id
from (select distinct index_name, ka.area_id
from raw_kpe rk,
kpe_areas ka 
where 1=1
and rk.area_name  = ka.area_name) gg;

select * from raw_swod_det rsd ;

select * from raw_res_storage rrs ;

select * from raw_remains rrs ;

select distinct shop_name from raw_swod_det;


select distinct index_name, ka.area_id
from raw_kpe rk,
kpe_areas ka 
where 1=1
and rk.area_name  = ka.area_name;


select * from raw_swod rs ;

select * 
from raw_swod_det rsd ;

create table aggregates
as select nextval('base_seq') agregate_id, gg.agregate_name 
from
(
select distinct name agregate_name 
from raw_swod) gg;



drop table aggregates_loadup_swod;
create table aggregates_loadup_swod
as
select ag.agregate_id, s.shop_id, to_number(substring(val,1,length(val)-1),'999') val_percent, dt_swod 
from raw_swod rs,
shops s,
aggregates ag
where 1=1
and rs."name"  = ag.agregate_name
and rs.shop_name  = s.shop_name;

select * from raw_swod_det rsd ;


create table aggregates_loadup_det
;

alter table raw_swod_det 
rename column duration_id_days to duration_in_days;

drop table aggregates_loadup_det;

create table aggregates_loadup_det
as
select --substring(shop_name,4) sh_name,
s.shop_id,
r.res_id,
--name_1 res_name,
d_start plan_for_day,
duration_in_days,
occupied_percentage,
unavailable_percentage,
dt_plan
--total_capacity 
--rsd.* 
from raw_swod_det rsd
, shops s
--, res_groups rg 
, resources r
where 1=1
and substring(rsd.shop_name,4) = s.shop_name 
and rsd.id_1 = r.res_src_id
--and rsd.id  = r.res_group_src_id
;

drop table kpe_fact;



create table res_groups
as
select distinct id res_group_id, name res_group_name
from raw_swod_det rsd ;

create table resources
as
select distinct rsd.id_1 res_id,rsd.name_1 res_name, rsd.id res_group_id
from raw_swod_det rsd ;


select distinct "day" , "Day" from raw_swod_det rsd ;


truncate table raw_swod_det ;

alter table raw_swod_det
drop column "Day";


alter table raw_swod_det 
add dt_plan date;



select * from raw_swod_det;
insert into raw_swod_Det (dt_plan)
values (current_date);

select * from raw_res_storage rrs ;

select * from raw_remains rr ;