import argparse
import datetime
import json
import os
import pathlib
import shlex
import subprocess


target_dir = 'jupyters'
lists = []


def file_tree(path=target_dir):
    dirs = os.listdir(path)
    buf_child = []
    root = {
        'path': path,
        'name': '',
        'child': buf_child,
        'timestamp': datetime.datetime.fromtimestamp(pathlib.Path(path).stat().st_ctime).strftime('%Y-%m-%d %H:%M:%S')
    }
    for dir in dirs:
        dir_path = os.path.join(path, dir)
        if os.path.isdir(dir_path):

            child = file_tree(dir_path)
            child['name'] = dir
            buf_child.append(child)
        else:

            buf_child.append({
                'path': dir_path,
                'name': dir,
                'child': [],
                'timestamp': datetime.datetime.fromtimestamp(pathlib.Path(dir_path).stat().st_ctime).strftime('%Y-%m-%d %H:%M:%S')
            })
    return root

def output_list(dirs):

    for dir in dirs:
         if dir["name"].endswith('.ipynb'):
             lists.append([dir["timestamp"], dir["path"], dir["name"]])

         elif len(dir["child"]) != 0:
             output_list(dir["child"])

    return lists


def make_log(fs):
    logs = open('logs.txt', 'w', encoding='UTF-8')
    for f in fs:
        logs.write(str(f) + '\n')

    logs.close()

def exec_converter(params):
    section_path = params[1].replace(target_dir + "/", "").replace(params[2], "")
    if section_path == "":
        section_path = "./"
    subprocess.run(shlex.split(f'python converter.py {params[1]} --site-dir ./ --section {section_path}'))
    # print(params[0], params[1], params[2])


def list_difference(list1, list2):
    for value in list1:
        if value not in list2:
            exec_converter(value)


if __name__ == '__main__':
    subprocess.run(shlex.split('find ./ -type d -name ".ipynb_checkpoints" -prune -exec rm -rf {} +;'))

    prs = argparse.ArgumentParser(description='convert to markdown')
    prs.add_argument('-l', '--list', help='output ipynb list', action='store_true')
    prs.add_argument('-e', '--exec', help='execute convert to markdown', type=int)
    prs.add_argument('-m', '--make', help='update log file', action='store_true')
    prs.add_argument('-d', '--diff', help='check between jupyters and logs', action='store_true')
    args = prs.parse_args()

    if args.list:
        fs = sorted(output_list([file_tree()]))
        for f in fs:
            print(f[0], f[1])

        print("ipynb files are %s" % (len(fs)))

    elif args.exec:
        fs = sorted(output_list([file_tree()]), reverse=True)
        cnt = 0
        while cnt < args.exec:
            exec_converter(fs[cnt])
            cnt += 1

    elif args.make:
        make_log(sorted(output_list([file_tree()])))

    elif args.diff:
        logs = []
        jps = output_list([file_tree()])
        with open('logs.txt') as f:
            line = f.readline()
            while line:
                logs.append(eval(line))
                line = f.readline()
            f.close()
        list_difference(jps, logs)
        make_log(sorted(output_list([file_tree()])))
