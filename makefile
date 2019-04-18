
run: main.py display.py draw.py matrix.py parser.py
	python main.py

gif:
	python gif_main.py

clean:
	rm -f *.pyc
	rm -f *~
