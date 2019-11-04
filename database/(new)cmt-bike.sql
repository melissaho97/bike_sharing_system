/*
 Navicat Premium Data Transfer

 Source Server         : Melissa Ho
 Source Server Type    : MySQL
 Source Server Version : 50724
 Source Host           : localhost
 Source Schema         : cmt-bike

 Target Server Type    : MySQL
 Target Server Version : 50724
 File Encoding         : 65001

 Date: 03/11/2019 23:37:13
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for city
-- ----------------------------
DROP TABLE IF EXISTS `city`;
CREATE TABLE `city`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `City_Name` varchar(255) NOT NULL UNIQUE,
  `Status` varchar(255) NOT NULL,
  `Created_At` datetime(0),
  `Updated_At` datetime(0),
  `Last_Operator_ID` int(11)
) ENGINE = InnoDB;

-- ----------------------------
-- Table structure for location
-- ----------------------------
DROP TABLE IF EXISTS `location`;
CREATE TABLE `location`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `Zone_Name` varchar(255) NOT NULL,
  `Slot` int(255),
  `Status` varchar(255) NOT NULL,
  `Created_At` datetime(0),
  `Updated_At` datetime(0),
  `City_ID` int(11) NOT NULL,
  `Last_Operator_ID` int(11)
) ENGINE = InnoDB;

-- ----------------------------
-- Table structure for bike
-- ----------------------------
DROP TABLE IF EXISTS `bike`;
CREATE TABLE `bike`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `Condition` varchar(255) NOT NULL,
  `Location_ID` int(11) NOT NULL,
  `City_ID` int(11) NOT NULL,
  `Created_At` datetime(0),
  `Updated_At` datetime(0),
  `Type_ID` int(11) NOT NULL,
  `Last_Operator_ID` int(11)
) ENGINE = InnoDB;

-- ----------------------------
-- Table structure for type
-- ----------------------------
DROP TABLE IF EXISTS `type`;
CREATE TABLE `type`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `Type_Name` varchar(255) NOT NULL,
  `Fixed_Price` double(10, 2),
  `Add_Price` double(10, 2),
  `Day_Price` double(10, 2),
  `Created_At` datetime(0),
  `Updated_At` datetime(0),
  `Last_Operator_ID` int(11)
) ENGINE = InnoDB;

-- ----------------------------
-- Table structure for customer
-- ----------------------------
DROP TABLE IF EXISTS `customer`;
CREATE TABLE `customer`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `Amount_Balance` double(10, 2),
  `Phone_Number` int(11),
  `Full_Name` varchar(255) NOT NULL,
  `Email` varchar(255),
  `Username` varchar(255) NOT NULL UNIQUE,
  `Password` varchar(255) NOT NULL,
  `Email_Subscription` tinyint(1),
  `Card_No` int(11),
  `Expired_Date` varchar(255),
  `CVV` int(11)
) ENGINE = InnoDB;

-- ----------------------------
-- Table structure for operator_manager
-- ----------------------------
DROP TABLE IF EXISTS `operator_manager`;
CREATE TABLE `operator_manager`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `Username` varchar(255) NOT NULL UNIQUE,
  `Password` varchar(255) NOT NULL,
  `Full_Name` varchar(255) NOT NULL,
  `Role` varchar(255) NOT NULL,
  `Status` varchar(255) NOT NULL
) ENGINE = InnoDB;

-- ----------------------------
-- Table structure for transaction
-- ----------------------------
DROP TABLE IF EXISTS `transaction`;
CREATE TABLE `transaction`  (
  `ID` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `Status` varchar(255) NOT NULL,
  `Paid_Amount` double(10, 2),
  `Created_At` datetime(0),
  `Updated_At` datetime(0),
  `Customer_ID` int(11) NOT NULL,
  `Bike_ID` int(11) NOT NULL,
  `Remarks` varchar(255),
  `Origin_ID` int(11) NOT NULL,
  `Destination_ID` int(11)
) ENGINE = InnoDB;

SET FOREIGN_KEY_CHECKS = 1;
