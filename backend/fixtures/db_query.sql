CREATE database IF NOT EXISTS flask_task;

USE flask_task;

CREATE TABLE IF NOT EXISTS `user` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `username` varchar(50) UNIQUE NOT NULL,
  `email` varchar(100) UNIQUE,
  `password` varchar(500) UNIQUE NOT NULL,
  `date_of_birth` date,
  `is_active` bool NOT NULL,
  `creation_timestamp` timestamp NOT NULL
);

CREATE TABLE IF NOT EXISTS `post` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `content` text NOT NULL,
  `creation_timestamp` timestamp NOT NULL,
  `modification_timestamp` timestamp NOT NULL
);

CREATE TABLE IF NOT EXISTS `comment` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `post_id` int NOT NULL,
  `user_id` int NOT NULL,
  `content` text NOT NULL,
  `creation_timestamp` timestamp NOT NULL
);

CREATE TABLE IF NOT EXISTS `like` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `post_id` int NOT NULL,
  `user_id` int NOT NULL,
  `creation_timestamp` timestamp NOT NULL
);

CREATE TABLE IF NOT EXISTS `friend` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `friend_id` int NOT NULL,
  `creation_timestamp` timestamp NOT NULL
);

ALTER TABLE `post` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

ALTER TABLE `comment` ADD FOREIGN KEY (`post_id`) REFERENCES `post` (`id`);

ALTER TABLE `comment` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

ALTER TABLE `like` ADD FOREIGN KEY (`post_id`) REFERENCES `post` (`id`);

ALTER TABLE `like` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

ALTER TABLE `friend` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

ALTER TABLE `friend` ADD FOREIGN KEY (`friend_id`) REFERENCES `user` (`id`);
