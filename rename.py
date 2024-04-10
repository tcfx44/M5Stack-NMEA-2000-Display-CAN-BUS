import subprocess

Import("env")

env.Replace(PROGNAME="%s" % (str(env["PROGNAME"]).replace("firmware", "NMEA2K_Display")))