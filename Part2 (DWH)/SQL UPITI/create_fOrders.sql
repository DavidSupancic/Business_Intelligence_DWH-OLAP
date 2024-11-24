CREATE TABLE fOrders(
	OrderDateID INT,
	RequiredDateID INT,
	ShippedDateID INT,
	OrderTimeID INT,
	RequiredTimeID INT,
	ShippedTimeID INT,
	DelayID INT,
	ShipperID INT,
	CustomerID VARCHAR(20),
	PaymentMethodID INT,

	OrderPrice DECIMAL(8,2),
	Freight DECIMAL(8,2)
);