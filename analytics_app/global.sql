--Global

select 
	date_trunc('month',rs.month)::date as month     --casting to date is important because the date range filter expects 'date' type
	,sum(revenue) as mrr 
	,sum(s.nb_seats) as nb_seats
	,count(distinct s.id_customer) as nb_customers 
from revenue_schedule rs 
left join subscriptions s on s.id = rs.id_subscription 
where 1 = 1
and date_trunc('month',rs.month) <= date_trunc('month', now())  
group by 1
order by 1 desc