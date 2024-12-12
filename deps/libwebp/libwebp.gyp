{
  "includes": [
    "../../common.gypi"
  ],
  "targets": [
    {
      "target_name": "libwebp",
      "type": "static_library",
      "sources": [
        # 解码相关源文件
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

        # 编码相关源文件
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

        # DSP 相关源文件（基础实现）
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

        # 实用工具源文件
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
      "defines": [
        "WEBP_USE_THREAD=1",
        # 不要开启包含 .h 文件，会报错
#         "HAVE_CONFIG_H"
      ],
      "direct_dependent_settings": {
        "include_dirs": [
          "webp",
          "webp/src"
        ]
      },
      "conditions": [
        ["target_arch=='x64'", {
          "sources": [
            # x64 架构优化实现
            "webp/src/dsp/alpha_processing_sse2.c",
            "webp/src/dsp/alpha_processing_sse41.c",
            "webp/src/dsp/cost_sse2.c",
            "webp/src/dsp/dec_sse2.c",
            "webp/src/dsp/dec_sse41.c",
            "webp/src/dsp/filters_sse2.c",
            "webp/src/dsp/lossless_sse2.c",
            "webp/src/dsp/rescaler_sse2.c",
            "webp/src/dsp/upsampling_sse2.c",
            "webp/src/dsp/upsampling_sse41.c",
            "webp/src/dsp/yuv_sse2.c",
            "webp/src/dsp/yuv_sse41.c"
          ]
        }],
        ["target_arch=='arm'", {
          "sources": [
            # ARM 架构优化实现
            "webp/src/dsp/alpha_processing_neon.c",
            "webp/src/dsp/cost_neon.c",
            "webp/src/dsp/dec_neon.c",
            "webp/src/dsp/filters_neon.c",
            "webp/src/dsp/lossless_neon.c",
            "webp/src/dsp/rescaler_neon.c",
            "webp/src/dsp/upsampling_neon.c",
            "webp/src/dsp/yuv_neon.c"
          ]
        }],
        ["OS=='win'", {
          "defines": [
            "_CRT_SECURE_NO_DEPRECATE",
            "_CRT_NONSTDC_NO_DEPRECATE",
            "WEBP_USE_WIN32_THREAD=1"
          ],
          "msvs_settings": {
            "VCCLCompilerTool": {
              "ExceptionHandling": 1,
              "AdditionalOptions": [
                "/wd4057",
                "/wd4100",
                "/wd4115",
                "/wd4244",
                "/wd4245",
                "/wd4267"
              ]
            }
          }
        }],
        ["OS=='linux'", {
          "defines": [
            "LINUX",
            "WEBP_USE_PTHREAD=1"
          ],
          "cflags": [
            "-Wall",
            "-fPIC",
            "-O3",
            "-std=c99"
          ],
          "cflags!": [
            "-O2"
          ]
        }],
        ["OS=='mac'", {
          "defines": [
            "DARWIN",
            "WEBP_USE_PTHREAD=1"
          ],
          "xcode_settings": {
            "GCC_SYMBOLS_PRIVATE_EXTERN": "YES",
            "OTHER_CFLAGS": [
              "-fvisibility=hidden",
              "-O3",
              "-std=c99"
            ]
          }
        }]
      ]
    }
  ]
}
