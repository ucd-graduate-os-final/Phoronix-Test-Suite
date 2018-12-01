import os
import sys
import datetime

if(len(sys.argv)) != 2:
    raise Exception("This file takes 3 arguments. Exiting...")


class PhoronixTestSuite:
    def __init__(self, folder_path):
        self._tests = ['blogbench', 'c-ray', 'cachebench', 'dacapobench', 'dolfyn', 'glibc-bench',
                       'himeno', 'hmmer', 'hpcg', 'iperf', 'lammps', 'm-queens', 'mcperf',
                       'mrbayes', 'namd', 'netperf', 'osbench', 'pjdfstest', 'polybench-c',
                       'primesieve', 'psstop', 'sample-program', 'schbench', 'startup-time', 'stockfish',
                       'sysbench', 'systemd-boot-kernel', 'systemd-boot-total', 'systemd-boot-userspace-1.0.1',
                       'tachyon']
        #self._tests = ['himeno']
        self._magic = str(datetime.datetime.now()).replace(' ', '').replace(':', '').replace('.', '').replace('-', '')
        self._git_name = 'https://github.com/ucd-graduate-os-final/Phoronix-Test-Suite'
        self._git_folder = folder_path
        self._test_suite_path = "/root/.phoronix-test-suite/test-results"

    def _create_result_name(self, file_name):
        return '{}_{}'.format(file_name, self._magic)

    def run_tests(self):
        for test in self._tests:
            os.system('phoronix-test-suite batch-run {}'.format(test))
        print("All tests completed. ")
        self._move_folder_contents(self._test_suite_path, os.path.join(self._git_folder, self._magic))
        self._push_to_git()
        #self._stop_vm_instance()

    def install_tests(self):
        for test in self._tests:
            os.system('phoronix-test-suite install {}'.format(test))

    def _stop_vm_instance(self):
        os.system('shutdown -h now')

    def _move_folder_contents(self, from_path, to_path):
        try:
            os.system('mkdir {}'.format(to_path))
        except Exception:
            pass
        os.system('mv {} {}'.format(os.path.join(from_path, '*'), to_path))

    def _push_to_git(self):
        os.system('cd {}'.format(self._git_folder))
        os.system('git add .')
        os.system('git commit -m "{}"'.format('Update Code'))
        os.system('git push origin master')
        os.system('git pull {}'.format(self._git_name))

path = '/root/pts_project'
pts = PhoronixTestSuite(path)
if sys.argv[1] == 'install':
    pts.install_tests()
elif sys.argv[1] == 'run':
    pts.run_tests()
else:
    raise Exception("Sorry, your last argument was invalid. Exiting...")
