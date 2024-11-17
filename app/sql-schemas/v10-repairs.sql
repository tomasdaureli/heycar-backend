CREATE TABLE repairs (
    "id" SERIAL PRIMARY KEY,
    "date" DATE NOT NULL,
    "part" VARCHAR(255) NOT NULL,
    "description" TEXT NOT NULL,
    "cost" DECIMAL(10, 2) NOT NULL,
    "repair_vehicle_id" INT NOT NULL,
    "repair_user_id" INT NOT NULL,
    "created_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY ("repair_vehicle_id") REFERENCES vehicles ("id"),
    FOREIGN KEY ("repair_user_id") REFERENCES users ("id")
);

ALTER TABLE repairs
ADD COLUMN "type" VARCHAR(255) NOT NULL DEFAULT 'repair';