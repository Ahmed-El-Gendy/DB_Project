CREATE database IF not hotel;
CREATE TABLE bill (
  id INT NOT NULL AUTO_INCREMENT,
  total_price INT DEFAULT NULL,
  guest_id INT DEFAULT NULL,
  date_of_check_out DATETIME DEFAULT NULL,
  receptionist_id INT DEFAULT NULL,
  PRIMARY KEY (id)
);

-- Insert data into the 'bill' table
INSERT INTO bill (total_price, guest_id, date_of_check_out, receptionist_id) VALUES
(200, 1, '2024-04-24 02:41:56', 2),
(200, 1, '2024-04-24 05:41:47', 2),
(650, 1, '2024-04-24 05:45:49', 2),
(650, 1, '2024-04-24 05:48:28', 2),
(350, 1, '2024-04-24 05:56:44', 2),
(260, 1, '2024-04-24 12:04:49', 2),
(260, 100, '2024-04-25 13:29:20', 2),
(290, 101, '2024-04-25 13:51:39', 2),
(200, 101, '2024-04-25 13:55:56', 2),
(800, 100, '2024-04-25 14:00:10', 2),
(400, 1, '2024-04-25 18:25:27', 2),
(150, 100, '2024-04-25 18:25:40', 2),
(200, 100, '2024-04-25 18:25:43', 2);

-- Drop and create the 'employee' table
CREATE TABLE employee (
  id INT NOT NULL,
  age INT DEFAULT NULL,
  nationality VARCHAR(250) DEFAULT NULL,
  job VARCHAR(250) DEFAULT NULL,
  salary INT DEFAULT NULL,
  manager_id INT DEFAULT NULL,
  name VARCHAR(250) DEFAULT NULL,
  PRIMARY KEY (id)
);

-- Insert data into the 'employee' table
INSERT INTO employee (id, age, nationality, job, salary, manager_id, name) VALUES
(1, 30, 'egyptian', 'boss', 11000, 1, 'Ramy Rashad'),
(2, 25, 'egyptian', 'receptionist', 5000, 1, 'Ahmed'),
(3, 21, 'egyptian', 'chef', 9000, 1, 'Hassan'),
(4, 21, 'egyptian', 'receptionist', 5000, 1, 'Ahmed Abbas'),
(45, 21, 'egyptian', 'receptionist', 120, 1, 'Saged');

-- Drop and create the 'feedback' table
CREATE TABLE feedback (
  id INT NOT NULL AUTO_INCREMENT,
  opinion VARCHAR(255) DEFAULT NULL,
  rate INT DEFAULT NULL,
  guest_id INT DEFAULT NULL,
  PRIMARY KEY (id),
  CHECK (rate BETWEEN 0 AND 10)
);

-- Insert data into the 'feedback' table
INSERT INTO feedback (opinion, rate, guest_id) VALUES
('well done', 10, 1),
('good', 10, 100);

-- Drop and create the 'guest' table
CREATE TABLE guest (
  id INT NOT NULL,
  name VARCHAR(120) DEFAULT NULL,
  age INT DEFAULT NULL,
  nationality VARCHAR(50) DEFAULT NULL,
  PRIMARY KEY (id)
);

-- Insert data into the 'guest' table
INSERT INTO guest (id, name, age, nationality) VALUES
(1, 'Ramy Rashad', 21, 'egyptian'),
(2, 'Hassan', 21, 'egyptian'),
(45, 'Ahmed', 21, 'egyptian'),
(100, 'Saged', 21, 'egyptian'),
(101, 'Ahmed', 21, 'egyptian'),
(150, 'Sir Ryan', 20, 'egyptian');

-- Drop and create the 'guest_num' table
CREATE TABLE guest_num (
  guest_id INT NOT NULL,
  phone_number VARCHAR(12) NOT NULL,
  PRIMARY KEY (guest_id, phone_number)
);

-- Insert data into the 'guest_num' table
INSERT INTO guest_num (guest_id, phone_number) VALUES
(1, '0120681549'),
(1, '01280348153');

-- Drop and create the 'guest_orders' table
CREATE TABLE guest_orders (
  guest_id INT NOT NULL,
  meal_id INT NOT NULL,
  number_of_order INT DEFAULT NULL,
  PRIMARY KEY (guest_id, meal_id)
);

-- Drop and create the 'menu' table
CREATE TABLE menu (
  id INT NOT NULL,
  price INT DEFAULT NULL,
  name VARCHAR(250) DEFAULT NULL,
  PRIMARY KEY (id)
);

-- Insert data into the 'menu' table
INSERT INTO menu (id, price, name) VALUES
(1, 30, 'fries'),
(2, 20, 'can'),
(3, 10, 'water'),
(4, 30, 'juice');

-- Drop and create the 'room' table
CREATE TABLE room (
  id INT NOT NULL AUTO_INCREMENT,
  state ENUM('Occupied', 'not Occupied') DEFAULT NULL,
  class ENUM('A', 'B', 'C') DEFAULT NULL,
  price_per_night INT DEFAULT NULL,
  guest_id INT DEFAULT NULL,
  receptionist_id INT DEFAULT NULL,
  interval_duration INT,
  start_date DATE DEFAULT NULL,
  end_date DATE DEFAULT NULL,
  PRIMARY KEY (id)
);