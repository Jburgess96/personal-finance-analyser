SELECT 
    category,
    COUNT(*) as num_transactions,
    ROUND(AVG(amount), 2) as avg_transaction,
    ROUND(MIN(amount), 2) as min_transaction,
    ROUND(MAX(amount), 2) as max_transaction
FROM transactions
WHERE type = 'expense'
GROUP BY category
ORDER BY avg_transaction DESC;