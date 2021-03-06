# -*- encoding: utf-8 -*-
##############################################################################
#
#    Acrisel LTD
#    Copyright (C) 2008- Acrisel (acrisel.com) . All Rights Reserved
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################


from acris import threaded
from time import sleep

class ThreadedExample(object):
    @threaded
    def proc(self, id_, num, stall):
        s=num
        while num > 0:
            print("%s: %s" % (id_, s))
            num -= 1
            s += stall
            sleep(stall)
        print("%s: %s" % (id_, s))  
        return s
        
class RetVal(object):
    def __init__(self, name):
        self.name=name
        
    def __call__(self, retval):
        print(self.name, ':', retval)  
            
if __name__ == '__main__':
    te1=ThreadedExample().proc(1, 3, 1)
    te2=ThreadedExample().proc(2, 3, 5)
    
    te1.addCallback(RetVal('te1'))
    te2.addCallback(RetVal('te2'))
    