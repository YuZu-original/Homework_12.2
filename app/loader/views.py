from flask import Blueprint, render_template, request
import logging

from app.main.dao.posts_dao import PostsDAO
from app.loader.dao.loader_dao import LoaderDAO
from config import POSTS_DATA_PATH


loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename="log.log", level=logging.INFO, encoding="utf-8")

post_dao = PostsDAO(POSTS_DATA_PATH)
loader_dao = LoaderDAO()

@loader_blueprint.route('/post')
def page_post_form():
    return render_template("post_form.html")


@loader_blueprint.route('/post', methods=['POST'])
def page_post_upload():
    picture = request.files.get("picture", None)
    content = request.form.get("content", None)
    
    if not picture:
        logging.info("Забыл добавить фотографию")
        return "Вы забыли добавить фотографию)"
    if not content:
        logging.info("Забыл добавить текст")
        return "Вы забыли добавить текст)"
    if not loader_dao.check_img_file_type(picture):
        logging.info("Загруженный файл не картинка!")
        return "Загруженный файл не картинка!"
    
    try:
        loader_dao.save_image(picture)
    except:
        logging.error("Не получается сохранить фото")
        return "Не получается сохранить фото"
    post = {
        "pic": loader_dao.get_url_img(picture.filename),
        "content": content
        }
    try:
        post_dao.add_new(post)
    except:
        logging.error("Не получается добавить пост")
        return "Не получается добавить пост"
    return render_template("post_uploaded.html", post=post)
