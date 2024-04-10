import subprocess

Import("env")

def get_firmware_specifier_build_flag():
    ret = subprocess.run(["git", "describe", "--tags", "--always", "--dirty"], stdout=subprocess.PIPE, text=True) #Uses any tags
    build_version = ret.stdout.strip()
    return (build_version)

build_version = get_firmware_specifier_build_flag()

build_flag = "-D GIT_REVISION=\\\"" + build_version + "\\\""
print ("Firmware Revision: " + build_version)


env.Append(
    BUILD_FLAGS=[build_flag]
)

env.Replace(PROGNAME="firmware_%s" % build_version.replace(':', '_'))