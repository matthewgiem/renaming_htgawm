import os
import glob
files = glob.glob('How*')
for file in files:
    if file.split(".")[-1] == 'mkv':
        # os.rename(file, "How to Get Away with Murder {}.mkv".format(file.split(".")[6]))
        pass
    else:
        # print(file)
        os.chdir(file)
        inside = glob.glob("How*")
        # print(inside)
        for new_file in inside:
            # print(new_file)
            if new_file.split(".")[-1] == 'mkv':
                # print(new_file.split("."))
                # os.rename(new_file, "How to Get Away with Murder {}.mkv".format(new_file.split(".")[6]))
                pass
        os.chdir("..")
    # print(file.split("."))
    # os.rename(file, '{}.m{}'.format(file.split('m')[0],file.split("m")[1]))
