--Global MRR

select 
	date_trunc('month',rs.month)::date as month     --casting to date is important because the date range filter expects 'date' type
	,sum(revenue) as mrr 
from revenue_schedule rs 
where 1 = 1
and date_trunc('month',rs.month) <= date_trunc('month', now())  
group by 1
order by 1 desc 