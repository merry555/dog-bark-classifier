# dog-bark-classifier

Goal: categorize types of dog barks. 

TODO: everything.

## Data Collection

I used Google's AudioSet to get the different types of dog barks
- [Bark](https://research.google.com/audioset/ontology/bark_1.html): these are communicative barks.
- [Whimper](https://research.google.com/audioset/ontology/whimper_dog_1.html): these barks are used to communicate fear or pain.
- [Yip](https://research.google.com/audioset/ontology/yip_1.html): higher pitched bark or cry
- [Howl](https://research.google.com/audioset/ontology/howl_1.html): longer cries
- [Growling](https://research.google.com/audioset//dataset/growling.html): used for anger, agression, or warning.
- [Bow Wow](https://research.google.com/audioset/ontology/bowwow_1.html): a more tonal communicative bark.

I found an [ontology json](https://github.com/audioset/ontology/blob/master/ontology.json) to get a list of all urls. 



## Data Pre-processing


- download the videos
- use ffmpeg to convert from webm to wav

## Model Architecture


## Training


## Performance

## Open Questions
- Multimodal. Dogs use body language to communicate too! The same bark can mean [different thingshttps://www.rd.com/list/noises-your-dog-makes/#:~:text=Like%20barking%20and%20howling%2C%20growling,adhered%20to%2C%E2%80%9D%20says%20Dr.) depending on the context. How  can this information be incorporated?

## Resources
