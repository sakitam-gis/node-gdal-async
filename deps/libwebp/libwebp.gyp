{
  "targets": [
    {
      "target_name": "libwebp",
      "type": "static_library",
      "sources": [
        "webp/src/dec/*.c",
        "webp/src/enc/*.c",
        "webp/src/dsp/*.c",
        "webp/src/utils/*.c"
      ],
      "include_dirs": [
        "webp/src"
      ],
      "direct_dependent_settings": {
        "include_dirs": [
          "webp/src"
        ]
      }
    }
  ]
}
