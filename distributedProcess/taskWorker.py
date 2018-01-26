# coding=utf-8

import time
from multiprocessing.managers import BaseManager

#创建类似的QueueManager
class QueueManager(BaseManager):
    pass

#第一步 使用QueueManager注册用于获取Queue的方法名称
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#第二步：连接到服务器：
server_addr = '127.0.0.1'
print 'Connect to server %s ...'%(server_addr)

manager = QueueManager(address=(server_addr,8001),authkey='luoxiang')
manager.connect()

#第三步： 获取Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

#第四步：从task队列获取任务，并把结果写入到result队列
while (not task.empty()):
    image_url = task.get(True,timeout=5)
    print 'run task download %s ...'%(image_url)
    time.sleep(1)
    result.put('%s ...>success '%image_url)

print 'worker exit...'

