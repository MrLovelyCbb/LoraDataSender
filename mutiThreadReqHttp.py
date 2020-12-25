import threading, time


def run(num):
    print("子线程%s开始..." % (threading.current_thread().name))
    time.sleep(2)
    print(num)
    time.sleep(2)
    # current_thread  返回一个当前线程的实例
    print("子线程%s结束..." % (threading.current_thread().name))


if __name__ == '__main__':
    print("主线程%s启动..." % (threading.current_thread().name))
    # 创建子线程
    t = threading.Thread(target=run, args=(1,))
    t.start()
    t.join()
    print("主线程%s结束..." % (threading.current_thread().name))
