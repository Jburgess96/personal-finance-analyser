SELECT 
    date,
    description,
    category,
    amount
FROM transactions
WHERE type = 'expense'
ORDER BY amount DESC
LIMIT 10;