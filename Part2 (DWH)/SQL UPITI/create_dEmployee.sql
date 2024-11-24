DROP TABLE dEmployee;

SELECT EmployeeID, LastName, FirstName, Title, TitleOfCourtesy, BirthDate, HireDate, [Address], HomePhone, Extension, Photo, Notes, ReportsTo,
		PostalCode, CityName, Region, Country
INTO dEmployee
FROM Employees LEFT JOIN City ON Employees.CityID = City.CityID;
