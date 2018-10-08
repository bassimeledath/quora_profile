# quora_profile

Mini Quora challenge. I gave myself 24 hours to work with whatever Quora data I could find online. Ended up with:

1. A web scraper that scrapes by quora profile. Looked at some my stats (followers,questions etc.). Created a wordcloud of my questions and answers. Used a pre-trained RNN (textgenRNN) to generate new questions and answers after training it on my existing questions and answers. Results were pretty impressive given the limited data and number of epochs.

2. Worked with quora's question pair challenge dataset. Since I had limited time, I decided to train and evaluate simple models (including my very own naive model), rather than using more complex machine learning and deep learning models. I got decent results with my naive model (better than simply using cosine similarity), with an ROC-AUC score of 0.69 and log-loss score of 1.05. Going forward I would test more complex models, and do more linguistic related transformations. 


