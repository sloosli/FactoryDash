-- Drop table

-- DROP TABLE public.aggregates;

CREATE TABLE public.aggregates (
	agregate_id int8 NULL,
	agregate_name varchar(200) NULL,
	shop_id int4 NULL
);
CREATE UNIQUE INDEX pk_aggregtes ON public.aggregates (agregate_id);


-- Drop table

-- DROP TABLE public.aggregates_loadup_det;

CREATE TABLE public.aggregates_loadup_det (
	shop_id int8 NULL,
	res_id int4 NULL,
	plan_for_day date NULL,
	duration_in_days int4 NULL,
	occupied_percentage int4 NULL,
	unavailable_percentage float8 NULL,
	dt_plan date NULL
);
CREATE UNIQUE INDEX pk_aggregates_loadup_det ON public.aggregates_loadup_det (shop_id,res_id,plan_for_day,duration_in_days,dt_plan);


CREATE OR REPLACE PROCEDURE public.fill_calendar(date)
 LANGUAGE plpgsql
AS $procedure$declare
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
	
end;$procedure$
;


-- Drop table

-- DROP TABLE public.aggregates_loadup_swod;

CREATE TABLE public.aggregates_loadup_swod (
	agregate_id int8 NULL,
	shop_id int8 NULL,
	val_percent numeric NULL,
	dt_swod date NULL
);
CREATE UNIQUE INDEX pk_aggregates_loadup_swod ON public.aggregates_loadup_swod (agregate_id,shop_id,dt_swod);


-- Drop table

-- DROP TABLE public.calendar;

CREATE TABLE public.calendar (
	day_date date NULL
);


-- public.kpe_areas definition

-- Drop table

-- DROP TABLE public.kpe_areas;

CREATE TABLE public.kpe_areas (
	area_id int8 NULL,
	area_name varchar(200) NULL
);
CREATE UNIQUE INDEX pk_kpe_areas ON public.kpe_areas USING btree (area_id);

-- public.kpe_fact definition

-- Drop table

-- DROP TABLE public.kpe_fact;

CREATE TABLE public.kpe_fact (
	index_id int8 NULL,
	area_id int8 NULL,
	val_percent numeric NULL,
	dt_metric date NULL,
	st_color varchar(10) NULL
);
CREATE UNIQUE INDEX pk_kpe_fact ON public.kpe_fact USING btree (index_id, area_id, dt_metric);

-- public.kpe_indexes definition

-- Drop table

-- DROP TABLE public.kpe_indexes;

CREATE TABLE public.kpe_indexes (
	index_id int8 NULL,
	index_name varchar(200) NULL,
	area_id int8 NULL
);

-- public.kpi_limits definition

-- Drop table

-- DROP TABLE public.kpi_limits;

CREATE TABLE public.kpi_limits (
	index_id int4 NULL,
	target_val int4 NULL,
	warning_val int4 NULL,
	if_more int4 NULL
);

-- public.raw_kpe definition

-- Drop table

-- DROP TABLE public.raw_kpe;

CREATE TABLE public.raw_kpe (
	area_name varchar(200) NULL,
	index_name varchar(200) NULL,
	val varchar(10) NULL,
	dt_metric date NULL
);

-- public.raw_kpi_limits definition

-- Drop table

-- DROP TABLE public.raw_kpi_limits;

CREATE TABLE public.raw_kpi_limits (
	area_name varchar(100) NULL,
	index_name varchar(200) NULL,
	target_val float8 NULL,
	warning_val float8 NULL,
	if_more int4 NULL
);

-- public.raw_remains definition

-- Drop table

-- DROP TABLE public.raw_remains;

CREATE TABLE public.raw_remains (
	id varchar(100) NULL,
	"name" varchar(100) NULL,
	duration int4 NULL,
	plan_dt date NULL,
	remains_lvl float8 NULL,
	overplan bool NULL,
	max_capacity int4 NULL
);

-- public.raw_res_storage definition

-- Drop table

-- DROP TABLE public.raw_res_storage;

CREATE TABLE public.raw_res_storage (
	has_constraint_violations bool NULL,
	storage_name varchar(200) NULL,
	has_constraint_power bool NULL,
	storage_id varchar(100) NULL,
	input_sp varchar(100) NULL,
	output_sp varchar(200) NULL,
	dealer bool NULL
);

-- public.raw_swod definition

-- Drop table

-- DROP TABLE public.raw_swod;

CREATE TABLE public.raw_swod (
	seq_id int4 NULL,
	"name" varchar(200) NULL,
	shop_name varchar(100) NULL,
	val varchar(10) NULL,
	dt_swod date NULL
);

-- public.raw_swod_det definition

-- Drop table

-- DROP TABLE public.raw_swod_det;

CREATE TABLE public.raw_swod_det (
	level_0 int4 NULL,
	shop_name varchar(100) NULL,
	id varchar(100) NULL,
	"name" varchar(100) NULL,
	id_1 varchar(100) NULL,
	name_1 varchar(100) NULL,
	d_start date NULL,
	"day" int4 NULL,
	duration_in_days int4 NULL,
	occupied_percentage int4 NULL,
	unavailable_percentage float8 NULL,
	total_capacity varchar(8) NULL,
	dt_plan date NULL
);

-- public.res_groups definition

-- Drop table

-- DROP TABLE public.res_groups;

CREATE TABLE public.res_groups (
	res_group_src_id varchar(100) NULL,
	res_group_name varchar(100) NULL,
	res_group_id int4 NULL
);
CREATE UNIQUE INDEX pk_res_groups ON public.res_groups USING btree (res_group_id);

-- public.resources definition

-- Drop table

-- DROP TABLE public.resources;

CREATE TABLE public.resources (
	res_src_id varchar(100) NULL,
	res_name varchar(100) NULL,
	res_group_id varchar(100) NULL,
	res_id int4 NULL,
	shop_id int4 NULL
);
CREATE UNIQUE INDEX pk_resources ON public.resources USING btree (res_id);

-- public.shops definition

-- Drop table

-- DROP TABLE public.shops;

CREATE TABLE public.shops (
	shop_id int8 NULL,
	shop_name varchar(100) NULL
);
CREATE UNIQUE INDEX pk_shops ON public.shops USING btree (shop_id);

-- public.tmp_rec definition

-- Drop table

-- DROP TABLE public.tmp_rec;

CREATE TABLE public.tmp_rec (
	has_constraint_violations bool NULL,
	agr_name varchar(200) NULL,
	has_constraint_power bool NULL,
	agr_src_id varchar(100) NULL,
	input_sp text NULL,
	output_sp text NULL,
	dealer bool NULL
);