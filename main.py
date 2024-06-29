import os

import google.generativeai as genai
from IPython.display import Image, display
from openai import OpenAI

my_secret1 = os.environ['OPENAI_SECRET_KEY']
client = OpenAI(
    api_key = my_secret1
)

my_secret2 = os.environ['GOOGLE_SECRET_KEY']
genai.configure(api_key=my_secret2)

# Create a new model
def story_ai(msg,sysprompt):
  story_response = client.chat.completions.create(
      model="gpt-4o",
      messages=[{
          "role":"system",
          "content":sysprompt
      },
      {
          "role":"user",
          "content":msg
      }
      ],
      max_tokens=300
  )

  story = story_response.choices[0].message.content
  return story

def art_ai(msg):
  art_response = client.images.generate(
      model="dall-e-3",
      prompt=msg,
      size="1024x1024",
      n=1,
      style="natural"
  )
  art = art_response.data[0].url
  return art

def storybook_ai(msg,sysprompt):
  story = story_ai(msg,sysprompt)
  art = art_ai(story)

  display(Image(url=art))
  print("Story : ",story)

def design_ai(msg):
  design_model = genai.GenerativeModel('gemini-1.5-flash')
  design = design_model.generate_content([f"""
  Craft a fitting prompt for an AI image generator to generatora most fitting cover art for this story: {msg}
  """])
  return design.text

def storybook_ai(msg,sysprompt):
  story = story_ai(msg,sysprompt)
  design = design_ai(story)
  art = art_ai(design)

  display(Image(url=art))
  print("Design : ",design)
  print("Story : ",story)
##


msg = "write a story about a Frog"
sysprompt = """
You are a bestselling author.
You will take in a user's request and create a 100 words story about it.
The story should be suitable for children from 7 to 9 years old.
"""
storybook_ai(msg,sysprompt)