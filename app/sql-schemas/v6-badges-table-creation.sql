CREATE TABLE IF NOT EXISTS badges (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    score INT DEFAULT 0,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

ALTER TABLE users ADD COLUMN points INT NULL;
