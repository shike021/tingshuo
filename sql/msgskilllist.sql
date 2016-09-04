
-- ----------------------------
-- Table structure for msgskilllist
-- ----------------------------
DROP TABLE IF EXISTS `msgskilllist`;
CREATE TABLE `msgskilllist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `msgid` int(10) unsigned not null default 0,
  `skilltype` int(10) unsigned not null default 0,
  `sender` int(11) unsigned not null default 0,
  `usetime` timestamp not null default CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  index idx_msg(msgid)
) ENGINE=MyISAM AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

