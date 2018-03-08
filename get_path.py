import sys

from os import path

def _base_filename(filename):
    return path.splitext(path.basename(filename))[0]

def _is_package(pckg_path):
    filename = path.join(pckg_path, '__init__.py')
    if path.exists(filename):
        return True
    return False

def run(filename):
    pckg = []

    if _base_filename(filename) != '__init__':
        pckg.append(_base_filename(filename))

    pckg_path = path.dirname(filename)
    while _is_package(pckg_path):
        pckg.append(path.basename(pckg_path))
        pckg_path, old_path = path.dirname(pckg_path), pckg_path
        if pckg_path == old_path:
            break

    return '.'.join(reversed(pckg))


if __name__ == '__main__':
    print(run(sys.argv[1]))