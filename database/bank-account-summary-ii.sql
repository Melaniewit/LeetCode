SELECT u.name, SUM(t.amount) AS BALANCE
FROM Transactions t
JOIN Users u ON t.account = u.account
GROUP BY t.account, u.name
HAVING BALANCE > 10000;
