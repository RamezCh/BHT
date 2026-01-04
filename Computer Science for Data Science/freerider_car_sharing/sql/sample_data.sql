USE FREERIDER_DB;
-- We use DELETE instead of DROP to keep the schema intact
DELETE FROM RESERVATION;
DELETE FROM VEHICLE;
DELETE FROM CUSTOMER;

INSERT INTO CUSTOMER (ID, NAME, CONTACTS, STATUS) VALUES
    (1, 'Meyer, Eric', 'eme22@gmail.com', 'Active'),
    (2, 'Sommer, Tina', '030 22458 29425', 'Active'),
    (3, 'Schulze, Tim', '+49 171 2358124', 'Active');

INSERT INTO VEHICLE (ID, MAKE, MODEL, SEATS, CATEGORY, POWER, STATUS) VALUES
    (1001, 'VW', 'Golf', 4, 'Sedan', 'Gasoline', 'Active'),
    (1002, 'VW', 'Golf', 4, 'Sedan', 'Hybrid', 'Active'),
    (1200, 'VW', 'Multivan Life', 8, 'Van', 'Gasoline', 'Active'),
    (3000, 'Mercedes', 'EQS', 4, 'Sedan', 'Electric', 'Active'),
    (6000, 'Tesla', 'Model 3', 4, 'Sedan', 'Electric', 'Active'),
    (6001, 'Tesla', 'Model S', 4, 'Sedan', 'Electric', 'Serviced');

INSERT INTO RESERVATION (ID, CUSTOMER_ID, VEHICLE_ID, BEGIN, END, PICKUP, DROPOFF, STATUS) VALUES
    (145373, 2, 6001, '2022-12-04 20:00:00', '2022-12-04 23:00:00', 'Berlin Wedding', 'Hamburg', 'Inquired'),
    (201235, 1, 1002, '2022-12-20 10:00:00', '2022-12-20 20:00:00', 'Berlin Wedding', 'Berlin Wedding', 'Booked'),
    (682351, 2, 6000, '2022-12-18 10:00:00', '2022-12-18 16:00:00', 'Potsdam', 'Teltow', 'Inquired');