# Homework 4

Rendered version of Clustering part of the project (some graphs visible only here)
http://nbviewer.jupyter.org/github/dusicastepic/ADMFourthHomework/blob/master/Clustering%20part.ipynb


The goal of the first part of this project was to do the scrapping of the announcements from the [immobiliare.it](https://www.immobiliare.it) website and do the clustering. In the second part of this project the aim was to define a hash function that associates a value to each string(from given file with passwords) and check whether there are some duplicate strings.  


# Clustering
## 1) Does basic house information reflect house's description?
    

 You will implement two clustering and compare the results you get. You will need to create two datasets and each of them will be filled by data that you scraped.

 Steps of project work:

	1. Scrapping of the data from immobiliare.it
  2. Clean the data
 	3. Make description(tf_idf based on the announcement's descriptions) and information data set(prezzo, locali, bagno, superficie, bagno)
  4. Using k-means++ and elbow method determine the optimal k(number of clusters) for each data set
  5. Compare clusters and find 3 most similar ones using Jaccard similarity
  6. Make word clouds for those 3 clusters
  
<p align="center">
<img src="http://www.abc.net.au/reslib/201104/r753424_6267355.JPG" alt text="Clustering">
</p>
 
 

# Hash function



<p align="center">
<img src="http://learningspot.altervista.org/wp-content/uploads/2016/11/Hash_Function2.png" alt text="Hash function">
</p>
 


The repository consists of the following files:
1. __`Clustering part.ipynb`__: 
     > A Jupyter notebook which provides the following: 
       Search Engine 1 - Conjunctive query
    	    The first Search Engine evaluated queries based on the `description` and `title` of each document. It also uses inverted index to return the result of the query. Inverted index is in the form of dictionary(key=term_id, value=list of document_ids). 
 
       Search Engine 2 - Conjunctive query & Ranking score
	   In the new Search Engine, given a query, top-k documents related to the query should be returned 
	   sorted based on the calculated _Cosine similarity_  
	   Based on the second inverted index it will return the result of the query. Second inverted index is in the form of		            dictionary(key=term_id, value=list of tuples(doc_id,dict{key=(term,doc_id), value=tf_idf value}). 
	   Afterwards the values were stored and sorted using the heap structure. It was also used to return top-5 houses.
	   
       Search Engine 3 - Conjunctive query & a new score
			
2. __`Hashing.ipynb`__:
      > A python script which provides all the functions used in the `Homework 3 - group #19.ipynb` notebook. 

3. __`Scraper.ipynb`__:
      > A map that shows the houses in the radius user chose based on the location he entered. The code is in the `Homework 3 - group #19.ipynb` notebook. 
      
4. __`libscrap.py`__:
      > A map that shows the houses in the radius user chose based on the location he entered. The code is in the `Homework 3 - group #19.ipynb` notebook. 
      
      
      

 ![alt text](http://learningspot.altervista.org/wp-content/uploads/2016/11/Hash_Function2.png "Hash function")
    
	 
  
  
  ![alt text](http://www.abc.net.au/reslib/201104/r753424_6267355.JPG "Clustering")

