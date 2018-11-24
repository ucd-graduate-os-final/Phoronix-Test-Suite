import os
import sys
import shutil
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
        self._magic = str(datetime.datetime.now()).replace(' ', '').replace(':', '').replace('.', '').replace('-', '')
        self._git_name = 'https://github.com/ucd-graduate-os-final/Phoronix-Test-Suite'
        self._git_folder = folder_path
        self._test_suite_path = os.path.join('~', '.phoronix-test-suite', 'test-results')

    def _create_result_name(self, file_name):
        return '{}_{}'.format(file_name, self._magic)

    def run_tests(self):
        # for test in self._tests:
        #     os.system('phoronix-test-suite batch-run {}'.format(test))
        print("All tests completed. ")
        self._move_folder_contents(self._test_suite_path, os.path.join(self._git_folder, self._magic))
        # self._remove_folder_contents(self._test_suite_path)
        self._push_to_git()
        # self._stop_vm_instance()

    def install_tests(self):
        for test in self._tests:
            os.system('phoronix-test-suite install {}'.format(test))

    def _stop_vm_instance(self):
        os.system('sudo shutdown -h now')

    def _move_folder_contents(self, from_path, to_path):
        # try:
        try:
            os.system('mkdir {}'.format(os.path.join(self._git_folder, self._magic)))
        except Exception:
            pass
        os.system('sudo mv {} {}'.format(os.path.join(self._test_suite_path, '*'),
                                         os.path.join(self._git_folder, self._magic)))
            # shutil.copytree(from_path, to_path)
        # except OSError:
        #     print("{} failed to be moved to {}. Do this manually.".format(from_path, to_path))
        # except Exception:
        #     raise Exception("Unknown error occurred. Exiting...")

    # def _remove_folder_contents(self, path):
    #     try:
    #         files = os.listdir(path)
    #         for file in files:
    #             if os.path.isfile(file):
    #                 os.remove(file)
    #             elif os.path.isdir(file):
    #                 os.rmdir(file)
    #     except OSError:
    #         print("{} failed to be deleted. Do this manually".format(path))
    #     except Exception:
    #         raise Exception("Unknown error occured. Exiting...")

    def _push_to_git(self):
        print(self._git_name)
        os.system('git commit {}'.format(self._git_name))
        os.system('git push {}'.format(self._git_name))
        os.system('git pull {}'.format(self._git_name))

path = '~/Phoronix-Test-Suite'
pts = PhoronixTestSuite(path)
if sys.argv[1] == 'install':
    pts.install_tests()
elif sys.argv[1] == 'run':
    pts.run_tests()
else:
    raise Exception("Sorry, your last argument was invalid. Exiting...")