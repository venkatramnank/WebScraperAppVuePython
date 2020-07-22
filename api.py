import os
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from CompleteScraper import CompleteScraper

app=Flask(__name__)
CORS(app)
api=Api(app)

parser=reqparse.RequestParser()


parser.add_argument("content")

class scraper(Resource):
    def post(self):
        args=parser.parse_args()

        
        content=args["content"]
        output=CompleteScraper(content=content)
        return {"Output": output}

api.add_resource(scraper, "/scraper")

if __name__ == "__main__":
    app.run(debug=True)

# In the terminal run "curl http://localhost:5000/scraper -d "content="WHEAT"" -X POST -v"