SELECT CAST(OrderDate AS date) AS OrderDate, CAST(OrderDate AS time) AS OrderTime,
		OrderItems.ProductID, Orders.EmployeeID, Orders.PaymentMethod, Discount, 
		OrderItems.UnitPrice AS UnitPriceSold, Products.UnitPrice AS UnitPricePaid, Quantity
FROM OrderItems LEFT JOIN Products ON OrderItems.ProductID = Products.ProductID
LEFT JOIN Orders ON OrderItems.OrderID = Orders.OrderID
LEFT JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID