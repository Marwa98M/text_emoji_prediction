Text-to-Emoji Prediction with MistralAI

Overview
This project utilizes the MistralAI model from Hugging Face to predict emojis based on input text. The model is fine-tuned on a text-to-emoji dataset and is capable of generating emoji predictions for various text inputs. It supports inputs in both Arabic and english. 

Installation
Clone the repository
git clone https://github.com/Marwa98M/text_emoji_prediction.git
Create a new conda environment
conda create -n text_emoji_prediction=3.12
Activate the environment
conda activate text_emoji_prediction
Build the docker image
sudo docker build -t text-emoji-app -f dockerfile .
Run the docker, to deploy it locally
sudo docker run text-emoji-app



Examples
Input Text: "الطقس حار نوعا ما"
Predicted Emojis: 🌞🔥🔥🌞🌞🔥
Input Text: "I had a great day at work!"
Predicted Emojis: 😄🎉👏
