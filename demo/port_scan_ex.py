#!/usr/bin/env python
# coding=utf-8
import nmap
nm = nmap.PortScanner()

nm.scan('127.0.0.1','22-10000')
nm.command_line()
nm.scaninfo()
