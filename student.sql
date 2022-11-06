-- MySQL dump 10.13  Distrib 5.1.33, for Win32 (ia32)
--
-- Host: localhost    Database: python
-- ------------------------------------------------------
-- Server version	5.1.33-community

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student` (
  `name` varchar(50) NOT NULL,
  `reg_no` varchar(8) NOT NULL,
  `Specialization` varchar(50) NOT NULL,
  `mobile` varchar(10) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `supervisorid` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`reg_no`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('user','00000000','Hello','9XXXXXXXXX','abc@xyz.com','user','12345','0'),('shiva','0000111','HEllo','','','shi','1470','0'),('Manoj','102365','Computer Architecture','9874563210','smanoj12@gmail.com','smanoj','123','null'),('Manoj','14236','Data Analytics','9845612354','asd@fgh.cpm','manoj','123','74123'),('Devansh','142394','Computer Architecture','9874561321','asd@fgy.com','dvnsh1','123','78452'),('Devansh','142398','Mechanical Manufacturing','9874561321','asd@fgy.com','dvnsh','123','42158'),('Devansh','14520','Cyber Security','9874563210','asd@fgh.com','dvnsh2','123','23147'),('Shivdutt','14526','Electronics Hardwaring','9874562103','dxt@gmail.com','dxt','123','147894'),('Shiva Dixit','741236','Mechanical Manufacturing','41258746','asd@dkj.com','dxtshiva','1258','23147'),('Manoj Rana','74563','Electronics Hardwaring','7412365890','qwer@fgh.com','rmanoj','123','147894');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supervisor`
--

DROP TABLE IF EXISTS `supervisor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `supervisor` (
  `name` varchar(50) DEFAULT NULL,
  `uid` varchar(8) NOT NULL,
  `Specialization` varchar(50) DEFAULT NULL,
  `mobile` varchar(10) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`uid`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supervisor`
--

LOCK TABLES `supervisor` WRITE;
/*!40000 ALTER TABLE `supervisor` DISABLE KEYS */;
INSERT INTO `supervisor` VALUES ('Admin','0','Hello','9XXXXXXXX','abx@cbz.com','admin','12345'),('shiva','0000111','Hello','9XXXXXX','asd@dfg.com','user','123'),('Dr. Nikhil Singh','147894','Electronics Hardwaring','9876543210','asd@fgh.com','nksingh','123'),('Dr. Ankit Nadim','23147','Cyber Security','7845369874','ankitna@gmail.com','nadank','1234'),('Dr. Rajat Raj','26458','Electrical Devices','9415875210','rajatraj@gmail.com','rajrajat','1234'),('Dr. Suresh Pandit','42158','Mechanical Manufacturing','7412365874','s.pandit12@gmail.com','psuresh','1234'),('Raghuram','56985','Data Analytics','7412589630','qwerty@xyz.com','raguhr','123'),('Dr. Amin Sahil','74123','Data Analytics','9745213698','sahilamin@gmail.com','sahilamin','1234'),('Dr. Rahul Dixit','78452','Computer Architecture','9874587410','rdixit@gmail.com','rdkt','1234');
/*!40000 ALTER TABLE `supervisor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `temp`
--

DROP TABLE IF EXISTS `temp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `temp` (
  `id` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `temp`
--

LOCK TABLES `temp` WRITE;
/*!40000 ALTER TABLE `temp` DISABLE KEYS */;
INSERT INTO `temp` VALUES ('14526');
/*!40000 ALTER TABLE `temp` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-18  6:55:40
