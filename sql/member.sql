#-- ----------------------------
#-- Table structure for member
#-- ----------------------------
DROP TABLE IF EXISTS `member`;
CREATE TABLE `member` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `account` varchar(64) NOT NULL DEFAULT '' COMMENT '用户帐号',
  `email` varchar(128) NOT NULL DEFAULT '' COMMENT '邮箱',
  `telephonenum` varchar(11) NOT NULL DEFAULT '',
  `nickname` varchar(64) NOT NULL DEFAULT '',
  `gender` varchar(1) NOT NULL DEFAULT 'f' COMMENT 'm:male; f:female',
  `age` smallint(3) unsigned NOT NULL DEFAULT '18' COMMENT '年龄',
  `password` varchar(64) NOT NULL DEFAULT '' COMMENT 'md5(密码)',
  `avatar` varchar(256) NOT NULL DEFAULT '',
  `totallike` int(11) unsigned NOT NULL DEFAULT '0',
  `gold` int(11) NOT NULL DEFAULT '0',
  `readmsgno` int(10) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `key_account` (`account`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=1531 DEFAULT CHARSET=utf8;

#2015-08-24
alter table member add column `todaylike` int(10) unsigned not null default 0;
alter table member add column `yesterdaylike` int(10) unsigned not null default 0;
