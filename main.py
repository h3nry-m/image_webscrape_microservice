from os import lseek
import requests
from bs4 import BeautifulSoup
from flask import Flask 

app = Flask(__name__)

@app.route('/get_image/<vegetable>', methods=['GET'])
def get_image(vegetable):
  try: 
    params = {
      "q": f"{vegetable}",
      "tbm": "isch",
      "content-type": "image/png",
  }

    html = requests.get("https://www.google.com/search", params=params)
    soup = BeautifulSoup(html.text, 'html.parser')

    image_link = soup.select('img')[1]['src']
    return {"image-link": image_link}
  except:
    return f"Sorry, unable to find image associated with {vegetable}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)