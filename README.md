# An Analysis of Methods to Combat Leetspeak Content Obfuscation

## Required Installations:
- pyleetspeak - <https://pypi.org/project/pyleetspeak/> 
- transformers - <https://huggingface.co/docs/transformers/installation>

## source code:
1. Leetspeak Translation Algorithm

2. Leetspeak Mining Algorithm
    a. Accuracy tests:
        - folder: accuracy  

        - synthetic data using pyleetspeak accuracy test - 1_testAccuracy.ipynb.  
         Tested on words from commonWords.csv.  
          Result dataset - pyleet_accuracy_result.csv  

        - accuracy test on profanity word list - 2_testProfanity.ipynb,  
        test dataset - profanity_en.csv  
        result dataset - profanity_test_result.csv
        
        - Graph analysis - 3_Accuracy_analysis.ipynb

    b. Social media tests:
        In both twitter and YouTube folder:
        1. 1_test1...Ipynb  is the sentiment analysis test WITHOUT leet mine
        2. 2_train...Ipynb  is the extraction of substitution list
        3. 3_test2...Ipynb  is the sentiment analysis test WITH leet mine
        4. the files ending in ...analysis.ipynb are graph analysis
       5. Trans_YT_Test.ipynb is the sentiment analysis for translation algorithm

## Results:

Alg 2 = leet mining 
Alg 2 Accuracy results - pyleet_accuracy_result.csv, profanity_test_result.csv
Alg 2 Twitter result csv - without leet mine "twitter/test1_result.csv", with leet mine "twitter/test2_result_trial2.csv", overall - "twitter/avg_compare_tweet.csv"
Alg 2 Youtube results csv - without leet mine "youtube/test1_noLeet_setiment_result.csv", with leet mine "youtube/test2_result_yt.csv", overall - "\twitter\youtube_sentiment_analysis.csv"


## Datasets:

most common words - <https://www.kaggle.com/datasets/rtatman/english-word-frequency/> 

Twitter - <https://huggingface.co/datasets/jacksoncsie/Famous-Keyword-Twitter-Replies>

profanity(with leet) - <https://www.kaggle.com/datasets/konradb/profanities-in-english-collection> 

Youtube - <https://huggingface.co/datasets/breadlicker45/youtube-comments-180k> 
