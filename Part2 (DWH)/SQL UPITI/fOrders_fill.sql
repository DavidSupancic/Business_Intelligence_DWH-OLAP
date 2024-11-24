SELECT CAST(OrderDate AS date) AS OrderDate, CAST(RequiredDate AS date) AS RequiredDate, CAST(ShippedDate AS date) AS ShippedDate, 
	CAST(OrderDate AS time) AS OrderTime, CAST(RequiredDate AS time) AS RequiredTime, CAST(ShippedDate AS time) AS ShippedTime, 
	Orders.CustomerID, ShipVia, PaymentMethod, Freight, SUM(UnitPrice * Quantity * (1-Discount)) AS OrderPrice
FROM Orders LEFT JOIN Customers ON Orders.CustomerID = Customers.CustomerID
LEFT JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID
GROUP BY OrderDate, RequiredDate, ShippedDate, 
	Orders.CustomerID, ShipVia, PaymentMethod, Freight