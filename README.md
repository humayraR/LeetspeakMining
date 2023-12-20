# LeetspeakMining
Analyzing use of leetspeak in social media

installation requirements:
pyspellchecker
nlkt

most common words - https://www.kaggle.com/datasets/rtatman/english-word-frequency/ 

youtube comments source - https://huggingface.co/datasets/breadlicker45/youtube-comments-180k 
https://huggingface.co/datasets/breadlicker45/youtube-comments-v2 (376k) [might not see good results, because filters might already be in place]

reddit - https://huggingface.co/datasets/HuggingFaceGECLM/REDDIT_comments (7.5 M rows 109gb may be too big)

civil comments - https://huggingface.co/datasets/civil_comments news comments, to see how likely are people to use leetspeak in more formal platforms (might find discriminatory/racist words)

https://huggingface.co/datasets/levalencia/TwitterHateSpeech 
https://huggingface.co/datasets/jacksoncsie/Famous-Keyword-Twitter-Replies *****
https://huggingface.co/datasets/strombergnlp/broad_twitter_corpus/blob/main/README.md 
test

profanity(with leet) - https://www.kaggle.com/datasets/konradb/profanities-in-english-collection . https://huggingface.co/datasets/mmathys/profanity *****
reddit - https://huggingface.co/datasets/SocialGrep/one-million-reddit-jokes
bad words(no leet) - https://data.world/wordlists/dirty-naughty-obscene-and-otherwise-bad-words-in-english
https://huggingface.co/datasets/shawarmas/profanity-filter 

https://huggingface.co/datasets/SocialGrep/top-american-universities-on-reddit
https://huggingface.co/datasets/ksang/TwitchStreams #nothing much found
https://huggingface.co/datasets/breadlicker45/discord_data # not clean.. too many punctuations
https://huggingface.co/datasets/SophieTr/reddit_clean

nsfw sureddits rare already uncensored, no reason why people would use leetspeak, similarly other reddits.., no filters for profanity


found some leet in 
https://huggingface.co/datasets/breadlicker45/youtube-comments-180k # found some leet *****
https://huggingface.co/datasets/civil_comments