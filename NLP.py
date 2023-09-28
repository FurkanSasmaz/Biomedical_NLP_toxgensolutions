# Import necessary libraries
from Bio import Entrez
import ssl
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk import ne_chunk
import string
from collections import Counter
from itertools import islice
from datetime import datetime
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# Bypass SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# Function to fetch abstracts from PubMed using MeSH terms
def fetch_abstracts_with_date(term, start_date, end_date, max_results=1000):
    """
    Fetch abstracts from PubMed based on search terms.
    
    Parameters:
    term (str): Search term or MeSH term for querying PubMed.
    max_results (int): Maximum number of results to fetch.
    
    Returns:
    list: A list of abstracts fetched from PubMed.
    """
    
    
    # Format the start and end dates for the search query
    start_date = datetime.strptime(start_date, "%Y/%m/%d").date()
    end_date = datetime.strptime(end_date, "%Y/%m/%d").date()
    # Provide contact email for Entrez
    Entrez.email = "info@toxgensolutions.eu"
    
    # Perform the search query using Entrez
    handle = Entrez.esearch(db="pubmed", term=term, mindate=start_date, maxdate=end_date, retmax=max_results)
    
    # Read search results
    record = Entrez.read(handle)
    handle.close()
    
    # Extract PubMed IDs from the search results
    id_list = record["IdList"]
    
    # Check if search returned results
    if not id_list:
        print("No results found.")
        return []
    
    # Fetch abstracts based on PubMed IDs
    handle = Entrez.efetch(db="pubmed", id=id_list, rettype="abstract", retmode="text")
    
    # Read and split the abstracts
    abstracts = handle.read().split("\n\n")
    handle.close()
    
    return abstracts


# Define the search term, e.g., "Cancer Immunotherapy"
search_term = "Cancer Drugs"
start_date = "2010/01/01"
end_date = "2017/09/27"
abstracts = fetch_abstracts_with_date(search_term, start_date, end_date)

#Analyzing using NLP
stop_words = set(stopwords.words('english'))
punctuation_set = set(string.punctuation)

# Initialize WordNet lemmatizer
lemmatizer = WordNetLemmatizer()

# Create a list to store all the lemmatized words
all_words = []
# Display first 5 abstracts for quick inspection (optional)
print("Abstracts:\n")
#NER on the abstracts
for i, abstract in enumerate(abstracts[:50]):
        
    # Define the medicine names
    medicine_name = ["Icotinib"] 
    
     
    # Tokenize the abstract
    tokens = word_tokenize(abstract)
    
    # Perform part-of-speech tagging
    tagged_tokens = pos_tag(tokens)
    
    # Extract medicine names using named entity recognition
    medicine_counts = Counter()
    for i in range(len(tagged_tokens)):
        if tagged_tokens[i][1] == 'NNP' and tagged_tokens[i-1][1] != 'NNP':
            medicine = tagged_tokens[i][0]
            medicine_counts[medicine] += 1
            

    
    # Remove stopwords
    filtered_tokens = [token.lower() for token in tokens if token.lower() not in stopwords.words('english')]
    
    # Remove punctuation
    filtered_tokens = [token for token in filtered_tokens if token.isalpha()]

    # Lemmatize the filtered tokens
    lemmatized_tokens = [lemmatizer.lemmatize(token, wordnet.VERB) for token in filtered_tokens]
    
    # Join the lemmatized tokens back into a string
    lemmatized_abstract = ' '.join(lemmatized_tokens)   
    
    # Add the filtered tokens to the list of all words
    all_words.extend(lemmatized_tokens)
    
    # Perform NER on the tokens
    ner_tags = ne_chunk(nltk.pos_tag(tokens))   
    
    print(f"{i+1}. {lemmatized_abstract}\n")
    # print("------------")
    # print(f"{i+1}. {ner_tags}\n")
    
    # Print the medicine counts
    print("Medicine Counts:")
    for medicine in medicine_name:
        count = medicine_counts.get(medicine, 0)
        print(f"{medicine}: {count}")
    print("")

# Create a word frequency counter
word_counter = Counter(all_words)

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(word_counter)

# Plot the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# Print the first 10 unique words in the word counter
print("Most common words:")
for word, count in word_counter.most_common(20):
    print(f"{word}: {count}")

# Print the unique words in the word counter
print("\nUnique words:")
for word in islice(word_counter.keys(), 10):
    print(word)
    




    
    
    
    
    