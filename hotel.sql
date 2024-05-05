-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: hotel
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bill`
--

DROP TABLE IF EXISTS `bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bill` (
  `id` int NOT NULL AUTO_INCREMENT,
  `total_price` int DEFAULT NULL,
  `guest_id` int DEFAULT NULL,
  `date_of_check_out` datetime DEFAULT NULL,
  `receptionist_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `guest_id` (`guest_id`),
  KEY `receptionist_id` (`receptionist_id`),
  CONSTRAINT `bill_ibfk_1` FOREIGN KEY (`guest_id`) REFERENCES `guest` (`id`),
  CONSTRAINT `bill_ibfk_2` FOREIGN KEY (`receptionist_id`) REFERENCES `employee` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill`
--

LOCK TABLES `bill` WRITE;
/*!40000 ALTER TABLE `bill` DISABLE KEYS */;
INSERT INTO `bill` VALUES (1,200,1,'2024-04-24 02:41:56',2),(2,200,1,'2024-04-24 05:41:47',2),(3,650,1,'2024-04-24 05:45:49',2),(4,650,1,'2024-04-24 05:48:28',2),(5,350,1,'2024-04-24 05:56:44',2),(6,260,1,'2024-04-24 12:04:49',2),(7,260,100,'2024-04-25 13:29:20',2),(8,290,101,'2024-04-25 13:51:39',2),(9,200,101,'2024-04-25 13:55:56',2),(10,800,100,'2024-04-25 14:00:10',2),(11,400,1,'2024-04-25 18:25:27',2),(12,150,100,'2024-04-25 18:25:40',2),(13,200,100,'2024-04-25 18:25:43',2);
/*!40000 ALTER TABLE `bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `id` int NOT NULL,
  `age` int DEFAULT NULL,
  `nationality` varchar(250) DEFAULT NULL,
  `jop` varchar(250) DEFAULT NULL,
  `salary` int DEFAULT NULL,
  `manger_id` int DEFAULT NULL,
  `name` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `manger_id` (`manger_id`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`manger_id`) REFERENCES `employee` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,30,'egyption','boss',11000,1,'Ramy Rashad'),(2,25,'egyption','reciptionist',5000,1,'ahmed'),(3,21,'egyption','chef',9000,1,'hassan'),(4,21,'egypt','receptionist',5000,1,'ahmed abass'),(45,21,'egypt','receptionist',120,1,'saged');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `feedback` (
  `id` int NOT NULL AUTO_INCREMENT,
  `opinion` varchar(255) DEFAULT NULL,
  `rate` int DEFAULT NULL,
  `guest_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_guest` (`guest_id`),
  CONSTRAINT `fk_guest` FOREIGN KEY (`guest_id`) REFERENCES `guest` (`id`),
  CONSTRAINT `chk` CHECK ((`rate` between 0 and 10))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback`
--

LOCK TABLES `feedback` WRITE;
/*!40000 ALTER TABLE `feedback` DISABLE KEYS */;
INSERT INTO `feedback` VALUES (1,'well done',10,1),(2,'good',10,100);
/*!40000 ALTER TABLE `feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `guest`
--

DROP TABLE IF EXISTS `guest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `guest` (
  `id` int NOT NULL,
  `name` varchar(120) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `nationality` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `guest`
--

LOCK TABLES `guest` WRITE;
/*!40000 ALTER TABLE `guest` DISABLE KEYS */;
INSERT INTO `guest` VALUES (1,'ramy rashad',21,'egyption'),(2,'hassan',21,'egypt'),(45,'ahmed',21,'egypt'),(100,'saged',21,'egypt'),(101,'ahmed',21,'egypt'),(150,'sir ryan',20,'egypt');
/*!40000 ALTER TABLE `guest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `guest_num`
--

DROP TABLE IF EXISTS `guest_num`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `guest_num` (
  `guest_id` int NOT NULL,
  `phone_number` varchar(12) NOT NULL,
  PRIMARY KEY (`guest_id`,`phone_number`),
  CONSTRAINT `guest_num_ibfk_1` FOREIGN KEY (`guest_id`) REFERENCES `guest` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `guest_num`
--

LOCK TABLES `guest_num` WRITE;
/*!40000 ALTER TABLE `guest_num` DISABLE KEYS */;
INSERT INTO `guest_num` VALUES (1,'0120681549'),(1,'01280348153');
/*!40000 ALTER TABLE `guest_num` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `guest_orders`
--

DROP TABLE IF EXISTS `guest_orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `guest_orders` (
  `guest_id` int NOT NULL,
  `meal_id` int NOT NULL,
  `number_of_order` int DEFAULT NULL,
  PRIMARY KEY (`guest_id`,`meal_id`),
  KEY `meal_id` (`meal_id`),
  CONSTRAINT `guest_orders_ibfk_1` FOREIGN KEY (`guest_id`) REFERENCES `guest` (`id`),
  CONSTRAINT `guest_orders_ibfk_2` FOREIGN KEY (`meal_id`) REFERENCES `menu` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `guest_orders`
--

LOCK TABLES `guest_orders` WRITE;
/*!40000 ALTER TABLE `guest_orders` DISABLE KEYS */;
/*!40000 ALTER TABLE `guest_orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu`
--

DROP TABLE IF EXISTS `menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menu` (
  `id` int NOT NULL,
  `price` int DEFAULT NULL,
  `name` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
INSERT INTO `menu` VALUES (1,30,'fries'),(2,20,'can'),(3,10,'water'),(4,30,'juice');
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `room`
--

DROP TABLE IF EXISTS `room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `room` (
  `id` int NOT NULL AUTO_INCREMENT,
  `state` enum('Occupied','not Occupied') DEFAULT NULL,
  `class` enum('A','B','C') DEFAULT NULL,
  `price_per_night` int DEFAULT NULL,
  `guest_id` int DEFAULT NULL,
  `receptionist_id` int DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `interval_duration` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `guest_id` (`guest_id`),
  KEY `receptionist_id` (`receptionist_id`),
  CONSTRAINT `room_ibfk_1` FOREIGN KEY (`guest_id`) REFERENCES `guest` (`id`),
  CONSTRAINT `room_ibfk_2` FOREIGN KEY (`receptionist_id`) REFERENCES `employee` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room`
--

LOCK TABLES `room` WRITE;
/*!40000 ALTER TABLE `room` DISABLE KEYS */;
INSERT INTO `room` VALUES (1,'Occupied','A',200,100,2,'2024-04-25','2024-04-27',2),(2,'Occupied','B',150,2,2,'2024-04-29','2024-05-01',2),(3,'not Occupied','C',100,NULL,NULL,NULL,NULL,NULL),(4,'not Occupied','A',200,NULL,NULL,NULL,NULL,NULL),(5,'not Occupied','A',200,NULL,NULL,NULL,NULL,NULL),(6,'not Occupied','A',200,NULL,NULL,NULL,NULL,NULL),(7,'not Occupied','A',200,NULL,NULL,NULL,NULL,NULL),(8,'not Occupied','B',150,NULL,NULL,NULL,NULL,NULL),(9,'not Occupied','B',150,NULL,NULL,NULL,NULL,NULL),(10,'not Occupied','B',150,NULL,NULL,NULL,NULL,NULL),(11,'not Occupied','B',150,NULL,NULL,NULL,NULL,NULL),(12,'not Occupied','B',150,NULL,NULL,NULL,NULL,NULL),(13,'not Occupied','C',100,NULL,NULL,NULL,NULL,NULL),(14,'not Occupied','C',100,NULL,NULL,NULL,NULL,NULL),(15,'not Occupied','C',100,NULL,NULL,NULL,NULL,NULL),(16,'not Occupied','C',100,NULL,NULL,NULL,NULL,NULL),(17,'not Occupied','C',100,NULL,NULL,NULL,NULL,NULL),(18,'not Occupied','A',200,NULL,NULL,NULL,NULL,NULL),(19,'not Occupied','A',200,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tables`
--

DROP TABLE IF EXISTS `tables`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tables` (
  `table_num` int NOT NULL,
  `state` enum('Available','Not available') DEFAULT NULL,
  `chairs_num` int DEFAULT NULL,
  `guest_id` int DEFAULT NULL,
  `date` date DEFAULT NULL,
  `start` datetime DEFAULT NULL,
  `receptionist_id` int DEFAULT NULL,
  PRIMARY KEY (`table_num`),
  KEY `guest_id` (`guest_id`),
  KEY `receptionist_id` (`receptionist_id`),
  CONSTRAINT `tables_ibfk_1` FOREIGN KEY (`guest_id`) REFERENCES `guest` (`id`),
  CONSTRAINT `tables_ibfk_2` FOREIGN KEY (`receptionist_id`) REFERENCES `employee` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tables`
--

LOCK TABLES `tables` WRITE;
/*!40000 ALTER TABLE `tables` DISABLE KEYS */;
INSERT INTO `tables` VALUES (1,'Not available',2,1,'2024-04-26','2024-07-21 00:00:00',2),(2,'Available',2,NULL,NULL,NULL,NULL),(3,'Available',2,NULL,NULL,NULL,NULL),(4,'Not available',2,100,'2024-04-25','2024-04-26 04:00:00',2),(5,'Not available',2,1,'2024-04-25','2024-07-21 00:00:00',2),(6,'Available',2,NULL,NULL,NULL,NULL),(7,'Available',3,NULL,NULL,NULL,NULL),(8,'Available',3,NULL,NULL,NULL,NULL),(9,'Available',3,NULL,NULL,NULL,NULL),(10,'Available',3,NULL,NULL,NULL,NULL),(11,'Available',4,NULL,NULL,NULL,NULL),(12,'Available',4,NULL,NULL,NULL,NULL),(13,'Available',4,NULL,NULL,NULL,NULL),(14,'Available',4,NULL,NULL,NULL,NULL),(15,'Available',4,NULL,NULL,NULL,NULL),(16,'Available',4,NULL,NULL,NULL,NULL),(17,'Available',5,NULL,NULL,NULL,NULL),(18,'Available',5,NULL,NULL,NULL,NULL),(19,'Available',5,NULL,NULL,NULL,NULL),(20,'Available',5,NULL,NULL,NULL,NULL),(21,'Available',6,NULL,NULL,NULL,NULL),(22,'Available',6,NULL,NULL,NULL,NULL),(23,'Available',6,NULL,NULL,NULL,NULL),(24,'Available',7,NULL,NULL,NULL,NULL),(25,'Available',7,NULL,NULL,NULL,NULL),(26,'Available',1,NULL,NULL,NULL,NULL),(27,'Available',1,NULL,NULL,NULL,NULL),(28,'Available',1,NULL,NULL,NULL,NULL),(29,'Available',1,NULL,NULL,NULL,NULL),(30,'Available',5,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `tables` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-29 13:25:40
