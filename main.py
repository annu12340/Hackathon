from flask import Flask, request, send_file
from flask_restful import Api, Resource
from flasgger import Swagger
import folium, os
import json
from similarity import matchs
from steganography.encode import encode
from steganography.decode import decode

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

class EncodeMessage(Resource):
    """
    This resource represents an endpoint to encode user message using steganography.
    """

    def post(self):
        """
        Post method to receive hidden text.

        ---
        parameters:
          - name: text
            in: formData
            type: string
            required: true
            description: User input text
        responses:
          200:
            description: Received input text
        """
        hidden_text = request.form.get('text')
        encode("output", hidden_text)
        return {'message': f'Received input description: {hidden_text}'}, 200


class DecodeMessage(Resource):
    def post(self):
        """
        Post method to receive hidden text.

        ---
        parameters:
          - name: path
            in: formData
            type: string
            required: true
            description: Path where the encoded img is present
        responses:
          200:
            description: Received input text
        """

        encoded_img_path = request.form.get('path')
        decoded_msg = decode( encoded_img_path)
        return {'message': f'Decoded msg is {decoded_msg}'}, 200


class Map(Resource):
  def post(self):
    """ 
      Method to display map info

        ---

        responses:
          200:
            description: Saving result in map.html
    """

    json_file_path = os.path.join(os.getcwd(), 'loc.json')
    with open(json_file_path, 'r') as file:
        locations = json.load(file)


    marker = folium.Map(location=[43.001, -78.12], zoom_start=4)
    for loc in locations:
        popup_content = 'Same culprit found here'
        
        folium.Marker([loc["latitude"], loc["longitude"]],
                      popup=popup_content).add_to(marker)

    
    # Save the map as an HTML file
    map_path = os.path.join(os.getcwd(), 'map.html')
    marker.save(map_path, 'map.html')
    return send_file(map_path, mimetype='text/html')

class Match(Resource):
  def post(self):
    """ 
      Return culprits with similar features

        ---
        parameters:
          - name: description
            in: formData
            type: string
            required: true
            description: Give the description
        responses:
          200:
            description: Array of culprits with similar description
    """
        hidden_text = request.form.get('description')
        matchs("output", hidden_text)
        return {'message': f'Received input description: {hidden_text}'}, 200
    


# Adding resource to API
api.add_resource(EncodeMessage, '/encode')
api.add_resource(DecodeMessage, '/decode')
api.add_resource(Map, '/map')

if __name__ == '__main__':
    app.run(debug=True)
