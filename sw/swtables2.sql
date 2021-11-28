-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema starwarsscr
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema starwarsscr
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS starwarsscr;
CREATE SCHEMA IF NOT EXISTS `starwarsscr` DEFAULT CHARACTER SET utf8 ;
USE `starwarsscr` ;

-- -----------------------------------------------------
-- Table `starwarsscr`.`char`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `starwarsscr`.`char` (
  `idchar` INT NOT NULL AUTO_INCREMENT,
  `name char` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idchar`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `starwarsscr`.`episode`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `starwarsscr`.`episode` (
  `idepisode` INT NOT NULL AUTO_INCREMENT,
  `name episode` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idepisode`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `starwarsscr`.`dialogue`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `starwarsscr`.`dialogue` (
  `iddialogue` INT NOT NULL AUTO_INCREMENT,
  `dialogue` VARCHAR(9000) NOT NULL,
  `char_idchar` INT NOT NULL,
  `episode_idepisode` INT NOT NULL,
  PRIMARY KEY (`iddialogue`),
  INDEX `fk_dialogue_char_idx` (`char_idchar` ASC) VISIBLE,
  INDEX `fk_dialogue_episode1_idx` (`episode_idepisode` ASC) VISIBLE,
  CONSTRAINT `fk_dialogue_char`
    FOREIGN KEY (`char_idchar`)
    REFERENCES `starwarsscr`.`char` (`idchar`),
  CONSTRAINT `fk_dialogue_episode1`
    FOREIGN KEY (`episode_idepisode`)
    REFERENCES `starwarsscr`.`episode` (`idepisode`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
