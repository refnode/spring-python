# Workaround Makefile for cleanup

RM = rm -rf

.PHONY: clean

bootstrap2.6: distclean
	/usr/bin/python2.6 bootstrap.py
	bin/buildout

bootstrap2.7: distclean
	/usr/bin/python2.7 bootstrap.py
	bin/buildout

clean:
	@find . \( \
		-iname "*.pyc" \
		-or -iname "*.pyo" \
		\) -delete

distclean: clean
	@$(RM) \
		bin/ \
		build/ \
		develop-eggs/ \
		dist/ \
		docs/doctrees/ \
		docs/html/ \
		docs/make.bat \
		docs/Makefile \
		eggs/ \
		parts/ \
		src/*.egg-info/ \
		MANIFEST \
		.installed.cfg
