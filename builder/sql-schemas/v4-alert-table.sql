-- Active: 1729206605638@@127.0.0.1@33060@heycar
CREATE TABLE IF NOT EXISTS alerts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    part VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    severity VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fixed BOOLEAN NOT NULL,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles (id)
);