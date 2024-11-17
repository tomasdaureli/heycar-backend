ALTER TABLE alerts RENAME TO failures;

ALTER TABLE failures
ADD COLUMN km INTEGER,
ADD COLUMN report_type VARCHAR(255),
ADD COLUMN solution VARCHAR(255);

ALTER TABLE failures DELETE COLUMN severity;

CREATE TABLE notifications (
    id SERIAL PRIMARY KEY,
    failure_id INTEGER NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (failure_id) REFERENCES failures (id)
);

ALTER TABLE notifications ADD COLUMN user_id INTEGER NOT NULL;

ALTER TABLE notifications
ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users (id);