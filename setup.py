#!/usr/bin/python2
import sys
import glob
from distutils.core import setup

sys.path.append("/usr/share/pygtk/2.0")
sys.path.append("/usr/share/pygobject/2.0")
from dsextras import BuildExt, TemplateExtension, getoutput

#defsdir = getoutput("pkg-config --variable=defsdir pygtk-2.0")

extensions = []

mafw = TemplateExtension(name = "mafw",
                         pkc_name = "mafw",
                         pkc_version = "0.1.2009.28-1",
                         pygobject_pkc = ("mafw-shared", "pygobject-2.0"),
                         sources = ["mafwmodule.c",
                                    "mafw.c",
                                    "mafw-types.c",
                                   ],
                         defs = "mafw.defs",
                         override = "mafw.override",
                         register = "",
#                         register = [defsdir + "/gtk-types.defs",
#                                    defsdir + "/gdk-types.defs",
#                                    defsdir + "/gtk-base.defs",
#                                    ],
#                        extra_compile_args = ["-DMAEMO_CHANGES"],
                        )

extensions.append(mafw)

setup(name = "mafw",
      version = "0.1",
      ext_modules = extensions,
      data_files = [("/usr/share/python-mafw-dev/examples", glob.glob("examples/*.py")),
                    ("/usr/share/python-mafw-dev/defs", glob.glob("defs/*.defs")),
                    ("/usr/share/python-mafw-tests", glob.glob("tests/*.py"))],
      cmdclass = {"build_ext": BuildExt}
     )
