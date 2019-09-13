
all: 0.pdf 1.pdf 2.pdf 3.pdf 4.pdf 5.pdf 6.pdf 7.pdf

0.pdf: 0.tex 
	xelatex -shell-escape 0.tex
	xelatex -shell-escape 0.tex
	evince 0.pdf&

1.pdf: 1.tex
	xelatex -shell-escape 1.tex
	xelatex -shell-escape 1.tex
	evince 1.pdf&

2.pdf: 2.tex
	xelatex -shell-escape 2.tex
	xelatex -shell-escape 2.tex
	evince 2.pdf&

3.pdf: 3.tex
	xelatex -shell-escape 3.tex
	xelatex -shell-escape 3.tex
	evince 3.pdf&

4.pdf: 4.tex
	xelatex -shell-escape 4.tex
	xelatex -shell-escape 4.tex
	evince 4.pdf&

5.pdf: 5.tex
	xelatex -shell-escape 5.tex
	xelatex -shell-escape 5.tex
	evince 5.pdf&

6.pdf: 6.tex
	xelatex -shell-escape 6.tex
	xelatex -shell-escape 6.tex
	evince 6.pdf&

7.pdf: 7.tex
	xelatex -shell-escape 7.tex
	xelatex -shell-escape 7.tex
	evince 7.pdf&

.PHONY:clean  
clean:
	-rm -f *.soc *.ps *.dvi *.aux *.toc *.idx *.ind *.ilg *.log *.out *~ *.tid *.tms *.pdf *.bak *.blg *.bbl *.gz *.snm *.nav

