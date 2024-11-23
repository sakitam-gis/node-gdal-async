#!/bin/bash

set -eu

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

WEBP_VERSION=1.3.2

# 下载并解压 WebP 源码
if [[ ! -f libwebp-${WEBP_VERSION}.tar.gz ]]; then
  curl -L https://storage.googleapis.com/downloads.webmproject.org/releases/webp/libwebp-${WEBP_VERSION}.tar.gz -o libwebp-${WEBP_VERSION}.tar.gz
fi

# 清理并重新解压
rm -rf libwebp
mkdir -p libwebp
tar xf libwebp-${WEBP_VERSION}.tar.gz -C libwebp --strip-components=1
