create table producttype(
	producttypeid SERIAL PRIMARY KEY,
	producttype VARCHAR(255),
	corffictent DECIMAL(10, 2)
)
select * from producttype

create table partners(
	partnerid SERIAL PRIMARY KEY,
	partnertype VARCHAR(5),
	partnername VARCHAR(255),
	director VARCHAR(255), 
	email VARCHAR(255),
	phone VARCHAR(255),
	address TEXT,
	inn VARCHAR(255),
	rating INTEGER
)
select * from partners

create table temp_products(
	producttype VARCHAR(255),
	productname VARCHAR(255),
	articul VARCHAR(100),
	min_price DECIMAL(10, 2)
)
select * from temp_products
create table products(
	productid SERIAL PRIMARY KEY,
	producttype INTEGER,
	productname VARCHAR(255),
	articul VARCHAR(100),
	min_price DECIMAL(10, 2),
	FOREIGN KEY (producttype) REFERENCES producttype(producttypeid)
)

INSERT INTO products(producttype, productname, articul, min_price)
SELECT 
	p.producttypeid,
	tp.productname, 
	tp.articul,
	tp.min_price
FROM temp_products tp
INNER JOIN producttype p ON tp.producttype = p.producttype

select * from products

drop table sales
create table sales(
	saleid SERIAL PRIMARY KEY,
	productid INTEGER,
	partnerid INTEGER,
	quantity INTEGER,
	saledate date,
	total DECIMAL(15, 2),
	FOREIGN KEY (productid) REFERENCES products(productid),
	FOREIGN KEY (partnerid) REFERENCES partners(partnerid)
)

create table temp_sales(
	productname VARCHAR(255),
	partnername VARCHAR(255),
	quantity INTEGER,
	saledate date
)
select * from temp_sales
INSERT INTO sales(productid, partnerid, quantity, saledate, total)
SELECT
	p.productid,
	pr.partnerid,
	ts.quantity,
	ts.saledate,
	ts.quantity * p.min_price as total
FROM temp_sales ts
INNER JOIN products p ON p.productname = ts.productname
INNER JOIN partners pr ON pr.partnername = ts.partnername
select * from sales

drop table temp_sales