-- Write your query below
select e.left_operand, e.operator, e.right_operand,
(case when e.operator='>' then e.l > e.r
when e.operator='<' then e.l<e.r
when e.operator='=' then e.l=e.r end) as value
from (select left_operand, (select value from variables where name=left_operand) as l, operator,
right_operand, (select value from variables where name=right_operand) as r
from expressions) as e;