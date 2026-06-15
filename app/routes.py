import io
import json

from flask import Blueprint, Response, request, send_file, jsonify, render_template
from app.metadatabuilder.build_full_metadata import build_metadata
from app.suggestion_management.suggestion_manager import generate_full_suggestion, generate_optional_suggestions
from app.framework_handler.framework_data_manager import list_all_frameworks_with_top_level_entries, list_sub_entries


main = Blueprint('main', __name__)


@main.route('/metadata', methods=['POST'])
def generate_metadata() -> Response:
    data = request.get_json()
    data = json.dumps(build_metadata(data), indent=4)

    file_object = io.BytesIO(data.encode('utf-8'))
    file_object.seek(0)

    return send_file(
        file_object,
        download_name='metadata.json',
        mimetype='application/json',
        as_attachment=True
    )


@main.route('/fullsuggestion', methods=['POST'])
def generate_metadata_with_suggestions() -> Response:
    data = request.get_json()

    return jsonify(generate_full_suggestion(data))


@main.route('/suggestion', methods=['POST'])
def generate_suggestions() -> Response:
    data = request.get_json()

    return jsonify(generate_optional_suggestions(data))


@main.route('/')
def get_landing_page():
    return render_template("index.html")


@main.route('/frameworks')
def get_all_frameworks_with_top_level():
    return jsonify(list_all_frameworks_with_top_level_entries())


@main.route('/subentries', methods=['POST'])
def get_sub_entries():
    data = request.get_json()
    return jsonify(list_sub_entries(data))
