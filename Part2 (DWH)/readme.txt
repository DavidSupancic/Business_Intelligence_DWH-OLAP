Napravljene su 2 činjenične tablice fOrders (cjelokupna narudžba) i fOrderItems (zasebni proizvodi u narudžbama), dimenzijske tablice dDate i dTime 
(te po 3 view-a za svaku od njih za order, required i shipped datetime), dDelay koji prikazuje vrstu kašnjenja, dProducts koji spaja tablice Products, Suppliers i Categories,
dEmployee koji spaja Employees i City, dCustomers koji spaja Customers i City, dShippers identičan Shippers-u te dPaymentMethod "izvučen" iz tablice Orders.  
Nisam stigao ispraviti neke NULL vrijednosti u dimenzijskim tablicama (iako znam da bih one koje su tipa VARCHAR trebao promijeniti u npr. "Unknown").

Tablice su napravljene u SSMS-u pomoću CREATE TABLE ..., sve osim dProducts, dEmployee i dCustomers koje su direktno napravljene pomoću LEFT JOIN-a iznad navedenih tablica te su im 
pomoću pythona dodani redovi za nepoznatu vrijednost. 