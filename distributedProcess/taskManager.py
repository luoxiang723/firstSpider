# coding=utf-8
import random, Queue, time
from multiprocessing.managers import BaseManager

# 第一步：建立task_queue 和 result_queue 用来存放任务和结果
task_queue = Queue()
result_queue = Queue()

class Queuemanager(BaseManager):
    pass

# 第二步：把创建的两个队列注册在网络上，利用register方法，callable参数关联了Queue对象
# 将Queue对象在网络中暴露
Queuemanager.register('get_task_queue', callable=lambda: task_queue)
Queuemanager.register('get_result_queue', callable=lambda: result_queue)

# 第三步：绑定端口8081，设置验证口令‘qiye’.这个相当于对象的初始化
manager = Queuemanager(address=('', 8001), authkey='luoxiang')

# 第四步：启动管理，监听信息通道
manager.start()

# 第五步：通过管理实例的方法获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

# 第六步：添加任务
for url in ["ImgageUrl_" + i for i in range(10)]:
    print 'put task %s ...' % (url)
    task.put(url)
print 'try get result...'
for i in range(10):
    print 'result is %s ...' %(result.get(timeout=10))

#关闭管理
manager.shutdown()