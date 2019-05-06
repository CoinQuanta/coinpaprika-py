.PHONY: reqs clean docs 

HELP_FUNC = \
    %help; \
    while(<>) { \
        if(/^([a-z0-9_-]+):.*\#\#(?:@(\w+))?\s(.*)$$/) { \
            push(@{$$help{$$2}}, [$$1, $$3]); \
        } \
    }; \
    print "usage: make [target]\n\n"; \
    for (sort keys %help) { \
        printf("  %-20s %s\n", $$_->[0], $$_->[1]) for @{$$help{$$_}}; \
        print "\n"; \
    }

help:
		@perl -e '$(HELP_FUNC)' $(MAKEFILE_LIST)

reqs:		## Generate requirements.txt using pipreqs
		pipreqs $(shell pwd)

clean:		## Delete package build and artifacts
		rm -rf build/
		rm -rf dist/
		rm -rf *.egg-info

docs:		## Generate documentation
		sphinx-apidoc coinpaprikaAPI/ -o docs/source

#  vim: set ts=4 sw=4 tw=79 noet :
