SELECT 
    month,
    month_name,
    ROUND(SUM(CASE WHEN type = 'income' THEN amount ELSE 0 END), 2) as total_income,
    ROUND(SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END), 2) as total_expenses,
    ROUND(SUM(CASE WHEN type = 'income' THEN amount ELSE 0 END) - 
          SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END), 2) as net_position
FROM transactions
GROUP BY month, month_name
ORDER BY month;