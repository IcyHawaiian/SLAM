import sys
import os

from distutils.cmd import Command
from distutils.core import setup
from distutils.extension import Extension
from sys import platform



# Common flags for both release and debug builds.
#extra_compile_arguments = sysconfig.get_config_var('CFLAGS').split()

extra_compile_arguments = ['-std=c++11', '-O3','-Wall', '-Wextra']
extra_link_arguments = ['-Wl,-undefined,error','-lstdc++']

if platform.startswith('darwin'):
    from distutils import sysconfig
    vars = sysconfig.get_config_vars()
    vars['LDSHARED'] = vars['LDSHARED'].replace('-bundle', '-dynamiclib') #not sure if this is working


here = os.path.abspath(os.path.dirname(__file__))
exec(open(os.path.join(here, 'polyominomodel/_version.py')).read())


class PyTest(Command):
    user_options = []
    pytest_args=''

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
	import shlex
	import pytest
        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)

	

setup(
    name                = 'PolyominoModel',
    version             = __version__,
    author              = 'AS Leonard',
    packages            = ['polyominomodel'],
    cmdclass            = {'test': PyTest},
    author_email        = 'asl47@cam.ac.uk',
    description         = 'Various polyomino methods',
    long_description    = open('README.md').read(),
    license             = 'LICENSE.txt',
    platforms           = ['linux','osx'],
    url                 = 'https://github.com/IcyHawaiian/SLAM',
    ext_modules         = [Extension("polyominomodel.CLAM",sources=['src/graph_methods.cpp','src/graph_analysis.cpp','src/polyomino_wrapper.cpp'],include_dirs = ['src/includes'],extra_compile_args=extra_compile_arguments,extra_link_args=extra_link_arguments,language='c++11')],
    headers             = ['src/includes/graph_analysis.hpp','src/includes/graph_methods.hpp']
)
