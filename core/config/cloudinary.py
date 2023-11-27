import os

import cloudinary
import cloudinary.api
import cloudinary.uploader

cloudinary.config(
    cloud_name=os.environ.get("CLOUDINARY_NAME", None),
    api_key=os.environ.get("CLOUDINARY_API_KEY", None),
    api_secret=os.environ.get("CLOUDINARY_SECRET_KEY", None),
)
