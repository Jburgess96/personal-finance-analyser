SELECT 
    month_name,
    month,
    ROUND(SUM(CASE WHEN type = 'income' THEN amount ELSE 0 END), 2) as income,
    ROUND(SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END), 2) as expenses,
    ROUND(SUM(CASE WHEN type = 'income' THEN amount ELSE 0 END) - 
          SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END), 2) as savings,
    ROUND(
        (SUM(CASE WHEN type = 'income' THEN amount ELSE 0 END) - 
         SUM(CASE WHEN type = 'expense' THEN amount ELSE 0 END)) / 
         SUM(CASE WHEN type = 'income' THEN amount ELSE 0 END) * 100
    , 2) as savings_rate_pct
FROM transactions
GROUP BY month, month_name
ORDER BY month;