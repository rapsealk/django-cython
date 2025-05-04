from Cython.Build import cythonize
from setuptools import setup

# setup(
#     # ext_modules=cythonize("src/pyx/*.pyx"),
#     # ext_modules=cythonize("example.pyx"),
#     ext_modules=cythonize("braavos/**/*.pyx",
#         # exclude=["config/**", "compose/**"],
#     ),  # , language="c++", compiler_directives={"language_level": "3"}),  # type: ignore[call-arg]  # noqa: E501
#     # find=
# )

setup(ext_modules=cythonize(module_list=["braavos/**/*.pyx"]))
