-- DROP TABLE IF EXISTS get_json;

CREATE TABLE IF NOT EXISTS get_json
(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL ,
    description TEXT NOT NULL,
    category VARCHAR(255),
    price DECIMAL(10,4),
    discountPercentage DECIMAL(10,4),
    rating DECIMAL(3,2),
    stock INT,
    tags JSONB,
    brand TEXT DEFAULT NULL,
    sku VARCHAR(255),
    weight INT,
    dimensions JSONB,
    warrantyInformation VARCHAR(255),
    shippingInformation VARCHAR(255),
    availabilityStatus VARCHAR(255),
    reviews JSONB,
    returnPolicy VARCHAR(255),
    minimumOrderQuantity INT,
    meta JSONB,
    images JSONB,
    thumbnail TEXT

);

select * from get_json;
