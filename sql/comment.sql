DROP TABLE IF EXISTS `msgcomment`;
CREATE TABLE `msgcomment` (
  `id` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `msgid` int(10) unsigned NOT NULL DEFAULT '0',
  `sender` int(10) unsigned NOT NULL DEFAULT '0',
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `cmt` varchar(1024) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `index_msgid` (`msgid`),
  KEY `index_time` (`time`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
