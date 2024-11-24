CREATE TABLE fOrderItems(
	DateID INT,
	TimeID INT,
	ProductID INT,
	EmployeeID INT,
	PaymentMethodID INT,

	Discount DECIMAL(8,6),
	UnitPriceSold DECIMAL(8,2),
	UnitPricePaid DECIMAL(8,2),
	Quantity INT
);
