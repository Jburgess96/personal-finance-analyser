SELECT 
    month_name,
    ROUND(SUM(amount), 2) as total_spent,
    COUNT(*) as num_transactions
FROM transactions
WHERE type = 'expense'
GROUP BY month, month_name
ORDER BY total_spent DESC;