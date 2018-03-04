select articles.title, count(*) as views
from articles inner join log on concat('/article/', articles.slug) = log.path
where log.status like '200 %'
group by articles.title
order by views desc
limit 3
