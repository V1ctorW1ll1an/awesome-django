import hashlib
import os


def hash_path(string, length=10):
    """
        Generate md5 _hashlib.HASH object,
        return hash string
    """
    m = hashlib.md5()
    m.update(string)
    return m.hexdigest()[:length]


def file_extension(filename):
    """
        return file extension
    """
    _, extension = os.path.splitext(filename)
    if extension.startswith("."):
        return extension.replace(".", "")
    return extension


def image_hash_path(instance, filename):
    """
        return image path hashed
    """
    filename_hash = hash_path(
        filename.encode("utf-8") + str(instance.pk).encode("utf-8")
    )
    return f"images/{filename_hash}.{file_extension(filename)}"


def file_hash_path(instance, filename):
    """
        return file path hashed
    """
    filename_hash = hash_path(
        filename.encode("utf-8") + str(instance.pk).encode("utf-8")
    )
    extension = file_extension(filename)
    return f"files/{extension}/{filename_hash}.{extension}"
