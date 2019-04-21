from qcloud_cos.cos_client import CosClient
from qcloud_cos.cos_request import UploadFileRequest, ListFolderRequest

bucket = u'masonmou'

# 必须是unicode
cos_client = CosClient(1251123904, u'xxxxxxxxxxxxxxxxxxxxxxxxxx', u'xxxxxxxxxxxxxxxxxxxxxxxxx', region="cd")


def lst():
    # 列根目录出所有文件
    req = ListFolderRequest(bucket, u'/')
    for x in cos_client.list_folder(req)['data']['infos']:
        print(x)


def upload():
    # 上传本地文件到根目录
    req = UploadFileRequest(bucket, u'/%s' % filename, u'%s' % path)
    upload_file_ret = cos_client.upload_file(req)

    if upload_file_ret['code'] == 0:
        print('Upload Success!')
    else:
        print('Upload Failed!')