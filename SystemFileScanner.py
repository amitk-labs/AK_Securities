import glob
import time
import sys
import os

os_name = sys.platform
partition = []
version = []
files = []


def partitions(sfsFolder):
    global partition
    big = 65

    if "win" in os_name:
        for i in range(26):
            try:
                if glob.glob(str(chr(big + i)) + ":\\"):
                    print("Successfully found partition: " + str(chr(big + i)))
                    partition.append(str(chr(big + i)) + ":\\")
            except:
                continue
        return inds(sfsFolder)
    if "win" not in os_name:
        return inds(sfsFolder)


def inds(sfsFolder):
    global version
    global files

    if "win" in os_name:
        version2 = glob.glob("\\*")
    else:
        version2 = glob.glob("//*")
    version_tmp = []
    x = 1

    if "win" in os_name:
        for ind in range(len(partition)):
            # print(partition[ind])
            while version2 != []:
                version2 = glob.glob(partition[ind] + "\\*"*x)
                for i in range(len(version2)):
                    version.append(version2[i])
                x += 1
            x = 1

        for i in range(len(version)):
            if "." in version[i]:
                files.append(version[i])
        for i in range(len(version)):
            if not os.path.isfile(version[i]):
                version_tmp.append(version[i])
        version = version_tmp
        i = 0
        f = open(sfsFolder, "w")
        for i in range(len(files)):
            f.write(files[i] + "\n")
        f.close()
        time.sleep(3)

    if "win" not in os_name:
        while version2 != []:
            version = glob.glob("//*" * x)
            for i in range(len(version2)):
                version.append(version2[i])
            x += 1
        x = 1

        for i in range(len(version)):
            if "." in version[i]:
                files.append(version[i])
        for i in range(len(version)):
            if not os.path.isfile(version[i]):
                version_tmp.append(version[i])
        version = version_tmp
        i = 0
        f = open(sfsFolder, "w")
        for i in range(len(files)):
            f.write(files[i] + "\n")
        f.close()
        time.sleep(3)
