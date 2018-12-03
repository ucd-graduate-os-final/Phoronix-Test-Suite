import os
import sys
import datetime

if(len(sys.argv)) != 2:
    raise Exception("This file takes 3 arguments. Exiting...")


class PhoronixTestSuite:
    def __init__(self, folder_path):
        self._tests = ['osbench', 'polybench-c']
        self._magic = str(datetime.datetime.now()).replace(' ', '').replace(':', '').replace('.', '').replace('-', '')
        self._git_name = 'https://github.com/ucd-graduate-os-final/Phoronix-Test-Suite'
        self._git_folder = folder_path
        self._test_suite_path = os.path.join('~', '.phoronix-test-suite', 'test-results')

    def _create_result_name(self, file_name):
        return '{}_{}'.format(file_name, self._magic)

    def run_tests(self):
        self._stach_git()
        for test in self._tests:
            os.system('phoronix-test-suite batch-run {}'.format(test))
        print("All tests completed. ")
        self._move_folder_contents(self._test_suite_path, os.path.join(self._git_folder, self._magic))
        self._push_to_git()
        # self._stop_vm_instance()

    def install_tests(self):
        for test in self._tests:
            os.system('phoronix-test-suite install {}'.format(test))

    def _stop_vm_instance(self):
        os.system('sudo shutdown -h now')

    def _move_folder_contents(self, from_path, to_path):
        try:
            os.system('mkdir {}'.format(to_path))
        except Exception:
            pass
        os.system('mv {} {}'.format(os.path.join(from_path, '*'), to_path))

    def _stach_git(self):
        os.system('git config credential.helper store')
        os.system('git config --global user.name "Johnathan Becker"')
        os.system('git config --global user.email "historybuffjb@gmail.com"')
        os.system('cd {}'.format(self._git_folder))
        os.system('git pull {}'.format(self._git_name))
        os.system('git push')
        os.system("git config --global credential.helper 'cache --timeout=86400'")

    def _push_to_git(self):
        os.system('git add -A')
        os.system('git commit -m "{}"'.format('Update Code'))
        os.system('git push')
        os.system('git pull {}'.format(self._git_name))

path = '~/Phoronix-Test-Suite'
pts = PhoronixTestSuite(path)
if sys.argv[1] == 'install':
    pts.install_tests()
elif sys.argv[1] == 'run':
    pts.run_tests()
else:
    raise Exception("Sorry, your last argument was invalid. Exiting...")