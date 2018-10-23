import sys

from os import path

def run(filename):
    package = []
    base_filename = path.splitext(path.basename(filename))[0]

    if base_filename != '__init__':
        package.append(base_filename)

    package_path = path.dirname(filename)

    while path.exists(path.join(package_path, '__init__.py')):
        package.append(path.basename(package_path))

        package_path, old_path = path.dirname(package_path), package_path

        if package_path == old_path:
            break

    return '.'.join(reversed(package))


if __name__ == '__main__':
    print(run(sys.argv[1]))
