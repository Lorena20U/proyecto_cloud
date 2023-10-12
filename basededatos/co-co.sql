-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 16, 2021 at 02:28 AM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 7.4.16
CREATE DATABASE coandco;
USE coandco;


SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `co-co`
--

-- --------------------------------------------------------

--
-- Table structure for table `intereses`
--

CREATE TABLE IF NOT EXISTS `intereses` (
  `id` int(11) NOT NULL,
  `descripcion` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `intereses`
--

INSERT INTO `intereses` (`id`, `descripcion`) VALUES
(1, 'Programación'),
(2, 'Diseno'),
(3, 'Estudio mercado'),
(4, 'Campañas de publicidad'),
(5, 'Matemáticas'),
(6, 'Circuitos');

-- --------------------------------------------------------

--
-- Table structure for table `proyectos`
--

CREATE TABLE IF NOT EXISTS `proyectos` (
  `id_proyecto` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `objetivo` varchar(50) NOT NULL,
  `descripcion` varchar(150) NOT NULL,
  `fecha_cierre` varchar(225) NOT NULL,
  `visible` int(11) NOT NULL,
  `cupo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `proyecto_intereses`
--

CREATE TABLE IF NOT EXISTS `proyecto_intereses` (
  `id_proyecto` int(11) DEFAULT NULL,
  `id_interes` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tag`
--

CREATE TABLE IF NOT EXISTS `tag` (
  `id_u` int(11) NOT NULL,
  `tag_t` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `usuario`
--

CREATE TABLE IF NOT EXISTS `usuario` (
  `id` int(11) NOT NULL,
  `nombre` varchar(44) DEFAULT NULL,
  `apellido` varchar(44) DEFAULT NULL,
  `mail` varchar(225) DEFAULT NULL,
  `tel` int(11) DEFAULT NULL,
  `birth` varchar(11) DEFAULT NULL,
  `password` varchar(225) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `usuario_proyecto`
--

CREATE TABLE IF NOT EXISTS `usuario_proyecto` (
  `id_usuario` int(11) DEFAULT NULL,
  `id_proyecto` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `intereses`
--
ALTER TABLE `intereses`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `proyectos`
--
ALTER TABLE `proyectos`
  ADD PRIMARY KEY (`id_proyecto`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Indexes for table `proyecto_intereses`
--
ALTER TABLE `proyecto_intereses`
  ADD KEY `id_proyecto` (`id_proyecto`),
  ADD KEY `id_interes` (`id_interes`);

--
-- Indexes for table `tag`
--
ALTER TABLE `tag`
  ADD KEY `id_u` (`id_u`),
  ADD KEY `tag_t` (`tag_t`);

--
-- Indexes for table `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `usuario_proyecto`
--
ALTER TABLE `usuario_proyecto`
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `id_proyecto` (`id_proyecto`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `intereses`
--
ALTER TABLE `intereses`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `proyectos`
--
ALTER TABLE `proyectos`
  MODIFY `id_proyecto` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `proyectos`
--
ALTER TABLE `proyectos`
  ADD CONSTRAINT `proyectos_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id`);

--
-- Constraints for table `proyecto_intereses`
--
ALTER TABLE `proyecto_intereses`
  ADD CONSTRAINT `proyecto_intereses_ibfk_1` FOREIGN KEY (`id_proyecto`) REFERENCES `proyectos` (`id_proyecto`),
  ADD CONSTRAINT `proyecto_intereses_ibfk_2` FOREIGN KEY (`id_interes`) REFERENCES `intereses` (`id`);

--
-- Constraints for table `tag`
--
ALTER TABLE `tag`
  ADD CONSTRAINT `tag_ibfk_1` FOREIGN KEY (`id_u`) REFERENCES `usuario` (`id`),
  ADD CONSTRAINT `tag_ibfk_2` FOREIGN KEY (`tag_t`) REFERENCES `intereses` (`id`);

--
-- Constraints for table `usuario_proyecto`
--
ALTER TABLE `usuario_proyecto`
  ADD CONSTRAINT `usuario_proyecto_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id`),
  ADD CONSTRAINT `usuario_proyecto_ibfk_2` FOREIGN KEY (`id_proyecto`) REFERENCES `proyectos` (`id_proyecto`);
COMMIT;

SELECT * FROM usuario;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
