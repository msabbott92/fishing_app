-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema car_dealz_schema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema car_dealz_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `car_dealz_schema` DEFAULT CHARACTER SET utf8 ;
USE `car_dealz_schema` ;

-- -----------------------------------------------------
-- Table `car_dealz_schema`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car_dealz_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car_dealz_schema`.`cars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car_dealz_schema`.`cars` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `price` INT NULL,
  `model` VARCHAR(45) NULL,
  `make` VARCHAR(45) NULL,
  `year` VARCHAR(45) NULL,
  `description` TEXT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_cars_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_cars_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `car_dealz_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `car_dealz_schema`.`purchases`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `car_dealz_schema`.`purchases` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `car_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_purchases_cars1_idx` (`car_id` ASC) VISIBLE,
  INDEX `fk_purchases_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_purchases_cars1`
    FOREIGN KEY (`car_id`)
    REFERENCES `car_dealz_schema`.`cars` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_purchases_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `car_dealz_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
