import os
import shlex
import subprocess
import sys


def get_bool(config_option):
    return config_option == "yes"


def main():
    # Run the init.sh script, and then delete it
    git_script = "./init.sh"
    cmd = shlex.split(git_script)
    try:
        subp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        out = ""
        err = e
    else:
        out, err = subp.communicate()
        encoding = sys.getfilesystemencoding()
        out = out.decode(encoding, "replace").rstrip()
        err = err.decode(encoding, "replace").rstrip()

    if out and out != "":
        print("init.sh stdout: {}".format(out))
    if err and err != "":
        print("init.sh stderr: {}".format(err))

    try:
        os.remove(git_script)
        pass
    except Exception:
        print("Removing {} Failed".format(git_script))


if __name__ == "__main__":
    main()
