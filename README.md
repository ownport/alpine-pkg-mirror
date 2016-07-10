# alpine-pkg-mirror

Alpine package mirror

This simple utility allows you to make selective Alpine package mirrors and update them based on the latest changes

## How-to use

You need just download the latest version of `mirror` for Releases page https://github.com/ownport/alpine-pkg-mirror/releases

```sh
$ ./mirror
Usage: mirror [OPTIONS] COMMAND [ARGS]...

  command line interface to Alpine package mirrorer

Options:
  -c, --config FILENAME  the path to configuration file (.repositories.json)
  --version              Show the version and exit.
  --help                 Show this message and exit.

Commands:
  list    show the list of repositories
  update  update repository(-ies)
```

to get the list of repositories
```sh
$ ./mirror -c .repositories.json list
edge/testing/x86_64: http://dl-cdn.alpinelinux.org/alpine/edge/testing/x86_64/
v3.4/community/x86_64: http://dl-cdn.alpinelinux.org/alpine/v3.4/community/x86_64/
v3.4/main/x86_64: http://dl-cdn.alpinelinux.org/alpine/v3.4/main/x86_64/
v3.3/main/x86_64: http://dl-cdn.alpinelinux.org/alpine/v3.3/main/x86_64/
edge/community/x86_64: http://dl-cdn.alpinelinux.org/alpine/edge/community/x86_64/
```
to update the repository
```sh
./mirror -c .repositories.json update v3.4/main/x86_64
[NEW] http://dl-cdn.alpinelinux.org/alpine/v3.4/main/x86_64/privoxy-3.0.24-r2.apk
[NEW] http://dl-cdn.alpinelinux.org/alpine/v3.4/main/x86_64/libxfixes-5.0.1-r1.apk
[NEW] http://dl-cdn.alpinelinux.org/alpine/v3.4/main/x86_64/libacl-2.2.52-r2.apk
[NEW] http://dl-cdn.alpinelinux.org/alpine/v3.4/main/x86_64/openssl-1.0.2h-r1.apk
[NEW] http://dl-cdn.alpinelinux.org/alpine/v3.4/main/x86_64/libssh2-1.7.0-r0.apk
[NEW] http://dl-cdn.alpinelinux.org/alpine/v3.4/main/x86_64/libintl-0.19.7-r3.apk
[NEW] http://dl-cdn.alpinelinux.org/alpine/v3.4/main/x86_64/libxcb-1.11.1-r0.apk
[NEW] http://dl-cdn.alpinelinux.org/alpine/v3.4/main/x86_64/tiff-4.0.6-r3.apk
[NEW] http://dl-cdn.alpinelinux.org/alpine/v3.4/main/x86_64/libxslt-1.1.29-r0.apk
.....
```

## How-to configure

All Alpine repositories are specified in `.repositories.json` file. The example of configuration file is available by the link: https://github.com/ownport/alpine-pkg-mirror/blob/master/.repositories.json

```json
{
    "v3.3/main/x86_64": {
        "url": "http://dl-cdn.alpinelinux.org/alpine/v3.3/main/x86_64/",
        "packages": [
            "busybox", "curl", "darkhttpd"
        ],
        "mirror-path": "repositories/alpine/v3.3/main/x86_64/"
    }
}
```

## For developers

to be described later
