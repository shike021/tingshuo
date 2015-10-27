DROP TABLE IF EXISTS `netflowpkg`;
CREATE TABLE `netflowpkg` (
		`net` 	int(10) unsigned NOT NULL DEFAULT '0' comment "网络类型",
		`pkgtype`	int(10) unsigned not null default 2 comment "包流量",
		`remainder` 	int(10) unsigned NOT NULL DEFAULT '0' comment "剩余包数量",
		`intro` 	varchar(255) NOT NULL DEFAULT '',
		PRIMARY KEY (`net`)
		) ENGINE=MyISAM DEFAULT CHARSET=utf8;

