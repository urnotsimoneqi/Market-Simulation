/*
Navicat MySQL Data Transfer

Source Server         : test
Source Server Version : 80015
Source Host           : localhost:3306
Source Database       : testdb

Target Server Type    : MYSQL
Target Server Version : 80015
File Encoding         : 65001

Date: 2019-11-21 14:31:57
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for ads
-- ----------------------------
DROP TABLE IF EXISTS `ads`;
CREATE TABLE `ads` (
  `ad_id` int(11) NOT NULL,
  `ad_type` varchar(255) NOT NULL,
  `seller_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `ad_expense` int(11) NOT NULL,
  `ad_year` int(11) NOT NULL,
  `ad_quarter` int(11) NOT NULL,
  PRIMARY KEY (`ad_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ads
-- ----------------------------
INSERT INTO `ads` VALUES ('1', 'Basic', '1', '2', '100', '2019', '2');
INSERT INTO `ads` VALUES ('2', 'Target', '5', '4', '100', '2019', '2');

-- ----------------------------
-- Table structure for customer
-- ----------------------------
DROP TABLE IF EXISTS `customer`;
CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_type` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `customer_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `customer_email` varchar(255) DEFAULT NULL,
  `customer_wallet` double(11,0) NOT NULL,
  `customer_tolerance` double(11,2) NOT NULL,
  `customer_status` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of customer
-- ----------------------------
INSERT INTO `customer` VALUES ('1', '', 'Simone', 'A0198890Hrobot@gmail.com', '800', '0.50', null);
INSERT INTO `customer` VALUES ('2', '', 'Betsy', 'A0198890Hrobot@gmail.com', '800', '0.50', null);
INSERT INTO `customer` VALUES ('3', '', 'Matthew', 'A0198890Hrobot@gmail.com', '800', '0.50', null);
INSERT INTO `customer` VALUES ('4', null, 'Dan', 'A0198890Hrobot@gmail.com', '800', '0.50', null);
INSERT INTO `customer` VALUES ('5', null, 'Ewa', 'A0198890Hrobot@gmail.com', '800', '0.50', null);

-- ----------------------------
-- Table structure for customer_ads
-- ----------------------------
DROP TABLE IF EXISTS `customer_ads`;
CREATE TABLE `customer_ads` (
  `ad_id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  PRIMARY KEY (`ad_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of customer_ads
-- ----------------------------
INSERT INTO `customer_ads` VALUES ('1', '2');

-- ----------------------------
-- Table structure for product
-- ----------------------------
DROP TABLE IF EXISTS `product`;
CREATE TABLE `product` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `product_quality` double(11,2) NOT NULL,
  `product_status` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of product
-- ----------------------------
INSERT INTO `product` VALUES ('1', 'iPhone XS', '0.90', null);
INSERT INTO `product` VALUES ('2', 'iPhone XR', '0.80', null);
INSERT INTO `product` VALUES ('3', 'Google pixel', '0.70', null);
INSERT INTO `product` VALUES ('4', 'Huawei P30 pro', '0.90', null);
INSERT INTO `product` VALUES ('5', 'iPhone XS case', '0.80', null);
INSERT INTO `product` VALUES ('6', 'iPhone XR case', '0.70', null);
INSERT INTO `product` VALUES ('7', 'Google pixel case', '0.60', null);
INSERT INTO `product` VALUES ('8', 'Huawei P30 pro case', '0.50', null);

-- ----------------------------
-- Table structure for promotion
-- ----------------------------
DROP TABLE IF EXISTS `promotion`;
CREATE TABLE `promotion` (
  `promotion_id` int(11) NOT NULL,
  `promotion_discount` varchar(255) NOT NULL,
  `promotion_status` varchar(255) NOT NULL,
  `promotion_from` datetime NOT NULL,
  `promotion_to` datetime NOT NULL,
  PRIMARY KEY (`promotion_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of promotion
-- ----------------------------

-- ----------------------------
-- Table structure for related_product
-- ----------------------------
DROP TABLE IF EXISTS `related_product`;
CREATE TABLE `related_product` (
  `related_product_id1` int(11) NOT NULL,
  `related_product_id2` int(11) NOT NULL,
  `status` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of related_product
-- ----------------------------
INSERT INTO `related_product` VALUES ('1', '5', null);
INSERT INTO `related_product` VALUES ('2', '6', null);
INSERT INTO `related_product` VALUES ('3', '7', null);
INSERT INTO `related_product` VALUES ('4', '8', null);

-- ----------------------------
-- Table structure for sales_summary
-- ----------------------------
DROP TABLE IF EXISTS `sales_summary`;
CREATE TABLE `sales_summary` (
  `seller_id` int(11) NOT NULL,
  `sales_year` int(4) NOT NULL,
  `sales_quarter` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sales_expense_amount` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `sales_revenue` int(11) DEFAULT NULL,
  `sales_profit` int(11) DEFAULT NULL,
  PRIMARY KEY (`seller_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sales_summary
-- ----------------------------

-- ----------------------------
-- Table structure for seller
-- ----------------------------
DROP TABLE IF EXISTS `seller`;
CREATE TABLE `seller` (
  `seller_id` int(11) NOT NULL,
  `seller_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `seller_wallet` double(11,2) NOT NULL,
  `seller_status` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`seller_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of seller
-- ----------------------------
INSERT INTO `seller` VALUES ('1', 'Alice', '1000.00', null);
INSERT INTO `seller` VALUES ('2', 'Bob', '1000.00', null);
INSERT INTO `seller` VALUES ('3', 'Carol', '1000.00', null);
INSERT INTO `seller` VALUES ('4', 'Dave', '500.00', null);
INSERT INTO `seller` VALUES ('5', 'Eve', '500.00', null);

-- ----------------------------
-- Table structure for stock
-- ----------------------------
DROP TABLE IF EXISTS `stock`;
CREATE TABLE `stock` (
  `product_id` int(11) NOT NULL,
  `seller_id` int(11) NOT NULL,
  `stock_quantity` int(11) DEFAULT NULL,
  `stock_cost` int(6) DEFAULT NULL,
  `stock_price` int(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of stock
-- ----------------------------
INSERT INTO `stock` VALUES ('1', '2', '20', '300', '500');
INSERT INTO `stock` VALUES ('1', '3', '20', '300', '490');
INSERT INTO `stock` VALUES ('2', '1', '30', '280', '480');
INSERT INTO `stock` VALUES ('2', '2', '20', '280', '480');
INSERT INTO `stock` VALUES ('2', '3', '20', '280', '480');
INSERT INTO `stock` VALUES ('3', '4', '50', '200', '400');
INSERT INTO `stock` VALUES ('4', '5', '50', '150', '300');
INSERT INTO `stock` VALUES ('5', '2', '50', '20', '100');
INSERT INTO `stock` VALUES ('5', '3', '50', '20', '90');
INSERT INTO `stock` VALUES ('5', '1', '50', '20', '95');
INSERT INTO `stock` VALUES ('6', '1', '50', '20', '95');
INSERT INTO `stock` VALUES ('6', '2', '50', '20', '95');
INSERT INTO `stock` VALUES ('6', '3', '50', '20', '95');
INSERT INTO `stock` VALUES ('7', '4', '25', '15', '80');
INSERT INTO `stock` VALUES ('8', '5', '70', '15', '60');

-- ----------------------------
-- Table structure for trans_record
-- ----------------------------
DROP TABLE IF EXISTS `trans_record`;
CREATE TABLE `trans_record` (
  `transaction_id` int(11) NOT NULL AUTO_INCREMENT,
  `transaction_datetime` datetime NOT NULL,
  `transaction_year` int(11) NOT NULL,
  `transaction_quarter` int(11) NOT NULL,
  `seller_id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `transaction_related` tinyint(1) NOT NULL,
  `transaction_quantity` int(11) NOT NULL,
  `transaction_amount` int(11) NOT NULL,
  `transaction_promotion_id` int(11) DEFAULT NULL,
  `transaction_status` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`transaction_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of trans_record
-- ----------------------------
INSERT INTO `trans_record` VALUES ('1', '2019-03-08 20:16:00', '2019', '1', '3', '2', '2', '1', '1', '480', null, '');
INSERT INTO `trans_record` VALUES ('2', '2019-04-11 12:48:57', '2019', '2', '4', '1', '3', '1', '1', '400', null, null);
INSERT INTO `trans_record` VALUES ('3', '2019-04-11 12:48:57', '2019', '2', '4', '1', '7', '1', '1', '80', null, null);
INSERT INTO `trans_record` VALUES ('4', '2019-05-16 22:57:07', '2019', '2', '2', '1', '5', '1', '2', '200', null, null);
INSERT INTO `trans_record` VALUES ('5', '2019-07-17 16:23:27', '2019', '3', '5', '3', '4', '1', '1', '300', null, null);
INSERT INTO `trans_record` VALUES ('6', '2019-07-18 08:59:37', '2019', '3', '5', '3', '8', '1', '2', '160', null, null);
INSERT INTO `trans_record` VALUES ('7', '2019-10-01 21:00:52', '2019', '4', '1', '2', '6', '1', '1', '95', null, null);
