import pyinputplus as pyip 
import markovify 

file_path = r'C:\Users\obinna\python story generator\stories.txt'
# Function to read text from a file
def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# Read the text data
file_path = 'your_text_file.txt'  # Replace with your text file path
text = read_text_from_file(r'C:\Users\obinna\python story generator\stories.txt')

# Ensure text is a valid string
if not isinstance(text, str):
    raise TypeError("The text variable must be a string.")

# Build the Markov model
try:
    text_model = markovify.Text(text)
except Exception as e:
    print(f"An error occurred while creating the Markov model: {e}")

# Generate some text
for i in range(5):
    print(text_model.make_sentence())


# load the text corpus 
with open("stories.txt") as f:
    text = f.read()

# Build the Markov model 
text_model = markovify

#Function to get user input
def get_user_input():
    hero_name = pyip.inputStr(prompt="Enter the hero's name:",allowRegexes=[r'^[a-zA]+$'],blockRegexes=[r'\d'])
    villain_name = pyip.inputStr(prompt="Enter the villain's name:",allowRegexes=[r'^[a-zA-Z]+$'],blockRegexes=[r'\d'])
    quest = pyip.inputstr(prompt="Enter the hero's quest(rescue the princess):")
    return hero_name,villain_name,quest 

#Function to generate a story using Markovify 
def generate_story(hero_name, villain_name, quest):
    intro = text_model.make_sentence_with_start("once upon a time")
    middle = text_model.make_sentence()
    end = text_model.make_sentence()
    story =(
        f"{intro} There lived a hero name {hero_name}"
        f"{middle} {hero_name} embarked on a quest to {quest}."
        f"However,the evil{villain_name}sought to thwart {hero_name}'s plans."
    )
    #Replace placeholders with actual names 
    story = story.replace("{Richard}",hero_name)
    story = story.replace("{jones}",villain_name)
    story = story.replace("{quest}",quest)
    return story 

#Main function 
def main():
    hero_name,villain_name,quest = get_user_input()
    story = generate_story(hero_name,villain_name,quest)
    print("\nHere is your fantasy story:")
    print(story)