# Biomedical_NLP_toxgensolutions
NLP-Research-Internship-Assignment-Biomedical-Text-Analysis

Interpretation and usefulness

"Cancer Drugs" was chosen as the topic for the article. The purpose of choosing this topic is to analyze how much the drug "Icotinib" was used in the articles between the years [2010/01/01 - 2017/09/27]. When I printed the first 50 sections of the abstracts (abstracts[:50]) on the console screen via PudMed, it was concluded that the drug "Icotinib" was used in only 1 article in total. While doing these, advanced NLP techniques were applied to the abstract sections obtained beforehand to avoid any errors in the results. The advanced NLP techniques applied are below;
    •	Tokenization
    •	Part-of-speech (POS) tagging
    •	Named entity recognition (NER)
    •	Stopwords
    •	Punctuation
    •	Lemmatization
    •	Word frequency counting
    •	Word cloud generation

  
Methodology
The NLP.py module attached to your question uses several natural language processing (NLP) techniques to analyze abstracts fetched from PubMed. Here is a detailed explanation of each technique:
  •	Tokenization: This technique involves breaking down a text into individual words or tokens. The module uses the word_tokenize() function from the nltk.tokenize module to tokenize the abstracts.
  •	Part-of-speech (POS) tagging: This technique involves assigning a part of speech (e.g., noun, verb, adjective) to each token in a text. The module uses the pos_tag() function from the nltk.tag module to perform POS tagging.
  •	Named entity recognition (NER): This technique involves identifying and classifying named entities (e.g., people, organizations, locations) in a text. The module uses the ne_chunk() function from the nltk module to perform NER.
  •	Stopword removal: This technique involves removing common words (e.g., "the", "and", "a") from a text that do not carry much meaning. The module uses the stopwords corpus from the nltk.corpus module to remove stopwords.
  •	Punctuation removal: This technique involves removing punctuation marks (e.g., periods, commas, question marks) from a text. The module uses the string module to remove punctuation.
  •	Lemmatization: This technique involves reducing words to their base or dictionary form (e.g., "running" to "run"). The module uses the WordNetLemmatizer class from the nltk.stem module to perform lemmatization.
  •	Word frequency counting: This technique involves counting the frequency of each word in a text. The module uses the Counter class from the collections module to count word frequencies.
  •	Word cloud generation: This technique involves creating a visual representation of the most frequent words in a text. The module uses the WordCloud class from the wordcloud module to generate a word cloud.

Evaluation
•	In the developed software, drug names and common words in the summaries obtained as a result of NLP techniques applied on summaries taken from PubMed were visualized to evaluate NLP methods. This visualization was achieved by creating a word cloud based on word frequencies.

Documentation
You can follow the steps below to run the NLP.py module:
  1.	Download and run the NLP.py file. You can download the file from the link below
  2.	Install the necessary libraries. The libraries used in the NLP.py file are:
    •	Bio
    •	ssl
    •	nltk
    •	wordcloud
    •	matplotlib

You can use the following commands to install these libraries:
!pip install biopython
!pip install nltk
!pip install wordcloud
!pip install matplotlib

4.	Run the NLP.py file. You can use the following command to run the file:
  •	python NLP.py


6.	When you run this code, NLP techniques will be applied on abstracts retrieved from PubMed and drug names and the most frequently used words will be visualized.
  •	A word cloud image will be created showing the number of drug names and the most frequently used words.
  •	The first 10 unique words and the 20 most frequently used words will be printed.
  •	The first 5 abstracts will be printed for quick review (optional).
  •	Medication counts will be printed.
  •	Drug names in summaries will be extracted using NER (Named Entity Recognition)



