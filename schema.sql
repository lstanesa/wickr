CREATE TABLE if not exists `article` (
    `id` INTEGER PRIMARY KEY NOT NULL,
    `content` TEXT NOT NULL,
    `name` VARCHAR(25) NOT NULL,
    `created` INTEGER NOT NULL
);

CREATE TABLE if not exists `revision` (
    `id` INTEGER PRIMARY KEY NOT NULL,
    `created` INTEGER NOT NULL
);

CREATE TABLE if not exists `static_page` (
    `id` INTEGER PRIMARY KEY NOT NULL,
    `content` TEXT NOT NULL,
    `name` VARCHAR(25) NOT NULL,
    `created` INTEGER NOT NULL
);
