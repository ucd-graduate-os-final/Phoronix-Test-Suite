import os
import xmltodict
path = '/Users/johnathanbecker/Dropbox/Documents/School Stuff/UC Denver New Degree/Fall 2018/Operating Systems/' \
       'Phoronix-Test-Suite/standard-tests'
tests = ['blogbench', 'c-ray', 'cachebench', 'dacapobench', 'dolfyn', 'glibc-bench',
                       'himeno', 'hmmer', 'hpcg', 'iperf', 'lammps', 'm-queens', 'mcperf',
                       'mrbayes', 'namd', 'netperf', 'osbench', 'pjdfstest', 'polybench-c',
                       'primesieve', 'psstop', 'sample-program', 'schbench', 'startup-time', 'stockfish',
                       'sysbench', 'systemd-boot-kernel', 'systemd-boot-total', 'systemd-boot-userspace-1.0.1',
                       'tachyon']


paths = os.listdir(path)
results = {}
for result in paths:
    if result[0] != '.':
        results[result] = [int(x.replace('-', '')) for x in os.listdir(os.path.join(path, result))
                           if not x.startswith('.')]
for x in results.keys():
    name_counter = 0
    for y in results[x]:
        final_folder = '{}-{}-{}-{}'.format(str(y)[0:4], str(y)[4:6], str(y)[6:8], str(y)[8:12])
        final_path = os.path.join(path, x, final_folder, 'composite.xml')
        if os.path.exists(final_path):
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
            os.rename(os.path.join(path, x, final_folder), os.path.join(path, x, name))
        else:
            print("Did not find {}".format(final_path))



