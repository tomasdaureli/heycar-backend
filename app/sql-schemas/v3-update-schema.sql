ALTER TABLE vehicles ADD COLUMN user_id INT NULL;

ALTER TABLE vehicles ADD FOREIGN KEY (user_id) REFERENCES users(id);