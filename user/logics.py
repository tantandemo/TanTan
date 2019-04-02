import os
from urllib.parse import urljoin

from django.conf import settings

from common import keys
from lib.qiniu import upload_qiniu
from TanTan.config import QN_CLOUD_URL


def save_upload_file(uid, avatar):
    filepath = os.path.join(settings.MEDIA_PATH, keys.AVATAR_NAME % uid)
    with open(filepath, 'wb') as fp:
        for chunk in avatar.chunks():
            fp.write(chunk)
    return filepath

def handle_upload_avatar(user, avatar):
    filename =keys.AVATAR_NAME % user.id
    filepath = save_upload_file(user.id, avatar)

    upload_qiniu(filepath, filename)

    user.avatar = urljoin(QN_CLOUD_URL, filename)
    user.save()

    # return user.avatar

