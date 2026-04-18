create database if not exists computer;
use database computer;
create table laptops(brand Varchar(50), model varchar(50), CPU varchar(50), frequency float, RAM int, price int);   
insert into laptops values("Apple", "Macbook Pro", "Intel core i5", 3.5, 16, 1000);     
delete from laptops;
insert into laptops values("Apple", "MacBook Air M11", "Apple M1", 3.2, 8, 999),
                          ("DEll", "XPS 13", "Intel core i7", 3.9, 16, 1200), 
                          ("HP", "Spectre x360", "Intel core i7", 4.0, 16, 1300), 
                          ("Lenovo", "ThinkPad x1 Carbon", "Intel core i7", 3.8, 16, 1400),
                          ("Asus", "Zenbook 14", "Intel core i5", 3.6, 8, 900),
                          ("Acer", "Swift 3", "AMD ryzen 5", 3.8, 8, 800),
                          ("Apple", "MacBook Air M11", "Apple M1", 3.3, 16, 1200),
                          ("DELL", "Inspiron 15", "Intel core i5", 3.5, 8, 700 ),
                          ("HP", "Pavilion 14", "Intel core i5", 3.4, 8, 800), 
                          ("Lenovo", "IdeaPad 5", "AMD ryzen 7", 3.4, 4, 400),
                          ("Asus", "ROG zephyrus", "AMD ryzen 9", 4.3, 32, 1800),
                          ("Acer", "Nitro 5", "Intel core i5", 4.1, 16, 1300), 
                          ("MSI", "GF63 thin", "Intel core i5", 3.8, 8, 850),
                          ("Samsung", "Galaxy book 3", "Intel core i7", 4.1, 16, 1200),
                          ("HUAWEI", "Matebook 105", "intel core i5", 3.6, 8, 750),
                          ("Razer", "Blade 15", "intel core i7", 4.2, 16, 2000),
                          ("Microsoft", "Surface laptop 5", "intel core i7", 3.9, 16, 1300),
                          ("DELL", "Aleanware 15", "Intel core i9", 4.2, 32, 2500),
                          ("HP", "Omen 16", "AMD ryzen 7", 4.2, 16, 1400),
                          ("Lenovo", "Legion 5", "AMD ryzen 7", 4.1, 16, 1300);

 +-----------+--------------------+---------------+-----------+------+-------+
| brand     | model              | CPU           | frequency | RAM  | price |
+-----------+--------------------+---------------+-----------+------+-------+
| Apple     | MacBook Air M11    | Apple M1      |       3.2 |    8 |   999 |
| DEll      | XPS 13             | Intel core i7 |       3.9 |   16 |  1200 |
| HP        | Spectre x360       | Intel core i7 |         4 |   16 |  1300 |
| Lenovo    | ThinkPad x1 Carbon | Intel core i7 |       3.8 |   16 |  1400 |
| Asus      | Zenbook 14         | Intel core i5 |       3.6 |    8 |   900 |
| Acer      | Swift 3            | AMD ryzen 5   |       3.8 |    8 |   800 |
| Apple     | MacBook Air M11    | Apple M1      |       3.3 |   16 |  1200 |
| DELL      | Inspiron 15        | Intel core i5 |       3.5 |    8 |   700 |
| HP        | Pavilion 14        | Intel core i5 |       3.4 |    8 |   800 |
| Lenovo    | IdeaPad 5          | AMD ryzen 7   |       3.4 |    4 |   400 |
| Asus      | ROG zephyrus       | AMD ryzen 9   |       4.3 |   32 |  1800 |
| Acer      | Nitro 5            | Intel core i5 |       4.1 |   16 |  1300 |
| MSI       | GF63 thin          | Intel core i5 |       3.8 |    8 |   850 |
| Samsung   | Galaxy book 3      | Intel core i7 |       4.1 |   16 |  1200 |
| HUAWEI    | Matebook 105       | intel core i5 |       3.6 |    8 |   750 |
| Razer     | Blade 15           | intel core i7 |       4.2 |   16 |  2000 |
| Microsoft | Surface laptop 5   | intel core i7 |       3.9 |   16 |  1300 |
| DELL      | Aleanware 15       | Intel core i9 |       4.2 |   32 |  2500 |
| HP        | Omen 16            | AMD ryzen 7   |       4.2 |   16 |  1400 |
| Lenovo    | Legion 5           | AMD ryzen 7   |       4.1 |   16 |  1300 |
+-----------+--------------------+---------------+-----------+------+-------+

-- 1-vazifa

select * from laptops order by price desc limit 1;
+-------+--------------+---------------+-----------+------+-------+
| brand | model        | CPU           | frequency | RAM  | price |
+-------+--------------+---------------+-----------+------+-------+
| DELL  | Aleanware 15 | Intel core i9 |       4.2 |   32 |  2500 |
+-------+--------------+---------------+-----------+------+-------+

-- 2-vazifa

select * from laptops order by price limit 1;
+--------+-----------+-------------+-----------+------+-------+
| brand  | model     | CPU         | frequency | RAM  | price |
+--------+-----------+-------------+-----------+------+-------+
| Lenovo | IdeaPad 5 | AMD ryzen 7 |       3.4 |    4 |   400 |
+--------+-----------+-------------+-----------+------+-------+

-- 3-vazifa

select frequency from laptops where price between 400 and 1000 and CPU like "Intel%";
+-----------+
| frequency |
+-----------+
|       3.6 |
|       3.5 |
|       3.4 |
|       3.8 |
|       3.6 |
+-----------+

-- 4-vazifa

select count(*) from laptops where brand= "Apple";
+----------+
| count(*) |
+----------+
|        2 |
+----------+

-- 5-vazifa

select price from laptops where brand="Asus" and RAM=8;
------+
| price |
+-------+
|   900 |
+-------+.
""" by yerda faqat bitta malumot bor edi Asus haqida"""