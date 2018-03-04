select * from
(
  select
    total.day as day,
    round(errors.requests * 100 / cast(total.requests as numeric), 2) as perc
  from
    (
      select date(time) as day, count(*) as requests
      from log
      group by day
    ) as total
    inner join (
      select date(time) as day, count(*) as requests
      from log
      where status like '404 %'
      group by day
    ) as errors ON total.day = errors.day
) as log_perc
where perc > 1.0
order by perc desc
