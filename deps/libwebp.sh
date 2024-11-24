#!/bin/bash

set -eu

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR/libwebp"

WEBP_VERSION=1.3.2
dir_webp=./webp

# download webp source
rm -rf $dir_webp
if [[ ! -f libwebp-${WEBP_VERSION}.tar.gz ]]; then
  curl -L https://storage.googleapis.com/downloads.webmproject.org/releases/webp/libwebp-${WEBP_VERSION}.tar.gz -o libwebp-${WEBP_VERSION}.tar.gz
fi
tar -xzf libwebp-${WEBP_VERSION}.tar.gz
mv libwebp-${WEBP_VERSION} $dir_webp

(
  cd $dir_webp
  ./configure
)
