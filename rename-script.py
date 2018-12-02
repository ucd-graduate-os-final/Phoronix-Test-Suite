import os
import xmltodict
path = '/Users/johnathanbecker/Dropbox/Documents/School Stuff/UC Denver New Degree/Fall 2018/Operating Systems/' \
       'Phoronix-Test-Suite/nested-vm-tests'
tests = ['blogbench', 'c-ray', 'cachebench', 'dacapobench', 'dolfyn', 'glibc-bench',
                       'himeno', 'hmmer', 'hpcg', 'iperf', 'lammps', 'm-queens', 'mcperf',
                       'mrbayes', 'namd', 'netperf', 'osbench', 'pjdfstest', 'polybench-c',
                       'primesieve', 'psstop', 'sample-program', 'schbench', 'startup-time', 'stockfish',
                       'sysbench', 'systemd-boot-kernel', 'systemd-boot-total', 'systemd-boot-userspace-1.0.1',
                       'tachyon']


paths = os.listdir(path)
results = {}
# Get paths that need name changed
for result in paths:
    if result[0] != '.':
        results[result] = [x for x in os.listdir(os.path.join(path, result))
                           if not x.startswith('.') and x.count('-') == 3]
# Rename top level folder names
for x in results.keys():
    # It always starts out with 'PhoronixTestSuite'
    for y in results[x]:
        final_path = os.path.join(path, x, y, 'composite.xml')
        if os.path.exists(final_path):
            name = ''
            with open(final_path) as fd:
                doc = xmltodict.parse(fd.read())
            try:
                name = doc['PhoronixTestSuite']['Result']
                for item in name:
                    if type(item) != str:
                        name = item['Title']
                    else:
                        name = doc['PhoronixTestSuite']['Result']['Title']
            except Exception as e:
                print("Exception {} happened".format(e))
            os.rename(os.path.join(path, x, y), os.path.join(path, x, name))
        else:
            print("Did not find {}".format(final_path))

# Repackage results in each folder for consumption




