# Freerider Car-Sharing Database Tutorial

This project demonstrates how to build and deploy a relational database for a car-sharing service using Docker and MySQL 8.4.

## 1. Project Overview
The system manages three core entities:
* **CUSTOMER**: People registered to use the service.
* **VEHICLE**: The fleet of cars available for rent.
* **RESERVATION**: The connection between a customer and a vehicle.

![ERD_FreeRide](/docs/freerider_ERD.png)

## 2. Deployment Steps

### Step 1: Build and Run
```cmd
docker build -t freerider-mysqld-img:1.0 .
docker volume create mysqld-vol
docker run --name freerider-mysqld -d -p 3306:3306 -v mysqld-vol:/var/lib/mysql freerider-mysqld-img:1.0
```

### Step 2: Load Data
```cmd
docker exec -i freerider-mysqld mysql -ufreerider -pfree.ride FREERIDER_DB < sample_data.sql
```

## 3. Testing Persistence (Volume Check)
To verify that the **Volume** is working, you must delete the container and recreate it. If the data is still there, the volume successfully stored it externally.

### Option A: Via Command Line
1. **Remove the container:** `docker rm -f freerider-mysqld`
2. **Re-run the container:** Use the same `docker run` command from Step 1.
3. **Verify:** Run a `SELECT` query. You will see the data exists without needing to reload `sample_data.sql`.

### Option B: Via Docker Desktop Dashboard
1. Open the **Containers** tab.
2. Find `freerider-mysqld`.
3. Click the **Delete (Trash can)** icon.
4. Go to the **Volumes** tab; you will notice `mysqld-vol` still exists.
5. Re-run the container from the terminal. The data will be automatically restored from the volume.

## 4. Technical Discussions

### Race Conditions
A **Race Condition** occurs when two customers try to book the same car at the same millisecond. 

If the database doesn't use proper locking, both might be told the car is "Available," leading to a double-booking. **Solutions** include using `START TRANSACTION` and `SELECT ... FOR UPDATE`.

### ACID Properties

* **Atomicity**: The reservation is saved completely or not at all.
* **Consistency**: Foreign keys prevent "ghost" reservations for non-existent cars.
* **Isolation**: One user's booking process doesn't interfere with another's.
* **Durability**: Once saved, data stays in `mysqld-vol` even after a crash or deletion.

## 5. Verification
```cmd
docker exec -it freerider-mysqld mysql -ufreerider -pfree.ride FREERIDER_DB -e "SELECT * FROM CUSTOMER; SELECT * FROM VEHICLE; SELECT * FROM RESERVATION;"
```