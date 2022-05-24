import json

class PostsDAO:
    
    def __init__(self, path:str) -> None:
        self.path = path
    
    
    def load_all(self):
        with open(self.path, 'r', encoding="utf-8") as file:
            return json.load(file)
    
    
    def save_all(self, posts):
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(posts, file, indent=4, ensure_ascii=False)
    
    
    def get_by_keyword(self, keyword:str):
        nice_keyword = keyword.strip().lower()
        
        posts_with_keyword = []
        for post in self.load_all():
            if nice_keyword in post["content"].lower():
                posts_with_keyword.append(post)
        return posts_with_keyword
    
    
    def add_new(self, post):

        all_posts = self.load_all()
        all_posts.append(post)
        
        self.save_all(all_posts)

