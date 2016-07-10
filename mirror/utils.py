
import urllib2
import tarfile

APKINDEX_FIELDS = {
    'P': 'package',
    'V': 'version',
    'A': 'architecture',
    'T': 'description',
    'L': 'licence',
    'U': 'project',
    'S': 'size',
    'o': 'origin',
    'm': 'maintaner',
    't': 'build-time',
    'c': 'commit',
    'I': 'installed-size',
}


def get_file(url, filename, timeout=60):

    opener = urllib2.build_opener(urllib2.HTTPHandler)
    request = urllib2.Request(url)
    request.get_method = lambda: 'GET'
    try:
        response = opener.open(request, timeout=timeout)
        if response.code == 200:
            with open(filename, 'w') as target:
                while True:
                    data = response.read(64000)
                    if not data:
                        break
                    target.write(data)

    except urllib2.HTTPError, err:
        print {
                "code": err.getcode(),
                "error_msg": err.msg,
                "headers": dict(err.headers.items()),
                "body": '\n'.join(err.readlines())
        }


def extract_packages_info(filename):

    targz = tarfile.open(filename)
    apkindex = targz.extractfile('APKINDEX')

    pkg_info = dict()

    while True:
        data = apkindex.readline()
        if not data:
            break
        if not data.strip():
            if pkg_info:
                yield pkg_info
                pkg_info = dict()
            continue
        k,v = data.strip().split(':',1)
        pkg_info[APKINDEX_FIELDS.get(k, k)] = v
    if pkg_info:
        yield pkg_info
