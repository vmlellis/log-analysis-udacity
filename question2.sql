select authors.name, count(*) as views
from
  authors
  inner join articles on authors.id = articles.author
  inner join log on concat('/article/', articles.slug) = log.path
where log.status like '200 %'
group by authors.name
order by views desc
