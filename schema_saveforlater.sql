golfcourse=# CREATE TABLE users (
   id SERIAL PRIMARY KEY,
   username VARCHAR(50) UNIQUE NOT NULL,
   password VARCHAR(100) NOT NULL,
   email VARCHAR(100) UNIQUE NOT NULL,
   created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
CREATE TABLE
golfcourse=# CREATE TABLE tee_times (
   id SERIAL PRIMARY KEY,
   time_slot TIME NOT NULL,
   date DATE NOT NULL,
   num_players INT NOT NULL,
   is_booked BOOLEAN NOT NULL DEFAULT FALSE,
   created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
CREATE TABLE
golfcourse=# CREATE TABLE bookings (
   id SERIAL PRIMARY KEY,
   user_id INT NOT NULL REFERENCES users(id),
   tee_time_id INT NOT NULL REFERENCES tee_times(id),
   created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
CREATE TABLE
golfcourse=# CREATE TABLE employees (
   id SERIAL PRIMARY KEY,
   username VARCHAR(50) UNIQUE NOT NULL,
   password VARCHAR(100) NOT NULL,
   job_title VARCHAR(100) NOT NULL,
   created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
CREATE TABLE
golfcourse=# CREATE TABLE schedule (
   id SERIAL PRIMARY KEY,
   employee_id INT NOT NULL REFERENCES employees(id),
   shift_start TIME NOT NULL,
   shift_end TIME NOT NULL,
   created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
CREATE TABLE
golfcourse=# CREATE TABLE customers (
   id SERIAL PRIMARY KEY,
   name VARCHAR(100) NOT NULL,
   email VARCHAR(100) UNIQUE NOT NULL,
   phone VARCHAR(20) NOT NULL,
   created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
