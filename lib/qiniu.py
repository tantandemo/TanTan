from qiniu import Auth, put_file

from TanTan.config import QN_ACCESS_KEY
from TanTan.config import QN_SECRET_KEY
from TanTan.config import QN_BUCKET_NAME


#需要填写你的 Access Key 和 Secret Key
access_key = QN_ACCESS_KEY
secret_key = QN_SECRET_KEY


def upload_qiniu(filepath, filename):
    #构建鉴权对象
    q = Auth(access_key, secret_key)

    #要上传的空间
    bucket_name = QN_BUCKET_NAME

    #上传后保存的文件名 filename

    #生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, filename, 3600)

    #要上传文件的本地路径 filepath
    ret, info = put_file(token, filename, filepath)
    print(info)
