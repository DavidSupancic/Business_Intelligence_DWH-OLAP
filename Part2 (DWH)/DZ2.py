import pyodbc
from datetime import datetime

#connect to DB
SERVER = ''
DATABASE = ''
USERNAME = ''
PASSWORD = ''
ENCRYPT = "no"

connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes; Encrypt={ENCRYPT}'

conn = pyodbc.connect(connectionString)

cursor = conn.cursor()

#dDate
query_1 = """INSERT INTO dDate (idDate, type_, formattedDate, dayOfWeekName, monthName_, isWorkday,
            isLastDayOfTheMonth, season, event_, isHoliday, holidayName) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

data_1 = [(-1, "Unknown", "?", "?", "?", "?", "?", "?", "?", "?", "?"), (-2, "Did not happen yet", "?", "?", "?", "?", "?", "?", "?", "?", "?")]  

for row in data_1:
    cursor.execute(query_1, row)

#all dates from years 2000-2024
query_2 = """INSERT INTO dDate (idDate, date_, type_, formattedDate, day_, month_, year_, quartal, dayOfWeek_, 
            dayOfWeekName, monthName_, isWorkday, isLastDayOfTheMonth, season, event_, isHoliday, holidayName) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
data_2 = []

leap_years = set([2000, 2004, 2008, 2012, 2016, 2020, 2024])
month_lengths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
months = ["January", "February", "March", "April", "May", 
          "June", "July", "August", "September", "October", "November", "December"]

holidays = {"0101":"New Year", "0106":"3 Kings Day", "0501":"Workers' Day", "0530":"Croatian National Day",
            "0622":"Anti-Fascist Struggle Day", "0805":"Dan pobjede i domovinske zahvalnosti, Dan hrvatskih branitelja",
            "0815":"Assumption of Mary", "1101":"All Saints' Day", "1118":"Dan sjećanja na žrtve Domovinskog rata",
            "1225":"Christmas", "1226":"Boxing Day"}

easter = set(["20000423", "20010415","20020331", "20030420", "20040411", "20050327", "20060416",
              "20070408", "20080323", "20090412", "20100404", "20110424", "20120408", "20130331", 
              "20140420", "20150405", "20160327", "20170416", "20180401", "20190421", "20200412", 
              "20210404", "20220417", "20230409", "20240331"])
easter_monday = set(["20000424", "20010416","20020401", "20030421", "20040412", "20050328", "20060417",
                     "20070409", "20080324", "20090413", "20100405", "20110425", "20120409", "20130401", 
                     "20140421", "20150406", "20160328", "20170417", "20180402", "20190422", "20200413", 
                     "20210405", "20220418", "20230410", "20240401"])
ascension_day = set(["20000622", "20010614", "20020530", "20030619", "20040610", "20050526", "20060615",
                     "20070607", "20080522", "20090611", "20100603", "20110623", "20120607", "20130530", 
                     "20140619", "20150604", "20160526", "20170615", "20180531", "20190620", "20200611", 
                     "20210603", "20220616", "20230608", "20240530" ])


day_of_week = 5 #day on 1/1/2000 was Saturday
season = "Winter"

for year in range (2000,2025):
    for month in range(1,13):
        #last day of the month
        if month != 2:
            month_len = month_lengths[month-1]
        else:
            if year not in leap_years:
                month_len = 28
            else:
                month_len = 29

        for day in range(1, month_len+1):    
            
            if month < 10:
                month_str = "0" + str(month)
            else:
                month_str = str(month)

            if day < 10:
                day_str = "0" + str(day)
            else:
                day_str = str(day)

            id = str(year) + month_str + day_str

            quartal = (month+2) // 3

            #last day of the month
            if month_len == day:
                last_day = "Yes"
            else:
                last_day = "No"

            #season
            if day == 21 and month == 3:
                season = "Spring"
            elif  day == 21 and month == 6:
                season = "Summer"
            elif day == 23 and month == 9:
                season = "Autumn"
            elif day == 21 and month==12:
                season = "Winter"

            #holiday
            is_holiday = "No"
            holiday_name = "Not a holiday"

            if id[4:] in holidays.keys():
                is_holiday = "Yes"
                holiday_name = holidays[id[4:]]
            
            if id in easter:
                if is_holiday == "No":
                    holiday_name = "Easter"
                else:
                    holiday_name += ", Easter"               
                is_holiday = "Yes"

            if id in easter_monday:
                if is_holiday == "No":
                    holiday_name = "Easter Monday"
                else:
                    holiday_name += ", Easter Monday"                    
                is_holiday = "Yes"

            if id in ascension_day:
                if is_holiday == "No":
                    holiday_name = "Ascension Day"
                else:
                    holiday_name += ", Ascension Day"
                is_holiday = "Yes"

            #work day
            if is_holiday == "No" and (day_of_week+1) <= 5:
                work_day = "Yes"
            else:
                work_day = "No"

            data_2.append([id, datetime(year, month, day), "Date", day_str+"."+month_str+"."+str(year)+".", day, month, year, quartal,
                           day_of_week+1, days_of_week[day_of_week], months[month-1], work_day, last_day,
                           season, "?", is_holiday, holiday_name                           
                           ])
            
            day_of_week = (day_of_week + 1) % 7


for row in data_2:
    cursor.execute(query_2, row)

#dTime
query_3 = "INSERT INTO dTime (idTimeOfDay, type_, formattedTime, period_) VALUES (?, ?, ?, ?)"

data_3 = [(-1, "Unknown", "?", "?"), (-2, "Did not happen yet", "?", "?")]  

for row in data_3:
    cursor.execute(query_3, row)


query_4 = """INSERT INTO dTime (idTimeOfDay, type_, secondsMidnight, minutesMidnight, formattedTime, 
            second_, minute_, hour_, period_) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""

data_4 = []

for hour in range (24):
    for minute in range(60):
        for second in range(60):
            id = hour*60*60 + minute*60 + second 

            if hour < 10:
                hour_str = "0" + str(hour)
            else:
                hour_str = str(hour)

            if minute < 10:
                minute_str = "0" + str(minute)
            else:
                minute_str = str(minute)

            if second < 10:
                second_str = "0" + str(second)
            else:
                second_str = str(second)           
            
            if hour >= 6 and hour < 18:
                period = "day"
            else:
                period = "night"

            data_4.append([id, "Normal", id, id//60, hour_str+":"+minute_str+":"+second_str,
                           second, minute, hour, period])


for row in data_4:
    cursor.execute(query_4, row)

#dProducts
query_5 = """INSERT INTO dProducts (ProductID, ProductName, CountryOfOrigin, QuantityPerUnit, UnitPrice, UnitsInStock,
		CategoryName, CategoryDescription, CategoryPicture, SupplierCompanyName, SupplierContactName, 
        SupplierContactTitle, SupplierAddress, SupplierPhone, SupplierFax, SupplierHomePage, SupplierPostalCode, 
        SupplierCityName, SupplierRegion, SupplierCountry) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

data_5 = [(-1, "Unknown", "Unknown", "Unknown", None, None, "Unknown", "Unknown", None,
           "Unknown", "Unknown", "Unknown", "Unknown", "Unknown", "Unknown", "Unknown", "Unknown", "Unknown", 
           "Unknown", "Unknown")]  

for row in data_5:
    cursor.execute(query_5, row)


#dEmployee
query_6 = """INSERT INTO dEmployee (EmployeeID, LastName, FirstName, Title, TitleOfCourtesy, BirthDate, HireDate, 
        Address, HomePhone, Extension, Photo, Notes, ReportsTo, PostalCode, CityName, Region, Country) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

data_6 = [(-1, "NA", "NA", "NA", "NA", None, None, "NA", "NA",
           "NA", None, "NA", None, "NA", "NA", "NA", "NA")]  

for row in data_6:
    cursor.execute(query_6, row)


#dCustomers
query_7 = """INSERT INTO dCustomers (CustomerID, CompanyName, ContactName, ContactTitle, Address, Phone, Fax,
		PostalCode, CityName, Region, Country) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

data_7 = [(-1, "Unknown", "Unknown", "Unknown", "Unknown", "Unknown", "Unknown", "Unknown", "Unknown",
           "Unknown", "Unknown")]  

for row in data_7:
    cursor.execute(query_7, row)

#dDelay
query_8 = "INSERT INTO dDelay (DelayID, DelayType) VALUES (?, ?)"

data_8 = [(-1, "Unknown"), (0, "No delay")]

for day in range(1, 365):
    if day <= 10:
        data_8.append((day, "Short Delay"))
    elif day <= 20:
        data_8.append((day, "Medium Delay"))
    else:
        data_8.append((day, "Long Delay"))

for row in data_8:
    cursor.execute(query_8, row)

#dPaymentMethod
payment_methods_dict = {}
payment_methods_dict["Unknown"] = -1
id_cnt = 0

query_9 = "INSERT INTO dPaymentMethod (PaymentMethodID, PaymentMethodName) VALUES (?, ?)"
data_9 = []

cursor.execute("SELECT DISTINCT PaymentMethod FROM Orders")

for row in cursor:
    if row[0] is not None and row[0] != "Csh":
        payment_methods_dict[row[0]] = id_cnt
        id_cnt += 1

for key in payment_methods_dict.keys():
    data_9.append((payment_methods_dict[key], key))

for row in data_9:
    cursor.execute(query_9, row)

#fOrders
query_10 = """INSERT INTO fOrders (OrderDateID, RequiredDateID, ShippedDateID, OrderTimeID, RequiredTimeID, 
            ShippedTimeID, DelayID, ShipperID, CustomerID, PaymentMethodID,
            OrderPrice, Freight) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

data_10 = []

cursor.execute("""SELECT CAST(OrderDate AS date) AS OrderDate, CAST(RequiredDate AS date) AS RequiredDate, CAST(ShippedDate AS date) AS ShippedDate, 
	CAST(OrderDate AS time) AS OrderTime, CAST(RequiredDate AS time) AS RequiredTime, CAST(ShippedDate AS time) AS ShippedTime, 
	Orders.CustomerID, ShipVia, PaymentMethod, Freight, SUM(UnitPrice * Quantity * (1-Discount)) AS OrderPrice
    FROM Orders LEFT JOIN Customers ON Orders.CustomerID = Customers.CustomerID
    LEFT JOIN OrderItems ON Orders.OrderID = OrderItems.OrderID
    GROUP BY OrderDate, RequiredDate, ShippedDate, Orders.CustomerID, ShipVia, PaymentMethod, Freight""")

for row in cursor:
    #date and time
    if row[0] == None:
        order_date_id = -1
    else:
        order_date_id = str(row[0]).replace("-","",2)
    
    if row[1] == None:
        req_date_id = -1
    else:
        req_date_id = str(row[1]).replace("-","",2)

    if row[2] == None:
        ship_date_id = -1
    else:
        ship_date_id = str(row[2]).replace("-","",2)

    if row[3] == None:
        order_time_id = -1
    else:
        list1 = str(row[3])[0:9].split(":")
        order_time_id = 3600*int(list1[0]) + 60*int(list1[1]) + int(list1[2])

    if row[4] == None:
        req_time_id = -1
    else:
        list1 = str(row[4])[0:9].split(":")
        req_time_id = 3600*int(list1[0]) + 60*int(list1[1]) + int(list1[2])

    if row[5] == None:
        ship_time_id = -1
    else:
        list1 = str(row[5])[0:9].split(":")
        ship_time_id = 3600*int(list1[0]) + 60*int(list1[1]) + int(list1[2])
    
    if req_date_id == -1 or ship_date_id == -1:
        delay_id = -1
    else:
        difference = row[2] - row[1]
        delay_id = difference.days

        if delay_id < 0:
            delay_id = 0



    #surrogate keys
    if row[6] == None:
        customer_id = -1
    else:
        customer_id = row[6]

    if row[7] == None:
        shipper_id = -1
    else:    
        shipper_id = row[7]

    if row[8] == None:
        payment_id = -1
    else: 
        if row[8] == "Csh":
            row[8] = "Cash"
        payment_id = payment_methods_dict[row[8]]

    #measures
    if row[9] == None:
        freight = None
    else:
        freight = row[9]

    if row[10] == None:
        order_price = None
    else:
        order_price = row[10]       

    data_10.append((order_date_id, req_date_id, ship_date_id, order_time_id, req_time_id, ship_time_id,
                    delay_id, shipper_id, customer_id, payment_id, order_price, freight))

for row in data_10:

    cursor.execute(query_10, row)


#fOrderItems
query_11 = """INSERT INTO fOrderItems (DateID, TimeID, ProductID, EmployeeID, PaymentMethodID,
            Discount, UnitPriceSold, UnitPricePaid, Quantity) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""

data_11 = []

cursor.execute("""SELECT CAST(OrderDate AS date) AS OrderDate, CAST(OrderDate AS time) AS OrderTime,
		OrderItems.ProductID, Orders.EmployeeID, Orders.PaymentMethod, Discount, 
		OrderItems.UnitPrice AS UnitPriceSold, Products.UnitPrice AS UnitPricePaid, Quantity
        FROM OrderItems LEFT JOIN Products ON OrderItems.ProductID = Products.ProductID
        LEFT JOIN Orders ON OrderItems.OrderID = Orders.OrderID
        LEFT JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID""")

for row in cursor:
    if row[0] == None:
        date_id = -1
    else:
        date_id = str(row[0]).replace("-","",2)
    
    if row[1] == None:
        time_id = -1
    else:
        list1 = str(row[1])[0:9].split(":")
        time_id = 3600*int(list1[0]) + 60*int(list1[1]) + int(list1[2])
    
    product_id = row[2]
    employee_id = row[3]

    if row[4] == None:
        payment_id = -1
    else: 
        payment_id = payment_methods_dict[row[4]]
    
    #measures
    if row[5] != None:
        discount = row[5]
    if row[6] != None:
        unit_price_sold = row[6]

    unit_price_paid = row[7]
    quantity = row[8]

    data_11.append((date_id, time_id, product_id, employee_id, payment_id, 
                    discount, unit_price_sold, unit_price_paid, quantity))

for row in data_11:
    cursor.execute(query_11, row)



conn.commit()

cursor.close()
conn.close()

