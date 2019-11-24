drop table if exists transaction;
drop table if exists product_summary;
drop table if exists related_product;
drop table if exists sales_summary;
drop table if exists customer_ads;
drop table if exists promotion;
drop table if exists stock;
drop table if exists ads;
drop table if exists product;
drop table if exists customer;
drop table if exists seller;

-- ----------------------------
-- Table structure for seller
-- ----------------------------
CREATE TABLE seller
(
    seller_id     int auto_increment primary key NOT NULL,
    seller_name   varchar(255),
    seller_wallet double(11, 2) default 0,
    seller_status varchar(255)  DEFAULT NULL
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

-- ----------------------------
-- Records of seller
-- ----------------------------
INSERT INTO seller (seller_name, seller_wallet)
VALUES ('Alice', 100000.00);
INSERT INTO seller (seller_name, seller_wallet)
VALUES ('Bob', 10000.00);
INSERT INTO seller (seller_name, seller_wallet)
VALUES ('Carol', 100000.00);
INSERT INTO seller (seller_name, seller_wallet)
VALUES ('Dave', 50000.00);
INSERT INTO seller (seller_name, seller_wallet)
VALUES ('Eve', 50000.00);

-- ----------------------------
-- Table structure for ads
-- ----------------------------
CREATE TABLE ads
(
    ad_id       int AUTO_INCREMENT PRIMARY KEY,
    ad_type     varchar(255),
    description text,
    seller_id   int,
    product_id  int,
    ad_expense  double,
    ad_year     int(4),
    ad_quarter  TINYINT,
    status      TINYINT NOT NULL,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ads
-- ----------------------------
INSERT INTO Ads (ad_type, description, seller_id, product_id, ad_expense, ad_year, ad_quarter, status)
VALUES ('Basic', '', 2, 2, 100, 2019, 2, 1);
INSERT INTO Ads (ad_type, description, seller_id, product_id, ad_expense, ad_year, ad_quarter, status)
VALUES ('Target', '', 5, 4, 200, 2019, 2, 1);

-- ----------------------------
-- Table structure for customer
-- ----------------------------
CREATE TABLE `customer`
(
    `customer_id`        int                                                     NOT NULL AUTO_INCREMENT,
    `customer_type`      tinyint      DEFAULT 0,
    `customer_name`      varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
    `customer_email`     varchar(255) DEFAULT NULL,
    `customer_wallet`    double(11, 0)                                           NOT NULL,
    `customer_tolerance` double(11, 2)                                           NOT NULL,
    `customer_status`    varchar(255) DEFAULT NULL,
    PRIMARY KEY (`customer_id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

-- ----------------------------
-- Records of customer
-- ----------------------------
INSERT INTO customer (customer_type, customer_name, customer_email, customer_wallet, customer_tolerance)
VALUES (0, 'Simone', 'A0198890Hrobot@gmail.com', 800, 0.80);
INSERT INTO customer (customer_type, customer_name, customer_email, customer_wallet, customer_tolerance)
VALUES (1, 'Betsy', 'A0198890Hrobot@gmail.com', 1000, 0.60);
INSERT INTO customer (customer_type, customer_name, customer_email, customer_wallet, customer_tolerance)
VALUES (0, 'Matthew', 'A0198890Hrobot@gmail.com', 900, 0.80);
INSERT INTO customer (customer_type, customer_name, customer_email, customer_wallet, customer_tolerance)
VALUES (1, 'Lisa', 'A0198890Hrobot@gmail.com', 800, 0.80);
INSERT INTO customer (customer_type, customer_name, customer_email, customer_wallet, customer_tolerance)
VALUES (1, 'Jimmy', 'A0198890Hrobot@gmail.com', 800, 0.50);
INSERT INTO customer(customer_type, customer_name, customer_email, customer_wallet, customer_tolerance) VALUES (0 , 'Ximeng', 'A0198890Hrobot@gmail.com', 600, 0.8);
INSERT INTO customer(customer_type, customer_name, customer_email, customer_wallet, customer_tolerance) VALUES (1 , 'Laoxi', 'A0198890Hrobot@gmail.com', 600, 0.8);
INSERT INTO customer(customer_type, customer_name, customer_email, customer_wallet, customer_tolerance) VALUES (0 , 'Xiaoxing', 'A0198890Hrobot@gmail.com', 600, 0.8);
INSERT INTO customer(customer_type, customer_name, customer_email, customer_wallet, customer_tolerance) VALUES (1 , 'Xiaoqi', 'A0198890Hrobot@gmail.com', 600, 0.5);
INSERT INTO customer(customer_type, customer_name, customer_email, customer_wallet, customer_tolerance) VALUES (0 , 'Meiqi', 'A0198890Hrobot@gmail.com', 800, 0.5);
INSERT INTO customer(customer_type, customer_name, customer_email, customer_wallet, customer_tolerance) VALUES (0 , 'Zixuan', 'A0198890Hrobot@gmail.com', 800, 0.7);
INSERT INTO customer(customer_type, customer_name, customer_email, customer_wallet, customer_tolerance) VALUES (0 , 'Xuanyi', 'A0198890Hrobot@gmail.com', 600, 0.8);
INSERT INTO customer(customer_type, customer_name, customer_email, customer_wallet, customer_tolerance) VALUES (1 , 'Laoxi', 'A0198890Hrobot@gmail.com', 600, 0.8);
INSERT INTO customer(customer_type, customer_name, customer_email, customer_wallet, customer_tolerance) VALUES (0 , 'Xiaoxing', 'A0198890Hrobot@gmail.com', 600, 0.8);
INSERT INTO customer(customer_type, customer_name, customer_email, customer_wallet, customer_tolerance) VALUES (1 , 'Xiaoqi', 'A0198890Hrobot@gmail.com', 600, 0.5);
INSERT INTO customer(customer_type, customer_name, customer_email, customer_wallet, customer_tolerance) VALUES (0 , 'Meiqi', 'A0198890Hrobot@gmail.com', 800, 0.5);
INSERT INTO customer(customer_type, customer_name, customer_email, customer_wallet, customer_tolerance) VALUES (0 , 'Zixuan', 'A0198890Hrobot@gmail.com', 800, 0.7);
INSERT INTO customer(customer_type, customer_name, customer_email, customer_wallet, customer_tolerance) VALUES (0 , 'Ximeng', 'A0198890Hrobot@gmail.com', 600, 0.8);
INSERT INTO customer(customer_type, customer_name, customer_email, customer_wallet, customer_tolerance) VALUES (1 , 'Laoxi', 'A0198890Hrobot@gmail.com', 600, 0.8);
INSERT INTO customer(customer_type, customer_name, customer_email, customer_wallet, customer_tolerance) VALUES (0 , 'Xiaoxing', 'A0198890Hrobot@gmail.com', 600, 0.8);
INSERT INTO customer(customer_type, customer_name, customer_email, customer_wallet, customer_tolerance) VALUES (2 , 'Fujing', 'A0198890Hrobot@gmail.com', 600, 0.5);
INSERT INTO customer(customer_type, customer_name, customer_email, customer_wallet, customer_tolerance) VALUES (2 , 'Yammy', 'A0198890Hrobot@gmail.com', 800, 0.5);
INSERT INTO customer(customer_type, customer_name, customer_email, customer_wallet, customer_tolerance) VALUES (2 , 'Dajuan', 'A0198890Hrobot@gmail.com', 800, 0.7);
INSERT INTO customer(customer_type, customer_name, customer_email, customer_wallet, customer_tolerance) VALUES (2 , 'Sunnee', 'A0198890Hrobot@gmail.com', 600, 0.8);
INSERT INTO customer(customer_type, customer_name, customer_email, customer_wallet, customer_tolerance) VALUES (2 , 'Chaoyue', 'A0198890Hrobot@gmail.com', 600, 0.8);
INSERT INTO customer(customer_type, customer_name, customer_email, customer_wallet, customer_tolerance) VALUES (2 , 'Shanzhi', 'A0198890Hrobot@gmail.com', 600, 0.8);
INSERT INTO customer(customer_type, customer_name, customer_email, customer_wallet, customer_tolerance) VALUES (2 , 'Zining', 'A0198890Hrobot@gmail.com', 600, 0.5);
INSERT INTO customer(customer_type, customer_name, customer_email, customer_wallet, customer_tolerance) VALUES (2 , 'Ziting', 'A0198890Hrobot@gmail.com', 800, 0.5);
INSERT INTO customer(customer_type, customer_name, customer_email, customer_wallet, customer_tolerance) VALUES (2 , 'Zixuan', 'A0198890Hrobot@gmail.com', 800, 0.7);

-- ----------------------------
-- Table structure for customer_ads
-- ----------------------------
CREATE TABLE customer_ads
(
    id          INT AUTO_INCREMENT PRIMARY KEY,
    ad_id       int NOT NULL,
    customer_id int not null,
    FOREIGN KEY (ad_id) REFERENCES Ads (ad_id),
    FOREIGN KEY (customer_id) REFERENCES customer (customer_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of customer_ads
-- ----------------------------
INSERT INTO customer_ads (ad_id, customer_id)
VALUES (1, 1);
INSERT INTO customer_ads (ad_id, customer_id)
VALUES (1, 2);
INSERT INTO customer_ads (ad_id, customer_id)
VALUES (2, 2);

-- ----------------------------
-- Table structure for product
-- ----------------------------
CREATE TABLE product
(
    product_id           int auto_increment NOT NULL primary key,
    product_name         varchar(255),
    product_market_price double,
    product_status       varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of product
-- ----------------------------
INSERT INTO product (product_name, product_market_price, product_status)
VALUES ('iPhone XS', 500, null);
INSERT INTO product (product_name, product_market_price, product_status)
VALUES ('iPhone XR', 600, null);
INSERT INTO product (product_name, product_market_price, product_status)
VALUES ('Google pixel', 500, null);
INSERT INTO product (product_name, product_market_price, product_status)
VALUES ('Huawei P30 pro', 300, null);
INSERT INTO product (product_name, product_market_price, product_status)
VALUES ('iPhone XS case', 10, null);
INSERT INTO product (product_name, product_market_price, product_status)
VALUES ('iPhone XR case', 10, null);
INSERT INTO product (product_name, product_market_price, product_status)
VALUES ('Google pixel case', 15, null);
INSERT INTO product (product_name, product_market_price, product_status)
VALUES ('Huawei P30 pro case', 20, null);

-- ----------------------------
-- Table structure for promotion
-- ----------------------------
CREATE TABLE `promotion` (
                             `promotion_id`       int auto_increment NOT NULL,
                             `promotion_discount` double default 1.0,
                             `promotion_status`   varchar(255),
                             `promotion_from`     datetime,
                             `promotion_to`       datetime,
                             PRIMARY KEY (`promotion_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of promotion
-- ----------------------------
insert into promotion(promotion_discount) values (0.95);
insert into promotion(promotion_discount) values (0.9);
insert into promotion(promotion_discount) values (0.8);
insert into promotion(promotion_discount) values (0.5);
insert into promotion(promotion_discount) values (-50);

-- ----------------------------
-- Table structure for related_product
-- ----------------------------
CREATE TABLE related_product
(
    id                  int auto_increment not null primary key,
    related_product_id1 int                NOT NULL,
    related_product_id2 int                NOT NULL,
    status              varchar(255) DEFAULT NULL,
    FOREIGN KEY (related_product_id1) REFERENCES product (product_id),
    FOREIGN KEY (related_product_id2) REFERENCES product (product_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of related_product
-- ----------------------------
INSERT INTO related_product (related_product_id1, related_product_id2)
VALUES (1, 5);
INSERT INTO related_product (related_product_id1, related_product_id2)
VALUES (2, 6);
INSERT INTO related_product (related_product_id1, related_product_id2)
VALUES (3, 7);
INSERT INTO related_product (related_product_id1, related_product_id2)
VALUES (4, 8);
INSERT INTO related_product (related_product_id1, related_product_id2)
VALUES (5, 1);
INSERT INTO related_product (related_product_id1, related_product_id2)
VALUES (6, 2);
INSERT INTO related_product (related_product_id1, related_product_id2)
VALUES (7, 3);
INSERT INTO related_product (related_product_id1, related_product_id2)
VALUES (8, 4);

-- ----------------------------
-- Table structure for sales_summary
-- ----------------------------
CREATE TABLE sales_summary
(
    id                   int auto_increment primary key not null,
    seller_id            int                            NOT NULL,
    sales_year           int(4)                         NOT NULL,
    sales_quarter        tinyint                        NOT NULL,
    sales_expense_amount double default 0,
    sales_revenue        double DEFAULT 0,
    sales_profit         double DEFAULT 0,
    FOREIGN KEY (seller_id) REFERENCES seller (seller_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sales_summary
-- ----------------------------
INSERT INTO sales_summary(seller_id, sales_year, sales_quarter, sales_expense_amount, sales_revenue, sales_profit)
VALUES (1, 2019, 1, 0, 0, 0);
INSERT INTO sales_summary(seller_id, sales_year, sales_quarter, sales_expense_amount, sales_revenue, sales_profit)
VALUES (2, 2019, 1, 0, 0, 0);
INSERT INTO sales_summary(seller_id, sales_year, sales_quarter, sales_expense_amount, sales_revenue, sales_profit)
VALUES (3, 2019, 1, 0, 480, 200);
INSERT INTO sales_summary(seller_id, sales_year, sales_quarter, sales_expense_amount, sales_revenue, sales_profit)
VALUES (4, 2019, 1, 0, 0, 0);
INSERT INTO sales_summary(seller_id, sales_year, sales_quarter, sales_expense_amount, sales_revenue, sales_profit)
VALUES (5, 2019, 1, 0, 0, 0);
INSERT INTO sales_summary(seller_id, sales_year, sales_quarter, sales_expense_amount, sales_revenue, sales_profit)
VALUES (1, 2019, 2, 0, 0, 0);
INSERT INTO sales_summary(seller_id, sales_year, sales_quarter, sales_expense_amount, sales_revenue, sales_profit)
VALUES (2, 2019, 2, 100, 200, 160);
INSERT INTO sales_summary(seller_id, sales_year, sales_quarter, sales_expense_amount, sales_revenue, sales_profit)
VALUES (3, 2019, 2, 0, 0, 0);
INSERT INTO sales_summary(seller_id, sales_year, sales_quarter, sales_expense_amount, sales_revenue, sales_profit)
VALUES (4, 2019, 2, 0, 480, 265);
INSERT INTO sales_summary(seller_id, sales_year, sales_quarter, sales_expense_amount, sales_revenue, sales_profit)
VALUES (5, 2019, 2, 200, 0, 0);
INSERT INTO sales_summary(seller_id, sales_year, sales_quarter, sales_expense_amount, sales_revenue, sales_profit)
VALUES (1, 2019, 3, 0, 95, 75);
INSERT INTO sales_summary(seller_id, sales_year, sales_quarter, sales_expense_amount, sales_revenue, sales_profit)
VALUES (2, 2019, 3, 0, 0, 0);
INSERT INTO sales_summary(seller_id, sales_year, sales_quarter, sales_expense_amount, sales_revenue, sales_profit)
VALUES (3, 2019, 3, 0, 0, 0);
INSERT INTO sales_summary(seller_id, sales_year, sales_quarter, sales_expense_amount, sales_revenue, sales_profit)
VALUES (4, 2019, 3, 0, 0, 0);
INSERT INTO sales_summary(seller_id, sales_year, sales_quarter, sales_expense_amount, sales_revenue, sales_profit)
VALUES (5, 2019, 3, 0, 480, 240);

-- ----------------------------
-- Table structure for stock
-- ----------------------------
CREATE TABLE stock
(
    id              int auto_increment primary key not null,
    product_id      int                            NOT NULL,
    product_quality double(11, 2),
    seller_id       int                            NOT NULL,
    stock_quantity  int    DEFAULT 0,
    stock_cost      double DEFAULT 0,
    stock_price     double DEFAULT 0,
    FOREIGN KEY (product_id) REFERENCES product (product_id),
    FOREIGN KEY (seller_id) REFERENCES seller (seller_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of stock
-- ----------------------------
INSERT INTO stock (product_id, product_quality, seller_id, stock_quantity, stock_cost, stock_price)
VALUES (1, 0.8, 1, 20, 300, 500);
INSERT INTO stock (product_id, product_quality, seller_id, stock_quantity, stock_cost, stock_price)
VALUES (2, 0.7, 2, 10, 200, 300);
INSERT INTO stock (product_id, product_quality, seller_id, stock_quantity, stock_cost, stock_price)
VALUES (3, 0.8, 4, 50, 600, 1000);
INSERT INTO stock (product_id, product_quality, seller_id, stock_quantity, stock_cost, stock_price)
VALUES (4, 0.6, 3, 50, 600, 1000);
INSERT INTO stock (product_id, product_quality, seller_id, stock_quantity, stock_cost, stock_price)
VALUES (5, 0.5, 5, 50, 600, 1000);
INSERT INTO stock (product_id, product_quality, seller_id, stock_quantity, stock_cost, stock_price)
VALUES (6, 0.8, 1, 50, 700, 1000);
INSERT INTO stock (product_id, product_quality, seller_id, stock_quantity, stock_cost, stock_price)
VALUES (7, 0.7, 2, 20, 600, 1000);
INSERT INTO stock (product_id, product_quality, seller_id, stock_quantity, stock_cost, stock_price)
VALUES (8, 0.8, 4, 50, 600, 1000);
-- ----------------------------
-- Table structure for transaction
-- ----------------------------
CREATE TABLE transaction
(
    transaction_id       int auto_increment primary key not null,
    transaction_datetime datetime                       NOT NULL default current_timestamp,
    transaction_year     int(4)                         NOT NULL,
    transaction_quarter  tinyint                        NOT NULL,
    seller_id            int                            NOT NULL,
    customer_id          int                            NOT NULL,
    product_id           int                            NOT NULL,
    related_product_id   int                                     default 0,
    transaction_quantity int                                     default 0,
    transaction_amount   double                                  default 0,
    promotion_id         int                                     default 0,
    FOREIGN KEY (seller_id) REFERENCES seller (seller_id),
    FOREIGN KEY (customer_id) REFERENCES customer (customer_id),
    FOREIGN KEY (product_id) REFERENCES product (product_id)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8;

-- ----------------------------
-- Records of transaction
INSERT INTO transaction (transaction_datetime, transaction_year, transaction_quarter, seller_id, customer_id,
                         product_id, related_product_id,
                         transaction_quantity, transaction_amount, promotion_id)
VALUES ('2019-03-08 20:16:00', 2019, 1, 3, 2, 2, 6, 1, 480, 1);
INSERT INTO transaction (transaction_datetime, transaction_year, transaction_quarter, seller_id, customer_id,
                         product_id, related_product_id,
                         transaction_quantity, transaction_amount, promotion_id)
VALUES ('2019-04-11 12:48:57', 2019, 2, 4, 1, 3, 7, 1, 400, 1);
INSERT INTO transaction (transaction_datetime, transaction_year, transaction_quarter, seller_id, customer_id,
                         product_id, related_product_id,
                         transaction_quantity, transaction_amount, promotion_id)
VALUES ('2019-04-11 12:48:57', 2019, 2, 4, 1, 7, 3, 1, 80, 2);
INSERT INTO transaction (transaction_datetime, transaction_year, transaction_quarter, seller_id, customer_id,
                         product_id, related_product_id,
                         transaction_quantity, transaction_amount, promotion_id)
VALUES ('2019-05-16 22:57:07', 2019, 2, 2, 1, 5, 1, 2, 200, 2);
INSERT INTO transaction (transaction_datetime, transaction_year, transaction_quarter, seller_id, customer_id,
                         product_id, related_product_id,
                         transaction_quantity, transaction_amount, promotion_id)
VALUES ('2019-07-17 16:23:27', 2019, 3, 5, 3, 4, 8, 1, 300, 3);
INSERT INTO transaction (transaction_datetime, transaction_year, transaction_quarter, seller_id, customer_id,
                         product_id, related_product_id,
                         transaction_quantity, transaction_amount, promotion_id)
VALUES ('2019-07-18 08:59:37', 2019, 3, 5, 3, 8, 4, 2, 160, 0);
INSERT INTO transaction (transaction_datetime, transaction_year, transaction_quarter, seller_id, customer_id,
                         product_id, related_product_id,
                         transaction_quantity, transaction_amount, promotion_id)
VALUES ('2019-09-01 21:00:52', 2019, 3, 1, 2, 6, 2, 1, 95, 0);

-- ----------------------------
-- Table structure for product_summary
-- ----------------------------
CREATE TABLE product_summary
(
  id              int auto_increment NOT NULL primary key,
  product_id      int(11)            NOT NULL,
  product_year    int(4)             NOT NULL,
  product_quarter tinyint            NOT NULL,
  product_counter int(11)            NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of product_summary
-- ----------------------------
INSERT INTO product_summary (product_id, product_year,product_quarter,product_counter)
VALUES (1, 2019, 1, 0);
INSERT INTO product_summary (product_id, product_year,product_quarter,product_counter)
VALUES (2, 2019, 1, 1);
INSERT INTO product_summary (product_id, product_year,product_quarter,product_counter)
VALUES (3, 2019, 1, 0);
INSERT INTO product_summary (product_id, product_year,product_quarter,product_counter)
VALUES (4, 2019, 1, 0);
INSERT INTO product_summary (product_id, product_year,product_quarter,product_counter)
VALUES (5, 2019, 1, 0);
INSERT INTO product_summary (product_id, product_year,product_quarter,product_counter)
VALUES (6, 2019, 1, 0);
INSERT INTO product_summary (product_id, product_year,product_quarter,product_counter)
VALUES (7, 2019, 1, 0);
INSERT INTO product_summary (product_id, product_year,product_quarter,product_counter)
VALUES (8, 2019, 1, 0);
INSERT INTO product_summary (product_id, product_year,product_quarter,product_counter)
VALUES (1, 2019, 2, 0);
INSERT INTO product_summary (product_id, product_year,product_quarter,product_counter)
VALUES (2, 2019, 2, 0);
INSERT INTO product_summary (product_id, product_year,product_quarter,product_counter)
VALUES (3, 2019, 2, 1);
INSERT INTO product_summary (product_id, product_year,product_quarter,product_counter)
VALUES (4, 2019, 2, 0);
INSERT INTO product_summary (product_id, product_year,product_quarter,product_counter)
VALUES (5, 2019, 2, 2);
INSERT INTO product_summary (product_id, product_year,product_quarter,product_counter)
VALUES (6, 2019, 2, 0);
INSERT INTO product_summary (product_id, product_year,product_quarter,product_counter)
VALUES (7, 2019, 2, 0);
INSERT INTO product_summary (product_id, product_year,product_quarter,product_counter)
VALUES (8, 2019, 2, 0);
INSERT INTO product_summary (product_id, product_year,product_quarter,product_counter)
VALUES (1, 2019, 3, 0);
INSERT INTO product_summary (product_id, product_year,product_quarter,product_counter)
VALUES (2, 2019, 3, 0);
INSERT INTO product_summary (product_id, product_year,product_quarter,product_counter)
VALUES (3, 2019, 3, 0);
INSERT INTO product_summary (product_id, product_year,product_quarter,product_counter)
VALUES (4, 2019, 3, 1);
INSERT INTO product_summary (product_id, product_year,product_quarter,product_counter)
VALUES (5, 2019, 3, 0);
INSERT INTO product_summary (product_id, product_year,product_quarter,product_counter)
VALUES (6, 2019, 3, 1);
INSERT INTO product_summary (product_id, product_year,product_quarter,product_counter)
VALUES (7, 2019, 3, 0);
INSERT INTO product_summary (product_id, product_year,product_quarter,product_counter)
VALUES (8, 2019, 3, 2);