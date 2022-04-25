#!/usr/bin/env python3

# LIST FILTERS v.1.1
# by Ben Byram-Wigfield
# This will list all Quartz Filters known to the OS. 
# Note that the filter name is an internal value and not necessarily the filename.
# Works with python3


import Quartz as Quartz
from Foundation import NSURL, NSString

def listFilters():
	Filters = (Quartz.QuartzFilterManager.filtersInDomains_(None))
	for eachFilter in Filters:
		print (eachFilter.localizedName(), ':', eachFilter.url().fileSystemRepresentation().decode('UTF-8'))
	return


listFilters()

