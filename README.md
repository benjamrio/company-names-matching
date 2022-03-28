# Company Name Matching
Match a list of company names written with humans (containing spelling mistakes, non standards names, word inversions, ...) with a list of *lookup* company names. In the context of fuzzy matching, this can be very useful. For example, a user enters his company in a form, and you have to match it with a list of *official names*. Keep in mind that company names are not unique. It is therefore great to use a smaller *lookup* dataset, for exemple a dataset containing client companies of your company or a dataset containing target companies (e.g. S&P500)

## Method
Different methods have been designed and implemented. It depends on the use case, the quality of the data, the size of the datasets.

### Preprocessing
Regular text preprocessing is applied to the company names. You can add or remove operations depending on how strict you want to be.
Being more strict removes the number of erroned matches, but decreases the number of matches.

### TF-IDF NGrams
* Both datasets are transformed in a list of n-grams. A n-gram is list of all consecutive n-characters. For example the 3-grams of `Benjamin` is `["Ben", "enj", "nja", "jam", "ami", "min"]`.
* Such lists build a corpus of *words*. We then compute the term frequency-inverse document frequency list for company name. For each company name, for each of the word in the corpus, the tf-idf reflects the apparition of the word in the name compared to its apparition in whole corpus.
* This allow us to build a vectorized representations of all words. The dimension of each vector is equal to the size of the corpus, that is the number of unique *words* in the datasets.
* We can then compute distances, and find closest vector of an *input* vector in the *lookup* dataset.

### Substring method (Not pushed online yet)
* For each name in the *input* dataset, find the names in *lookup* datasets that is a substring of the input name.
This is particularly useful if the *lookup* dataset

## Use
The project is still under development, and a major part remains to be pushed online. As of right now, please use `predict.ipynb`. The table `siren_table.csv` is the *lookup* dataset. It gives the link between a standard company name and its SIREN number (unique id for french companies). This table has been collected from data.gouv. The table `top500verifCom.tsv` is the *input* table. We wish to know the SIREN identifiers of thes 500 biggest french companies. The table has been optained with a copypasta from [verif](https://www.verif.com/Hit-parade/01-CA/00-Pays/0-France/).
