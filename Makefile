# mabozen

# modified on 2014-04-26 21:47:34

ALL: ;

install:
	python setup.py install

mon:
	nodemon --exec "c:/python27/python.exe" setup.py install

test:
	py.test test

benchmark:
	python benchmark/benchmark3.py

nose:
	nosetests -v -x

.PHONY: test  benchmark