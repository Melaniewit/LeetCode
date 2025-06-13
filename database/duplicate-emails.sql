# Write your MySQL query statement below
select 
email as  Email
from Person
-- GROUP BY 对某个字段进行分组后，所有的重复值确实会被合并成一个单独的组
group by email
--  GROUP BY 后，COUNT(email) 的计算是基于每个组里的行数。所以，它计算的是每个组里的行数，而不是整个表的原始行数
having count(email)>1
