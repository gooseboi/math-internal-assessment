.PHONY: all clean

all: internal.pdf

clean:
	rm -f bibliography.bib.{bbl,blg}
	rm -f internal.{aux,bbl,bcf,blg,fdb_latexmk,fls,log,out,pdf,pdf,run.xml,toc}
	rm -f graphs/*.{pdf,pgf}

internal.pdf: bibliography.bib internal.tex \
			  graphs/exponentialquarterderivative.pdf \
			  graphs/sinquarterderivative.pdf \
			  graphs/polynomialquarterderivative.pdf \
			  graphs/derivativelocal.pdf
	@lualatex internal
	@biber internal
	@lualatex internal
	@lualatex internal

graphs/%.pdf: graphs/%.py
	python3 graphs/$*.py graphs/$*.pdf
