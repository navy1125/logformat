#!/usr/bin/python2
# -*- coding: utf-8 -*-

import os,sys
import shutil
import datetime
import re
import os
import string
import re,xml.dom.minidom,codecs
from optparse import OptionParser
duplicatenum = 0

def uniqline(inputfile,outputfile):
  src = open(inputfile,"r")
	srclines = src.readlines()
	src.close()
	dst = open(outputfile,"w")
	i = 0
  lines = {}
	for dstline in dstlines:
		tmp = dstline
		tmp = tmp.replace('libgame.LuaRegisterBasic','luaginx.LuaRegisterBasic')
		tmp = tmp.replace('libgame.LuaIsFunction','luaginx.LuaIsFunction')
		tmp = tmp.replace('libgame.DumpPanic','luaginx.DumpPanic')
		tmp = tmp.replace('libgame.CloseLuaEngine','luaginx.CloseLuaEngine')
		tmp = tmp.replace('libgame.ReviewDumpPanic','luaginx.ReviewDumpPanic')
		tmp = tmp.replace('libgame.LuaExecInit','luaginx.LuaExecInit')
		if tmp != dstline:
			changenum = changenum + 1
			dstline = tmp
			if first == True:
				changefilenum = changefilenum + 1
				first = False
		dst.write(dstline)

	dst.close()



def main():
	uniqline("uniq_test_in.txt","uniq_test_out.txt")

main()
