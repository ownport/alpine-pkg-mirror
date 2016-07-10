
import os
import urlparse

from utils import get_file
from utils import extract_packages_info


class Repository(object):

    def __init__(self, name, mirror_path,  **kwargs):

        self._name = name
        self._mirror_path = mirror_path
        self._details = kwargs

        if not os.path.exists(self._mirror_path):
            os.makedirs(self._mirror_path)

        self._index_path = os.path.join(self._mirror_path, 'APKINDEX.tar.gz')

    @property
    def url(self):

        return self._details['url']


    @property
    def index_url(self):

        return urlparse.urljoin(self.url, 'APKINDEX.tar.gz')


    def update_index(self):

        get_file(self.index_url, self._index_path)


    def update_packages(self):

        for info in extract_packages_info(self._index_path):
            if not info['package'] in self._details['packages']:
                continue

            file_name = "%s-%s.apk" % (info['package'], info['version'])
            file_path = os.path.realpath(os.path.join(self._mirror_path, file_name))
            file_url = urlparse.urljoin(self.url, file_name)

            if os.path.exists(file_path):
                file_size = os.stat(file_path).st_size
                if file_size == int(info['size']):
                    continue

            yield file_url
            get_file(file_url, file_path)
