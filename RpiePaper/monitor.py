#Project: Get status information of the cluster node
#Author: Jiahui Tang
#Date: 2017-06-20

#import the necessary 
import psutil
import time
import datetime
import commands

#the main class
class Monitor(object):
	def __init__(self):
		self.cpu = psutil.cpu_times()
		self.memory = psutil.virtual_memory()
		self.disk = psutil.disk_partitions()
		self.network = psutil.net_io_counters()
		self.user = psutil.users()
		self.boot_time = psutil.boot_time()

	def __str__(self):
		return 'Monitoring node system state.'

	__repr__ = __str__

	def cpu_usage_(self):
		cpu_user = self.cpu.user
		cpu_system = self.cpu.system
		cpu_idle = self.cpu.idle
		cpu_iowait = self.cpu.iowait
		
		cpu_usage = (cpu_user + cpu_system + cpu_iowait) / float(cpu_idle + cpu_user + cpu_system + cpu_iowait)
		
		return cpu_usage

	def memory_usage_(self):
		memory_used = self.memory.used
		memory_total = self.memory.total

		memory_usage = memory_used / float(memory_total)
		
		return memory_usage
		
	def total_time_(self):
		boot_time = self.boot_time
		now_time = time.time()
		
		total_time = (now_time - boot_time) / 60

		return total_time

	@staticmethod
	def cpu_rate_():
		def cpu_r():
			with open('/proc/stat', "r") as f:
				for f_line in f:
					break
			f_line = f_line.split(" ")
			f_line_a = []
			for i in f_line:
				if i.isdigit():
					i = int(i)
					f_line_a.append(i)
			total = sum(f_line_a)
			idle = f_line_a[3]
			
			return total, idle

		total_a, idle_a = cpu_r()
		time.sleep(1)
		total_b, idle_b = cpu_r()
		
		sys_idle = idle_b - idle_a
		sys_total = total_b - total_a
		sys_us = sys_total - sys_idle

		cpu_a = (float(sys_us) / sys_total) * 100
		
		return cpu_a
		

	@staticmethod
	def cpu_temp_():
		with open("/sys/class/thermal/thermal_zone0/temp") as tempFile:
			cpu_temp = tempFile.read()
		
		return float(cpu_temp) / 1000

	@staticmethod
	def gpu_temp_():
		gpu_temp = commands.getoutput('/opt/vc/bin/vcgencmd measure_temp').replace('temp=', '').replace('\'C', '')
		
		return float(gpu_temp) 

monitor = Monitor()
#print monitor.cpu_usage_()
print monitor.cpu_rate_()
print monitor.memory_usage_()
print monitor.total_time_()
print monitor.cpu_temp_()
