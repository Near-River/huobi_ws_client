CREATE TABLE `marketDepthTopShort` (
  `id`        INT(11)          NOT NULL AUTO_INCREMENT,
  `version`   VARCHAR(16)      NOT NULL,
  `symbolId`  VARCHAR(16)      NOT NULL,
  `askPrice`  VARCHAR(255)
              COLLATE utf8_bin NOT NULL,
  `askAmount` VARCHAR(255)
              COLLATE utf8_bin NOT NULL,
  `bidPrice`  VARCHAR(255)
              COLLATE utf8_bin NOT NULL,
  `bidAmount` VARCHAR(255)
              COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8
  COLLATE = utf8_bin
  AUTO_INCREMENT = 1;


CREATE TABLE `marketDetail` (
  `id`              INT(11)               NOT NULL AUTO_INCREMENT,
  `totalVolume`     DOUBLE                NOT NULL,
  `turnoverRate`    DOUBLE                NOT NULL,
  `commissionRatio` DOUBLE                NOT NULL,
  `innerDisc`       DOUBLE                NOT NULL,
  `level`           DOUBLE                NOT NULL,
  `volumeRatio`     DOUBLE                NOT NULL,
  `turnVolume`      DOUBLE                NOT NULL,
  `priceLast`       DOUBLE                NOT NULL,
  `priceOpen`       DOUBLE                NOT NULL,
  `updownRatio`     DOUBLE                NOT NULL,
  `outerDisc`       DOUBLE                NOT NULL,
  `priceHigh`       DOUBLE                NOT NULL,
  `updownVolume`    DOUBLE                NOT NULL,
  `amount`          DOUBLE                NOT NULL,
  `totalAmount`     DOUBLE                NOT NULL,
  `symbolId`        VARCHAR(16)           NOT NULL,
  `priceNew`        DOUBLE                NOT NULL,
  `priceLow`        DOUBLE                NOT NULL,
  `poor`            DOUBLE                NOT NULL,
  `priceAverage`    DOUBLE                NOT NULL,
  `trades`          TEXT COLLATE utf8_bin NOT NULL,
  `asks`            TEXT COLLATE utf8_bin NOT NULL,
  `bids`            TEXT COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8
  COLLATE = utf8_bin
  AUTO_INCREMENT = 1;


CREATE TABLE `tradeDetail` (
  `id`        INT(11)               NOT NULL AUTO_INCREMENT,
  `symbolId`  VARCHAR(16)           NOT NULL,
  `tradeId`   VARCHAR(255)
              COLLATE utf8_bin      NOT NULL,
  `amount`    VARCHAR(255)
              COLLATE utf8_bin      NOT NULL,
  `time`      VARCHAR(255)
              COLLATE utf8_bin      NOT NULL,
  `price`     VARCHAR(255)
              COLLATE utf8_bin      NOT NULL,
  `direction` TEXT COLLATE utf8_bin NOT NULL,
  `topBids`   TEXT COLLATE utf8_bin NOT NULL,
  `topAsks`   TEXT COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8
  COLLATE = utf8_bin
  AUTO_INCREMENT = 1;


CREATE TABLE `marketDepthTopDiff` (
  `id`         INT(11)          NOT NULL AUTO_INCREMENT,
  `version`    VARCHAR(16)      NOT NULL,
  `versionOld` VARCHAR(16)      NOT NULL,
  `symbolId`   VARCHAR(16)      NOT NULL,
  `askDelete`  VARCHAR(64)
               COLLATE utf8_bin NOT NULL,
  `bidDelete`  VARCHAR(64)
               COLLATE utf8_bin NOT NULL,
  `bidInsert`  VARCHAR(255)
               COLLATE utf8_bin NOT NULL,
  `askInsert`  VARCHAR(255)
               COLLATE utf8_bin NOT NULL,
  `askUpdate`  VARCHAR(255)
               COLLATE utf8_bin NOT NULL,
  `bidUpdate`  VARCHAR(255)
               COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8
  COLLATE = utf8_bin
  AUTO_INCREMENT = 1;


CREATE TABLE `marketOverview` (
  `id`          INT(11)     NOT NULL AUTO_INCREMENT,
  `symbolId`    VARCHAR(16) NOT NULL,
  `priceNew`    DOUBLE      NOT NULL,
  `totalAmount` DOUBLE      NOT NULL,
  `totalVolume` DOUBLE      NOT NULL,
  `priceOpen`   DOUBLE      NOT NULL,
  `priceHigh`   DOUBLE      NOT NULL,
  `priceBid`    DOUBLE      NOT NULL,
  `priceAsk`    DOUBLE      NOT NULL,
  `priceLow`    DOUBLE      NOT NULL,
  PRIMARY KEY (`id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8
  COLLATE = utf8_bin
  AUTO_INCREMENT = 1;


CREATE TABLE `lastKLine` (
  `id`        INT(11)     NOT NULL AUTO_INCREMENT,
  `symbolId`  VARCHAR(16) NOT NULL,
  `time`      INT(11)     NOT NULL,
  `isTemp`    INT(1),
  `priceOpen` DOUBLE      NOT NULL,
  `priceLow`  DOUBLE      NOT NULL,
  `volume`    DOUBLE      NOT NULL,
  `priceLast` DOUBLE      NOT NULL,
  `priceHigh` DOUBLE      NOT NULL,
  `amount`    DOUBLE      NOT NULL,
  `period`    VARCHAR(16) NOT NULL,
  `count`     INT(11)     NOT NULL,
  PRIMARY KEY (`id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8
  COLLATE = utf8_bin
  AUTO_INCREMENT = 1;


CREATE TABLE `lastTimeLine` (
  `id`        INT(11)     NOT NULL AUTO_INCREMENT,
  `symbolId`  VARCHAR(16) NOT NULL,
  `time`      INT(11)     NOT NULL,
  `isTemp`    INT(1),
  `amount`    DOUBLE      NOT NULL,
  `priceLast` DOUBLE      NOT NULL,
  `volume`    DOUBLE      NOT NULL,
  `count`     INT(11)     NOT NULL,
  PRIMARY KEY (`id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8
  COLLATE = utf8_bin
  AUTO_INCREMENT = 1;
