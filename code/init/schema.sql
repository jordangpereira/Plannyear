CREATE DATABASE plannyear;

CREATE TABLE IF NOT EXISTS `plannyear`.`importantThings` (
  `id` INT NOT NULL,
  `task` VARCHAR(200) NOT NULL,
  `status` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `plannyear`.`todoList` (
  `id` INT NOT NULL,
  `day` INT NOT NULL,
  `month` INT NOT NULL,
  `year` INT NOT NULL,
  `task` VARCHAR(200) NOT NULL,
  `status` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`day`, `month`, `year`, `id`)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `plannyear`.`spendingList` (
  `id` INT NOT NULL,
  `day` INT NOT NULL,
  `month` INT NOT NULL,
  `year` INT NOT NULL,
  `amount` int NOT NULL,
  PRIMARY KEY (`day`, `month`, `year`, `id`)
) ENGINE = InnoDB;