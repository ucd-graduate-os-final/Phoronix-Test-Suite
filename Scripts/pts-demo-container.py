import os
import sys

if(len(sys.argv)) != 4:
    raise Exception("This file takes 5 arguments. Exiting...")


class PhoronixTestSuite:
    def __init__(self, folder_path, test_name, num_runs):
        self._tests = ['osbench', 'polybench-c']
        self._test_name = test_name
        self._num_runs = int(num_runs)
        self._git_name = 'https://github.com/ucd-graduate-os-final/Phoronix-Test-Suite'
        self._git_folder = folder_path
        self._test_suite_path = "/var/lib/phoronix-test-suite/test-results"
        self._final_results_path = os.path.join(self._git_folder, self._test_name)

    def run_tests(self):
        self._stach_git()
        if not os.path.exists(self._final_results_path):
            os.mkdir(self._test_name)
        else:
            raise Exception("It looks like this path already exists. Are you sure you want to re-run these tests?")
        for i in range(self._num_runs):
            for test in self._tests:
                os.system('phoronix-test-suite batch-run {}'.format(test))
            print("All tests completed. ")
            self._move_folder_contents(self._test_suite_path,
                                       os.path.join(self._final_results_path, '{}-run{}'.format(self._test_name, i)))
            os.system('python Scripts/rename-script.py {}'.format(self._final_results_path))
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

path = '/pts_project'
name = sys.argv[1]
runs = sys.argv[2]
pts = PhoronixTestSuite(path, name, runs)
if sys.argv[3] == 'install':
    pts.install_tests()
elif sys.argv[3] == 'run':
    pts.run_tests()
else:
    raise Exception("Sorry, your last argument was invalid. Exiting...")
