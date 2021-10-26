CREATE TABLE IF NOT EXISTS ETL.openstacketl (
    `timecode` DATETIME(3) NOT NULL,
    `type` VARCHAR(8) NOT NULL CHECK(type in ('compute', 'metadata')),
    `ip` VARCHAR(16) NOT NULL,
    `method` VARCHAR(6) NOT NULL,
    `status_code` SMALLINT NOT NULL,
    `length` SMALLINT NOT NULL,
    `time_taken` FLOAT(7) NOT NULL,
    PRIMARY KEY(timecode, ip)
);