DROP TABLE dProducts;

SELECT ProductID, ProductName, CountryOfOrigin, QuantityPerUnit, UnitPrice, UnitsInStock,
		CategoryName, [Description] AS CategoryDescription, Picture AS CategoryPicture,
		CompanyName AS SupplierCompanyName, ContactName AS SupplierContactName, ContactTitle AS SupplierContactTitle, [Address] AS SupplierAddress,
		Phone AS SupplierPhone, Fax AS SupplierFax, HomePage AS SupplierHomePage,
		PostalCode AS SupplierPostalCode, CityName AS SupplierCityName, Region AS SupplierRegion, Country AS SupplierCountry
INTO dProducts
FROM Products LEFT JOIN Categories ON Products.CategoryID = Categories.CategoryID
LEFT JOIN Suppliers ON Products.SupplierID = Suppliers.SupplierID
LEFT JOIN City ON Suppliers.CityID = City.CityID;