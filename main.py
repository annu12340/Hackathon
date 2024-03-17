from flask import Flask, request
from flask_restful import Api, Resource
from flasgger import Swagger

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

# Adding resource to API
api.add_resource(EncodeMessage, '/encode')
api.add_resource(DecodeMessage, '/decode')

if __name__ == '__main__':
    app.run(debug=True)
