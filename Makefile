compile:
	python setup.py build_ext --inplace
	# example_cython.cpython-313-aarch64-linux-gnu.so

clean:
	$(RM) ./tutorial/quickstart/bin/*.so
	$(RM) ./tutorial/quickstart/bin/*.c
	$(RM) -r ./build
