{
  "includes": [
		"../../common.gypi"
	],
  "targets": [
    {
      "target_name": "libwebp",
      "type": "static_library",
      "sources": [
        "webp/src/dec/alpha_dec.c",
        "webp/src/dec/buffer_dec.c",
        "webp/src/dec/frame_dec.c",
        "webp/src/dec/idec_dec.c",
        "webp/src/dec/io_dec.c",
        "webp/src/dec/quant_dec.c",
        "webp/src/dec/tree_dec.c",
        "webp/src/dec/vp8_dec.c",
        "webp/src/dec/vp8l_dec.c",
        "webp/src/dec/webp_dec.c",
        "webp/src/enc/alpha_enc.c",
        "webp/src/enc/analysis_enc.c",
        "webp/src/enc/backward_references_enc.c",
        "webp/src/enc/config_enc.c",
        "webp/src/enc/cost_enc.c",
        "webp/src/enc/filter_enc.c",
        "webp/src/enc/frame_enc.c",
        "webp/src/enc/histogram_enc.c",
        "webp/src/enc/iterator_enc.c",
        "webp/src/enc/picture_enc.c",
        "webp/src/enc/picture_csp_enc.c",
        "webp/src/enc/picture_psnr_enc.c",
        "webp/src/enc/picture_rescale_enc.c",
        "webp/src/enc/picture_tools_enc.c",
        "webp/src/enc/predictor_enc.c",
        "webp/src/enc/quant_enc.c",
        "webp/src/enc/syntax_enc.c",
        "webp/src/enc/token_enc.c",
        "webp/src/enc/tree_enc.c",
        "webp/src/enc/vp8l_enc.c",
        "webp/src/enc/webp_enc.c",
        "webp/src/dsp/alpha_processing.c",
        "webp/src/dsp/cost.c",
        "webp/src/dsp/cpu.c",
        "webp/src/dsp/dec.c",
        "webp/src/dsp/dec_clip_tables.c",
        "webp/src/dsp/enc.c",
        "webp/src/dsp/filters.c",
        "webp/src/dsp/lossless.c",
        "webp/src/dsp/lossless_enc.c",
        "webp/src/dsp/rescaler.c",
        "webp/src/dsp/ssim.c",
        "webp/src/dsp/upsampling.c",
        "webp/src/dsp/yuv.c",
        "webp/src/utils/bit_reader_utils.c",
        "webp/src/utils/bit_writer_utils.c",
        "webp/src/utils/color_cache_utils.c",
        "webp/src/utils/filters_utils.c",
        "webp/src/utils/huffman_utils.c",
        "webp/src/utils/quant_levels_dec_utils.c",
        "webp/src/utils/quant_levels_utils.c",
        "webp/src/utils/random_utils.c",
        "webp/src/utils/rescaler_utils.c",
        "webp/src/utils/thread_utils.c",
        "webp/src/utils/utils.c"
      ],
      "include_dirs": [
        "webp",
        "webp/src"
      ],
      "defines!": [
        "DEBUG"
      ],
      "defines": [
        "WEBP_USE_THREAD=1",
        "HAVE_CONFIG_H"
      ],
      "direct_dependent_settings": {
        "include_dirs": [
          "webp",
          "webp/src"
        ]
      },
      "conditions": [
        ["OS=='win'", {
          "defines": [
            "_CRT_SECURE_NO_DEPRECATE",
            "_CRT_NONSTDC_NO_DEPRECATE",
            "_WIN64",
            "WEBP_USE_WIN32_THREAD=1"
          ]
        }],
        ["OS=='linux'", {
          "defines": [
            "LINUX",
            "WEBP_USE_PTHREAD=1"
          ],
          "cflags": [
            "-Wall",
            "-fPIC"
          ],
          "cflags!": [ "-Wall", "-Wextra" ]
        }],
        ["OS=='mac'", {
          "defines": [
            "DARWIN",
            "WEBP_USE_PTHREAD=1"
          ],
          "xcode_settings": {
            "GCC_SYMBOLS_PRIVATE_EXTERN": "YES",
            "OTHER_CFLAGS": [
              "-fvisibility=hidden"
            ]
          }
        }]
      ]
    }
  ]
}
