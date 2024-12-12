#!/bin/bash

set -eu

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR/libwebp"

WEBP_VERSION=1.4.0
dir_webp=./webp

#
# download webp source
#

rm -rf $dir_webp
if [[ ! -f libwebp-${WEBP_VERSION}.tar.gz ]]; then
    curl -L https://storage.googleapis.com/downloads.webmproject.org/releases/webp/libwebp-${WEBP_VERSION}.tar.gz -o libwebp-${WEBP_VERSION}.tar.gz
fi
tar -xzf libwebp-${WEBP_VERSION}.tar.gz
mv libwebp-${WEBP_VERSION} $dir_webp

# Build configuration
#cd $dir_webp

# Configure with minimal features needed for GDAL
#./configure --enable-static --disable-shared \
#    --disable-gif \
#    --disable-png \
#    --disable-jpeg \
#    --disable-tiff \
#    --disable-libwebpmux \
#    --disable-libwebpdemux \
#    --disable-libwebpdecoder \
#    --disable-sdl \
#    --disable-gl \
#    --disable-threading \
#    --prefix="$DIR/libwebp"

#mkdir ".build"

#./configure --disable-shared --enable-static --prefix="$DIR/libwebp"
#./configure --disable-shared --enable-everything --prefix="$DIR/webp/.build" --libdir="$DIR/webp/.build/lib"

#make
#make install
