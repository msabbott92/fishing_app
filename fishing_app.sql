-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema fishing_app
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `fishing_app` ;

-- -----------------------------------------------------
-- Schema fishing_app
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `fishing_app` DEFAULT CHARACTER SET utf8 ;
USE `fishing_app` ;

-- -----------------------------------------------------
-- Table `fishing_app`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fishing_app`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `fishing_app`.`log`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `fishing_app`.`log` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `date` DATE NULL,
  `location` VARCHAR(45) NULL,
  `body_water` VARCHAR(255) NULL,
  `temp` INT NULL,
  `fish_caught` INT NULL,
  `fish_type` VARCHAR(255) NULL,
  `flies_used` VARCHAR(45) NULL,
  `comments` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_log_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_log_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `fishing_app`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
