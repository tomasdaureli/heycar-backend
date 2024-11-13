-- MySQL version
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

-- PostgreSQL version
CREATE TABLE IF NOT EXISTS alerts (
    id SERIAL PRIMARY KEY,
    vehicle_id INTEGER NOT NULL,
    title VARCHAR(255) NOT NULL,
    part VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    severity VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    fixed BOOLEAN NOT NULL,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(id)
);