-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 25, 2021 at 01:36 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tool_forward`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `ID` int(10) NOT NULL,
  `user_id` int(10) NOT NULL,
  `phone_number` varchar(255) NOT NULL,
  `api_id` int(11) NOT NULL,
  `api_hash` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`ID`, `user_id`, `phone_number`, `api_id`, `api_hash`) VALUES
(1, 1464849331, '+84976661645', 2776043, '56c7eb800eb4c06de24c26dc8a38b2a8'),
(2, 1442776649, '+84394880604', 2358245, '4dc2303f73b28a1c0c8ecc7a25ab8d65'),
(3, 1599704903, '+84388787463', 3562874, 'f340822512f8f0d5fd5454c105e91f83');

-- --------------------------------------------------------

--
-- Table structure for table `groupchat`
--

CREATE TABLE `groupchat` (
  `id` int(10) NOT NULL,
  `group_id` varchar(255) NOT NULL,
  `group_tittle` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `join_group`
--

CREATE TABLE `join_group` (
  `id` int(10) NOT NULL,
  `group_type` varchar(255) NOT NULL,
  `group_link` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `join_group`
--

INSERT INTO `join_group` (`id`, `group_type`, `group_link`) VALUES
(1, 'private', 'https://t.me/joinchat/TkZN3--y4WKuEgCl'),
(2, 'private', 'https://t.me/joinchat/Hj21f7pMN6yvoaQ8'),
(3, 'private', 'https://t.me/joinchat/IABFTC-7P6-RwPsW'),
(31, 'private', 'https://t.me/joinchat/IbB22ODB4zgWRKlj'),
(32, 'public', 't.me/testbvp'),
(33, 'public', 't.me/testbvp2');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `groupchat`
--
ALTER TABLE `groupchat`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `join_group`
--
ALTER TABLE `join_group`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `ID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `groupchat`
--
ALTER TABLE `groupchat`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `join_group`
--
ALTER TABLE `join_group`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
