{
  "targets": [
    {
      "target_name": "libwebp",
      "type": "static_library",
      "sources": [
        "libwebp/src/dec/alpha_dec.c",
        "libwebp/src/dec/buffer_dec.c",
        "libwebp/src/dec/frame_dec.c",
        "libwebp/src/dec/idec_dec.c",
        "libwebp/src/dec/io_dec.c",
        "libwebp/src/dec/quant_dec.c",
        "libwebp/src/dec/tree_dec.c",
        "libwebp/src/dec/vp8_dec.c",
        "libwebp/src/dec/vp8l_dec.c",
        "libwebp/src/dec/webp_dec.c",
        "libwebp/src/enc/alpha_enc.c",
        "libwebp/src/enc/analysis_enc.c",
        "libwebp/src/enc/backward_references_enc.c",
        "libwebp/src/enc/config_enc.c",
        "libwebp/src/enc/cost_enc.c",
        "libwebp/src/enc/filter_enc.c",
        "libwebp/src/enc/frame_enc.c",
        "libwebp/src/enc/histogram_enc.c",
        "libwebp/src/enc/iterator_enc.c",
        "libwebp/src/enc/picture_enc.c",
        "libwebp/src/enc/picture_csp_enc.c",
        "libwebp/src/enc/picture_psnr_enc.c",
        "libwebp/src/enc/picture_rescale_enc.c",
        "libwebp/src/enc/picture_tools_enc.c",
        "libwebp/src/enc/predictor_enc.c",
        "libwebp/src/enc/quant_enc.c",
        "libwebp/src/enc/syntax_enc.c",
        "libwebp/src/enc/token_enc.c",
        "libwebp/src/enc/tree_enc.c",
        "libwebp/src/enc/vp8l_enc.c",
        "libwebp/src/enc/webp_enc.c",
        "libwebp/src/dsp/alpha_processing.c",
        "libwebp/src/dsp/cost.c",
        "libwebp/src/dsp/cpu.c",
        "libwebp/src/dsp/dec.c",
        "libwebp/src/dsp/dec_clip_tables.c",
        "libwebp/src/dsp/enc.c",
        "libwebp/src/dsp/filters.c",
        "libwebp/src/dsp/lossless.c",
        "libwebp/src/dsp/lossless_enc.c",
        "libwebp/src/dsp/rescaler.c",
        "libwebp/src/dsp/ssim.c",
        "libwebp/src/dsp/upsampling.c",
        "libwebp/src/dsp/yuv.c",
        "libwebp/src/utils/bit_reader_utils.c",
        "libwebp/src/utils/bit_writer_utils.c",
        "libwebp/src/utils/color_cache_utils.c",
        "libwebp/src/utils/filters_utils.c",
        "libwebp/src/utils/huffman_utils.c",
        "libwebp/src/utils/quant_levels_dec_utils.c",
        "libwebp/src/utils/quant_levels_utils.c",
        "libwebp/src/utils/random_utils.c",
        "libwebp/src/utils/rescaler_utils.c",
        "libwebp/src/utils/thread_utils.c",
        "libwebp/src/utils/utils.c"
      ],
      "include_dirs": [
        "libwebp/src"
      ],
      "direct_dependent_settings": {
        "include_dirs": [
          "libwebp/src"
        ]
      },
      "conditions": [
        ["OS=='win'", {
          "defines": [
            "_CRT_SECURE_NO_DEPRECATE",
            "_CRT_NONSTDC_NO_DEPRECATE"
          ]
        }]
      ]
    }
  ]
}
