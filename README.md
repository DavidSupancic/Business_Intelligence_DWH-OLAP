# Business_Intelligence_DWH-OLAP

## OVERVIEW
Business_Intelligence_DWH-OLAP is a Business Intelligence (BI) project that focuses on designing and implementing a Data Warehouse (DWH) and Online Analytical Processing (OLAP) solutions. The project uses SQL Server Management Studio (SSMS), Visual Studio, Python and SQL to create a system capable of enabling powerful insights and analytics. By transforming raw operational data into a structured and optimized data warehouse, this project empowers users to explore and analyze business data effectively.

## KEY FEATURES
Development of a Data Warehouse (DWH) with two fact tables of different granulations:
fOrders: Aggregated data for orders.
fOrderItems: Detailed data at the item level for each order.
Creation of multiple dimension tables to support insightful analysis:
dTime: Time-specific details (hour, minute, second).
dDate: Date-specific details (day, week, month, year).
dProducts: Comprehensive product information.
dDelay: Tracking shipment delays.
dShippers: Information about shippers and carriers.
dCustomers: Customer demographics and preferences.
dEmployee: Employee-related data.
dPaymentMethod: Payment method types.
Implementation of OLAP cubes to enable multidimensional analysis.
Application of ETL processes (Extract, Transform, Load) for data preparation and cleaning.
Use of SSMS for database design and management.
Integration with Visual Studio for creating OLAP cubes and designing schema.
Scripting with Python to automate data transformations and validations.

## TECHNOLOGIES USED
SQL Server Management Studio (SSMS): For DWH creation and data management.
Visual Studio: For designing OLAP cubes and schema modeling.
SQL Server Analysis Services (SSAS): For building and deploying OLAP cubes.
Python: For automating ETL processes and advanced data handling.
SQL: For writing complex queries, creating tables, and performing transformations.

## PROJECT OBJECTIVES
To create a scalable Data Warehouse that stores and organizes data efficiently.
To implement an OLAP solution that supports multidimensional analysis and enhances decision-making.
To enable the integration of multiple data sources into a unified system.
To provide rich analytical capabilities for key business insights in domains such as sales, shipping, and customer behavior.

## BENEFITS
Streamlined access to consolidated business data.
Efficient multidimensional analysis through OLAP cubes.
Enhanced decision-making with actionable insights from data.
Support for advanced reporting and dashboards using BI tools.
Flexible granularity for both high-level and detailed analysis.

## KEY BUSINESS INTELLIGENCE CONCEPTS
Data Warehouse (DWH): A centralized repository for structured data optimized for query and analysis.
ETL: A pipeline to extract data from sources, transform it into usable formats, and load it into the DWH.
OLAP Cubes: Multidimensional data structures that support quick analysis of large datasets.
- Built using SSAS for optimized analytical processing
- Implemented multiple measure groups for various business metrics
- Created calculated members for advanced business calculations
Granularity: The level of detail in stored data, with fOrders for high-level metrics and fOrderItems for granular insights.
