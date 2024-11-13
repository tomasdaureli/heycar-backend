ALTER TABLE vehicles ADD COLUMN user_id INT NULL;

ALTER TABLE vehicles ADD FOREIGN KEY (user_id) REFERENCES users(id);

-- PostgreSQL version
ALTER TABLE vehicles ADD COLUMN user_id INTEGER NULL;

ALTER TABLE vehicles
ADD CONSTRAINT fk_user_id
FOREIGN KEY (user_id) REFERENCES users(id);