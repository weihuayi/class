pdf: *.pdf

*.pdf: *.tex 
	xelatex *.tex
	xelatex *.tex
	evince *.pdf&

view:
	evince *.pdf&

.PHONY:clean  
clean:
	-rm -f *.ps *.dvi *.aux *.toc *.idx *.ind *.ilg *.log *.out *~ *.tid *.tms *.pdf *.bak *.blg *.bbl

