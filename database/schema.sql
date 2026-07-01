CREATE TABLE customer (
    customer_id INT,
    height INT,
    weight INT,
    body_type VARCHAR(50),
    style VARCHAR(50)
);

CREATE TABLE product (
    product_id INT,
    dress_name VARCHAR(50),
    size VARCHAR(10),
    color VARCHAR(30),
    category VARCHAR(30)
);

CREATE TABLE inventory (
    product_id INT,
    stock INT,
    floor INT,
    rack VARCHAR(20)
);
