.PHONY: all clean

all: internal.pdf

clean:
	rm -f bibliography.bib.bbl
	rm -f bibliography.bib.blg
	rm -f internal.aux
	rm -f internal.bbl
	rm -f internal.bcf
	rm -f internal.blg
	rm -f internal.fdb_latexmk
	rm -f internal.fls
	rm -f internal.log
	rm -f internal.out
	rm -f internal.pdf
	rm -f internal.pdf
	rm -f internal.run.xml
	rm -f internal.toc

internal.pdf: bibliography.bib internal.tex
	@pdflatex internal
	@biber internal
	@pdflatex internal
	@pdflatex internal
