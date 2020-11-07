from flask import Flask, render_template
import random

app = Flask(__name__)

original_questions = {
   #Format is 'question':[options]
   "There are 17-floors in apartmant. On the first floor there are only 4 people living, \
   but the more you gohigher, the more the number of people is increasing in double. \
   So, which number of the elevator is being pushed the most each day?": ['First floor', 'Last floor', 'Middle floor', 'All floors are equal'],

   "In the lake there are 30 hungry Sharks that eat each other constantly.\
   A Shark is full when he ate 3 other sharks hungry or full. \
   What number of sharks will have eaten totally 3 of them in the end?": ['9', '7', '2', '0'],

   "George, Andrey and Sasha - friends. George is real brother of Andrey.\
   Andrey is real brother of Sasha. But is not their brother. Why?": ['She is girl', 'He is UFO', 'He hates them both', 'It was a trick'],

   "100 students learned English and German languages simultoneously. \
   At the end of course they give an exam which showed that 10 of them could not pass neither English \
   nor German subject. From others who left, 75 passed German and 83 passed English \
   How many of students know both languages?": ['68', '75', '88', '10'],

   "There are a group of Caterpillars going on. One is ahead, two are behind.\
   One is behind, two are ahead and one is between. How many of them in a group?": ['3', '2', '4', '5'],

   "Which one is heavier, 1kg of Cotton or 1kg of Iron?": ['Equal', 'Iron', 'Cotton', 'None'],

   "Three huge Chickens can eat three fattest Caterpillars in three minutes. \
   How much time would it take if thirty Chickens were about to eat thirty Caterpillars?": ['3', '5', '10', '30'],

   "The treasure hunter made his way to an uninhabited island in the Caribbean using an old map. \
   He wandered for several hours in the dense tropics, untill he came across a tribe of local Aborigens. \
   The tribal elder decided to kill the intruder immediately, but first decided to mock him. \
   The treasure hunter could only say the last phrase in his life. If it turns out to be true, \
   then he will be thrown from the mountain onto rocky shore. If the phrase turns out to be lie, \
   the wanderer will be torn apart by lions. However, the treasur hunter managed to escape. \
   What was his phrase after which the elder was forced to release the treasure hunter???": ['I am being torn apart by lions', 'I want to jump from mountains to rocky shore', 'I am sorry', 'I do not want to die'],

   "In the room there are four corners and at each corner there is a cat. \
   In front of each cat there are 3 cats. How many cats are there in total?": ['4', '16', '12', '3'],

   "Alex's grandfather was going home on foot on a sunny and beautiful day.\
   And suddenly rain started pouring and he went home soaking wet.\
   But when he got home not a single hair on his head got wet, Why?": ['He had\'t any', 'He was ill', 'He ran too fast', 'He met a friend'],

   "Two children can create two bicycles in two hours.\
   How many children required to create 12 bicycles in 6 hours?": ['4', '2', '3', '5'], 

   "You were given this, and it belongs to you now. You have never passed it on to anyone,\
   but all your friends use it. What is it?": ['Name', 'Skill', 'Age', 'Ability'],

   "I never was, am always to be. Noone ever saw me, nor ever will, and yet i am the confidence of all,\
   Who am I ???": ['Future', 'Earth', 'Sun', 'Air']
}

@app.route('/')
def main():
   for key, value in original_questions.items():
      random.shuffle(value)
   quest = original_questions
   return render_template('main.html', quest = quest)



if __name__=='__main__':
   app.run(debug=True)

