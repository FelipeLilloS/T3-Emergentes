CREATE TABLE Admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
    );
)

CREATE TABLE Company (
    id INT AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(255) NOT NULL,
    company_api_key TEXT NOT NULL
    FOREIGN KEY (company_id) REFERENCES Location(company_id)
);

CREATE TABLE Location (
    company_id INT,
    location_id INT AUTO_INCREMENT PRIMARY KEY,
    location_name VARCHAR(255) NOT NULL,
    location_country VARCHAR(255) NOT NULL,
    location_city VARCHAR(255) NOT NULL,
    location_meta VARCHAR(255) NOT NULL,
    -- sensor_id INT,
    FOREIGN KEY (company_id) REFERENCES Company(id)
    -- FOREIGN KEY (sensor_id) REFERENCES Sensor(location_id)
);

CREATE TABLE Sensor (
    location_id INT,
    sensor_id INT NOT NULL PRIMARY KEY,
    sensor_name VARCHAR(255) NOT NULL,
    sensor_category VARCHAR(255) NOT NULL,
    sensor_meta VARCHAR(255) NOT NULL,
    FOREIGN KEY (location_id) REFERENCES Location(location_id)
);

CREATE TABLE SensorData (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sensor_id INT NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    dataJSON TEXT NOT NULL,
    FOREIGN KEY (sensor_id) REFERENCES Sensor(sensor_id)
);

-- Inserción de datos admin

INSERT INTO Admin (username, password) VALUES ('admin', 'admin');