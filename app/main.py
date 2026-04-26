from flask import Flask, jsonify, request
from flask_cors import CORS

from app.config import FLASK_DEBUG, FLASK_HOST, FLASK_PORT
from app.services.search_service import SearchService

app = Flask(__name__)
app.config["DEBUG"] = FLASK_DEBUG
CORS(app)

search_service = SearchService()


@app.get("/api/v1/indexer")
def indexer():
    query = request.args.get("query", "").strip()
    mode = request.args.get("type", "page_rank").strip().lower()

    if not query:
        return jsonify({"query": "", "query_results": []})

    return jsonify(search_service.run(query, mode))


if __name__ == "__main__":
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)
