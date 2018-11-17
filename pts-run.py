import os
import sys
import shutil
import datetime

if(len(sys.argv)) != 3:
    raise Exception("This file takes 3 arguments. Exiting...")


class PhoronixTestSuite:
    def __init__(self):
        self._tests = ['blogbench', 'c-ray', 'cachebench', 'dacapobench', 'dolfyn', 'glibc-bench',
                       'himeno', 'hmmer', 'hpcg', 'iperf', 'lammps', 'm-queens', 'mcperf',
                       'mrbayes', 'namd', 'netperf', 'osbench', 'pjdfstest', 'polybench-c',
                       'primesieve', 'psstop', 'sample-program', 'schbench', 'startup-time', 'stockfish',
                       'sysbench', 'systemd-boot-kernel', 'systemd-boot-total', 'systemd-boot-userspace-1.0.1',
                       'tachyon']
        self._magic = str(datetime.datetime.now()).replace(' ', '').replace(':', '').replace('.', '').replace('-', '')
        self._git_name = 'https://github.com/ucd-graduate-os-final/Phoronix-Test-Suite'
        self._git_folder = 'Phoronix-Git-Folder'

    def _create_result_name(self, file_name):
        return '{}_{}'.format(file_name, self._magic)

    def run_tests(self):
        for test in self._tests:
            file_name = self._create_result_name(test)
            file_path = os.path.join('~/phoronix-test-suite', 'test_results', file_name)
            os.system('phoronix-test-suite batch-run {} {}'.format(test, file_path))
            self._move_file(file_path, os.path.join('~/{}'.format(self._git_folder), 'test_results', file_name))
        print("All tests completed. ")
        self._push_to_git()
        self._stop_vm_instance()

    def install_tests(self):
        for test in self._tests:
            os.system('phoronix-test-suite install {}'.format(test))

    def _stop_vm_instance(self):
        os.system('sudo shutdown -h now')

    def _move_file(self, from_path, to_path):
        try:
            shutil.move(from_path, to_path)
        except OSError:
            print("{} failed to be moved to {}. Do this manually.".format(from_path, to_path))
        except Exception:
            raise Exception("Unknown error occurred. Exiting...")

    def _push_to_git(self):
        os.system('git commit {} master'.format(self._git_name))
        os.system('git push {} master'.format(self._git_name))
        os.system('git pull {} master'.format(self._git_name))


pts = PhoronixTestSuite()
if sys.argv[2] == 'install':
    pts.install_tests()
elif sys.argv[2] == 'run':
    pts.run_tests()
else:
    raise Exception("Sorry, your last argument was invalid. Exiting...")