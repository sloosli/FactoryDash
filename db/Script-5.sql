drop table raw_kpe;

create table raw_kpe
(area_name varchar(200), --область
index_name varchar(200), --показатель
val varchar(10), --значение
dt_metric date --день
);

select * from raw_kpe;

drop table raw_swod;

select * from raw_swod;

create table raw_swod
(seq_id int,
name varchar(200),
shop_name varchar(100),
val varchar(10),
dt_swod date);

truncate table raw_swod_det;

create table raw_swod_det
(level_0 int,
shop_name varchar(100),
id varchar(100),
name varchar(100),
id_1 varchar(100),
name_1 varchar(100),
d_start date,
day int,
duration_id_days int,
occupied_percentage int,
unavailable_percentage float);


create table raw_res_storage
(has_constraint_violations bool,
storage_name varchar(200), 
has_constraint_power bool,
storage_id varchar(100),
input_sp varchar(100),
output_sp varchar(200),
dealer bool);

create table raw_remains
(id varchar(100),
name varchar(100),
duration int,
plan_dt date,
remains_lvl float,
overplan bool,
max_capacity int);


create sequence base_seq
increment by 1
minvalue 1
no maxvalue
start with 2;


