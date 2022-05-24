class LoaderDAO:
    
    def check_img_file_type(self, image):
        filename = image.filename
        file_type = filename.split('.')[-1]
        return file_type in ["png", "jpg", "jpeg"]
    
    def save_image(self, image):
        if self.check_img_file_type(image):
            image.save(f"./uploads/images/{image.filename}")
    
    
    def get_url_img(self, image_name):
        if image_name:
            return f"uploads/images/{image_name}"
        return "uploads/images/HAS_NOT_PHOTO.png" #! Не используется в новой версии проекта