#!/usr/bin/env python  
import json

def testjson():
	result = {}
	result["name"] = "shike";
	result["nick"] = "xizhilang";
	result["age"]  = "32";
	print json.dumps(result);

def testnotice():
	notice = {}
	notice["notice"] = "this is test notice";
	print json.dumps(notice);

