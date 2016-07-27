#
# top n demo

img_index=None

top_n:
	./core/top_n_demo.py data/test/ core/data.csv 5 $(img_index) # try img_index=12|16|54 [lol 44]
 

#
# search engine demo

destination_path=core/search_result/

search:
	./core/search_engine_demo.py data/test/ core/data.csv $(destination_path)


#
# similar images demo:

metric=0

similar_tennis:
	./core/similar_demo.py data/test/017029558.jpg data/test/ core/data.csv $(metric) # try metric=0|5|9

similar_music:
	./core/similar_demo.py data/test/000316731.jpg data/test/ core/data.csv $(metric)


#
# other

clean:
	rm -rf core/*.pyc $(destination_path)