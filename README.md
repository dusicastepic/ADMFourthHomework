# Homework 4

The rendered version of Clustering part of the project (some graphs visible only here)
http://nbviewer.jupyter.org/github/dusicastepic/ADMFourthHomework/blob/master/Clustering%20part.ipynb


The goal of the first part of this project was to do the scrapping of the announcements from the [immobiliare.it](https://www.immobiliare.it) website and do the clustering. In the second part of this project, the aim was to define a hash function that associates a value to each string(from given file with passwords) and checks whether there are some duplicate strings.  


# Clustering

 Steps of project work:

    1. The scrapping of the data from immobiliare.it
    2. Cleaning of the data
    3. Making description (tf_idf values based on the announcement's descriptions) and information data set
       ( values of: price(prezzo), locals(locali), number of bathrooms(bagno), surface(superficie), floor(piano) )
    4. Using k-means++ in elbow method to determine the optimal k (number of clusters) for each data set
    5. Compare clusters and find the 3 most similar ones using Jaccard similarity
    6. Make word clouds for those 3 clusters
  
<p align="center">
<img src="http://www.abc.net.au/reslib/201104/r753424_6267355.JPG" alt text="Clustering">
</p>
 
 

# Hash function

 Steps:

    1. Convert the strings containing the passwords from the file to a (potentially large) number
    2. Use a hash function to map the number to a large range
    3. Find the number of collisions and duplicates
     
 

<p align="center">
<img src="http://learningspot.altervista.org/wp-content/uploads/2016/11/Hash_Function2.png" alt text="Hash function">
</p>
 


The repository consists of the following files:
1. __`Clustering part.ipynb`__: 
     > A Jupyter notebook which provides the code of the Clustering part of the project.
      
            
2. __`Hashing.ipynb`__:
      > A Jupyter notebook which provides the code of the Hashing part of the project.

3. __`Scraper.ipynb`__:
      > A Jupyter notebook which provides the code of the Scrapping data for the clustering implemented in the `Clustering part.ipynb`  notebook.
      
4. __`libscrap.py`__:
      > A python script which provides all the functions used in the `Scraper.ipynb` notebook. 
      
       
