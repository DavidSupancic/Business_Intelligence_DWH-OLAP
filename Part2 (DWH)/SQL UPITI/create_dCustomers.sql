DROP TABLE dCustomers;

SELECT CustomerID, CompanyName, ContactName, ContactTitle, [Address], Phone, Fax,
		PostalCode, CityName, Region, Country
INTO dCustomers
FROM Customers LEFT JOIN City ON Customers.CityID = City.CityID;