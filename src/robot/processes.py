from multiprocessing import Process, Lock


class Processes:
    def __init__(self):
        self.method_list = []
        self.process_list = []
        self.results = {}

    def result(self, method_name):
        return self.results[method_name] if method_name in self.results else None

    def create_process(self, method, args):
        self.method_list.append([method, args])

    def wait(self):
        for process in self.process_list:
            process.join()

            self.results[process.name] = process.exitcode

    def run(self):
        for method in self.method_list:
            process = Process(target=method[0], args=method[1], name=method[0].__name__)

            self.process_list.append(process)

        for process in self.process_list:
            process.start()

        self.wait()
