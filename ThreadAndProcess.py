# coding=utf-8

'''
线程和进程
'''

import os, time, random
from multiprocessing import Pool
from multiprocessing import Process, Queue, Pipe

# def run_proc(name):
#     print 'Child process %s(%s) runing' % (name,os.getpid())
#
# if __name__=='__main__':
#     print 'Process %s start.' %(os.getpid())
#     i = 0
#     for i in range(5):
#         p = Process(target=run_proc,args=str(i))
#         p.start()
#         p.join()
#
#     print 'Process End.'

'''
进程池
'''
# def run_task(name):
#     print 'task %s(%s) begin start'%(name,os.getpid())
#     time.sleep(random.random()*3)
#     print 'task %s(%s) end'%(name,os.getpid())
#
# if __name__=='__main__':
#     print 'main %s start'%(os.getpid())
#     pool = Pool(3)
#     for i in range(5):
#         pool.apply_async(func=run_task,args=str(i))
#     pool.close()
#     pool.join()
#     print 'main %s end' % (os.getpid())

'''
多进程间的通信 queue
'''

# def proc_write(queue, urls):
#     print 'Porcess %s is writing...' % (os.getpid())
#     for url in urls:
#         queue.put(url)
#         print 'PUT the url is %s' % url
#         time.sleep(random.random() * 3)
#
#
# def proc_read(queue):
#     print 'Porcess %s is reading...' % (os.getpid())
#     while True:
#         url = queue.get()
#         print 'read the url is %s' % url
#
#
# if __name__ == '__main__':
#     print 'main %s start run...' % (os.getpid())
#     queue = Queue()
#     p1 = Process(target=proc_write, args=(queue, ['url1', 'url2', 'url3', 'url4', 'url5']))
#     p2 = Process(target=proc_write, args=(queue, ['url6', 'url7', 'url8', 'url9', 'url0']))
#     p3 = Process(target=proc_read, args=(queue,))
#     p1.start()
#     p2.start()
#     p3.start()
#
#     p1.join()
#     p2.join()
#     p3.terminate()
#     print 'main %s end...' % (os.getpid())

'''
多进程间的通信 pipe
'''


def proc_write(pipe, urls):
    print 'Porcess %s is writing...' % (os.getpid())
    for url in urls:
        pipe.send(url)
        print 'PUT the url is %s' % url
        time.sleep(random.random() * 3)


def proc_read(pipe):
    print 'Porcess %s is reading...' % (os.getpid())
    while True:
        url = pipe.recv()
        print 'read the url is %s' % url


if __name__ == '__main__':
    print 'main %s Process start...'%os.getpid()
    pipe = Pipe()
    p1 = Process(target=proc_write, args=(pipe[0], ['url1', 'url2', 'url3', 'url4', 'url5']))
    p2 = Process(target=proc_read, args=(pipe[1],))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print 'main %s Process end' % os.getpid()
