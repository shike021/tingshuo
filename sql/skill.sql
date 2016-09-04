
-- ----------------------------
-- Table structure for skill
-- ----------------------------
DROP TABLE IF EXISTS `skill`;
CREATE TABLE `skill` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` int(11) NOT NULL default 0 comment 'skill type:0-like 1-add gold 2-add time',
  `name` varchar(128) not null default '' comment 'skill name',
  `consume` int(10) not null default 0 comment 'need spend how much gold',
  `effect` int(10) not null default 0 comment 'how will the skill effect the receiver',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

