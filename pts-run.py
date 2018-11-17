import os
import datetime


class PhoronixTestSuite:
    def __init__(self):
        self._tests = ['blogbench', 'c-ray', 'cachebench', 'dacapobench', 'dolfyn', 'glibc-bench',
                       'himeno', 'hmmer', 'hpcg', 'iperf', 'lammps', 'm-queens', 'mcperf',
                       'mrbayes', 'namd', 'netperf', 'osbench', 'pjdfstest', 'polybench-c',
                       'primesieve', 'psstop', 'sample-program', 'schbench', 'startup-time', 'stockfish',
                       'sysbench', 'systemd-boot-kernel', 'systemd-boot-total', 'systemd-boot-userspace-1.0.1',
                       'tachyon']
        self._magic = str(datetime.datetime.now()).replace(' ', '').replace(':', '').replace('.', '').replace('-', '')

    def _create_result_name(self, file_name):
        return '{}_{}'.format(file_name, self._magic)

    def run_tests(self):
        for test in self._tests:
            file_name = os.path.join('~/phoronix-test-suite', 'test_results', self._create_result_name(test))
            os.system('phoronix-test-suite batch-run {} {}'.format(test, file_name))
            self._stop_vm_instance()
        print("All tests completed. ")
        self._stop_vm_instance()

    def install_tests(self):
        for test in self._tests:
            os.system('phoronix-test-suite install {}'.format(test))

    def _stop_vm_instance(self):
        os.system('sudo shutdown -h now')


pts = PhoronixTestSuite()
pts.run_tests()
