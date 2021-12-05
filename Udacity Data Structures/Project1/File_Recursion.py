import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    out = []
    file_list = os.listdir(path)
    dir_list = []
    for item in file_list:
        if not os.path.isfile(os.path.join(path, item)):
            #print(str(item) + "here\n")
            dir_list.append(item)

    if len(dir_list) == 0:
        for file in file_list:
            if file.endswith(suffix):
                out.append(file)
        return out

    for dir in dir_list:
        file_list.remove(dir)

    for file in file_list:
        if file.endswith(suffix):
            out.append(file)

    # print(dir_list)
    for dir in [os.path.join(path, x) for x in dir_list]:
        #print('--- ' + dir+'\n')
        out1 = find_files(suffix, dir)
        if out1:
            out.extend(out1)

    return out


# ['t1.c', 'a.c', 'test.c', 'b.c', 'a.c']
print(find_files('.c', '.'))
# ['t1.h', 'a.h', 'b.h', 'a.h']
print(find_files('.h', '.'))
# []
print(find_files('.x', '.'))
