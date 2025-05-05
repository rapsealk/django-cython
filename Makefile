compile:
	python setup.py build_ext --inplace
	# example_cython.cpython-313-aarch64-linux-gnu.so

clean:
	rm ./tutorial/**/*.so
	rm ./tutorial/**/*.c
