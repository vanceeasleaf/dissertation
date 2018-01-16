
main.pdf: main.tex bookcover/bookcover.pdf
	bibtex chapter01/chapter01
	bibtex chapter02/chapter02
	xelatex main.tex
	xelatex main.tex
	xelatex main.tex
	
bookcover/bookcover.pdf: bookcover/bookcover.tex
	make -C bookcover/
.PHONY:clean

clean : 
	rm -r bin