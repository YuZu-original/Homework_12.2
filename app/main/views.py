from flask import Blueprint, render_template, request
import logging

from app.main.dao.posts_dao import PostsDAO
from config import POSTS_DATA_PATH

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename="basic.log", level=logging.INFO, encoding="utf-8")

post_dao = PostsDAO(POSTS_DATA_PATH)

@main_blueprint.route('/')
def main_page():
    logging.info("Зашел на главную")
    return render_template("index.html")

@main_blueprint.route('/search')
def search_page():
    search_text = request.args.get('s', "")
    logging.info(f'Поиск по слову: "{search_text}"')
    try:
        posts = post_dao.get_by_keyword(search_text)
        return render_template("post_list.html", posts=posts, search_text=search_text)
    except:
        return "Что-то не так с файлом данных"