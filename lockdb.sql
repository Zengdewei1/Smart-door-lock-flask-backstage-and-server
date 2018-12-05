-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: lockDb
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `admins` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `adminName` varchar(32) DEFAULT NULL,
  `password` varchar(32) DEFAULT NULL,
  `email` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `adminName` (`adminName`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admins`
--

LOCK TABLES `admins` WRITE;
/*!40000 ALTER TABLE `admins` DISABLE KEYS */;
INSERT INTO `admins` VALUES (1,'yhm','111111','26614c.om'),(2,'zdw','111111','26sda614c.om');
/*!40000 ALTER TABLE `admins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doors`
--

DROP TABLE IF EXISTS `doors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `doors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `doorName` varchar(32) DEFAULT NULL,
  `address` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `doorName` (`doorName`),
  UNIQUE KEY `address` (`address`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doors`
--

LOCK TABLES `doors` WRITE;
/*!40000 ALTER TABLE `doors` DISABLE KEYS */;
INSERT INTO `doors` VALUES (1,'yhm','adfdfrw43'),(4,'mydo','adfdfradsa3'),(5,'mydsad','bbbdsadadsa3'),(6,NULL,NULL),(7,NULL,NULL),(8,'mydsddaad','cccsadadsa3'),(9,'mydsao090d','bbbdsadadsaa3');
/*!40000 ALTER TABLE `doors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historys`
--

DROP TABLE IF EXISTS `historys`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `historys` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `doorName` varchar(32) DEFAULT NULL,
  `adminName` varchar(32) DEFAULT NULL,
  `right` varchar(32) DEFAULT NULL,
  `charge` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `doorName` (`doorName`),
  KEY `adminName` (`adminName`),
  CONSTRAINT `historys_ibfk_1` FOREIGN KEY (`doorName`) REFERENCES `doors` (`doorname`),
  CONSTRAINT `historys_ibfk_2` FOREIGN KEY (`adminName`) REFERENCES `admins` (`adminname`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historys`
--

LOCK TABLES `historys` WRITE;
/*!40000 ALTER TABLE `historys` DISABLE KEYS */;
INSERT INTO `historys` VALUES (2,'mydo','zdw','owner',NULL),(3,'mydsad','zdw','owner',NULL),(4,NULL,NULL,'owner',NULL),(5,NULL,NULL,'owner',NULL),(6,'mydsddaad','zdw','owner','5'),(7,'mydsao090d','yhm','owner',NULL),(8,'mydsao090d','zdw','user',NULL);
/*!40000 ALTER TABLE `historys` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-05 22:20:28
