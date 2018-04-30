#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """a very simple logging class."""

    def __init__(self, logfilename):
        """constructor"""
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """creates and entry into log file"""
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """errors are caught and are, themselves, logged."""
        handled = []
        try:
            fhandler = open(self.logfilename, 'a')
            MsgsCounter = 0          
            for index, entry in enumerate(self.msgs):
                fhandler.write(str(entry) + '\n')
                handled.append(index)
                MsgsCounter += 1

            fhandler.close()           
            if MsgsCounter == len(self.msgs):
                for index in handled[::-1]:
                    del self.msgs[index]                      
        except IOError:                    
            EFilehandler = open('ErrorLog.log', 'a')
            EFilehandler.write(str(Exception) + '\n')
            EFilehandler.close()
            raise IOError

        except:
            raise
        finally:
            fhandler.close()
