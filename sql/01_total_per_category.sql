SELECT 
    category,
    COUNT(*) as num_transactions,
    ROUND(SUM(amount), 2) as total_amount
FROM transactions
WHERE type = 'expense'
GROUP BY category
ORDER BY total_amount DESC;