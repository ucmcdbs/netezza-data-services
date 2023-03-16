create database dw;

-- drop table dw.store if exists;
-- drop table dw.sales if exists;

create table dw.store (id integer primary key, store_name text);
create table dw.sales (id integer primary key, transaction_date date, store_id integer references dw.store(id), amount numeric);

insert into dw.store values (1, 'GBM');
insert into dw.sales values (1, current_date, 1, 1000000);

select
    s.store_name   as store
  , sum(f.amount)  as sales
from dw.sales f
  inner join dw.store s on s.id = f.store_id
where s.id = 1
  and f.transaction_date between current_date - 7 and current_date
group by s.store_name
;
