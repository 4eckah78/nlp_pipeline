from flask import jsonify, request

from helpers import get_tokens, search_top_3


def init_routes(app) -> None:
    @app.route("/nlp_pipeline", methods=["POST"])
    def npl_pipeline():
        try:
            data = request.json
            text = data.get("text", "")
            if not text:
                return jsonify({"error": "No text provided"}), 400

            tokens = get_tokens(text)
            return jsonify({"tokens": tokens})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route("/search", methods=["POST"])
    def search():
        try:
            data = request.json
            query = data.get("query", "")
            if not query:
                return jsonify({"error": "No query provided"}), 400

            results = search_top_3(query)
            return jsonify({"results": results})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
