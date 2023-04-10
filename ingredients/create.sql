CREATE TABLE meal_categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);
INSERT INTO meal_categories (name) VALUES ('petit_dejeuner');
INSERT INTO meal_categories (name) VALUES ('dejeuner');
INSERT INTO meal_categories (name) VALUES ('diner');

CREATE TABLE food_groups (
    id INT AUTO_INCREMENT PRIMARY KEY,
    meal_category_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    FOREIGN KEY (meal_category_id) REFERENCES meal_categories(id)
);
CREATE TABLE foods (
    id INT AUTO_INCREMENT PRIMARY KEY,
    food_group_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    calories DECIMAL(5, 2) NOT NULL,
    proteins DECIMAL(5, 2) NOT NULL,
    lipids DECIMAL(5, 2) NOT NULL,
    carbohydrates DECIMAL(5, 2) NOT NULL,
    season VARCHAR(255),
    restrictions VARCHAR(255),
    FOREIGN KEY (food_group_id) REFERENCES food_groups(id)
);
