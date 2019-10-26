
all: ppt.pdf \


ppt.pdf: ppt.tex
	xelatex -shell-escape ppt.tex
	xelatex -shell-escape ppt.tex
	evince ppt.pdf&


.PHONY:clean  
clean:
	-rm -fr *.ps *.dvi *.aux *.toc *.idx *.ind *.ilg *.log *.out *~ *.tid *.tms *.pdf *.bak *.blg *.bbl *.gz *.snm *.nav _minted*

