import os
import sys
import xmltodict
print(len(sys.argv))
if(len(sys.argv)) != 2:
    raise Exception("This file takes 2 arguments. Exiting...")
path = sys.argv[1]
if not os.path.exists(path):
    raise Exception("Folder {} does not exist. Exiting...".format(path))
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




