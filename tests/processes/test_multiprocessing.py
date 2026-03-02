import sys

from robot.processes import Processes
from time import sleep


def method_1(p):
    for i in range(40):
        print("multiprocessing method_1 running", p, i)

        sleep(0.05)


def method_2(p):
    for i in range(10):
        print("multiprocessing method_2 running", p, i)

        sleep(0.5)

    sys.exit(0)


def method_3():
    for i in range(30):
        print("multiprocessing method_3 running", i)

        sleep(0.05)

    sys.exit(99)


def test_processes_with_wait():
    processes = Processes()

    processes.create_process(method_1, (999,))
    processes.create_process(method_2, ("text",))
    processes.create_process(method_3, ())

    processes.run()

    assert processes.result("method_1") == 0
    assert processes.result("method_2") == 0
    assert processes.result("method_3") == 99
    assert processes.result("unknown") is None
    assert processes.result(None) is None
