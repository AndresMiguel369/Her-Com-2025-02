
suma.x: sum1i.cpp
	g++ -std=c++23 sum1i.cpp -o sumas.x

data.txt: sumas.x
	./sumas.x

fig.pdf: sum1i.py data.txt
	python sum1i.py

# %.x : %.cpp
#	g++ -std=c++23 $< -o $@