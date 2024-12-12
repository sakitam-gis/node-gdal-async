{
	"includes": [
		"../common.gypi"
	],
	"targets": [
		{
			"target_name": "libgdal_webp_frmt",
			"type": "static_library",
			"sources": [
				"../gdal/frmts/webp/webpdataset.cpp",
        "../gdal/frmts/webp/webpdrivercore.cpp",
        "../gdal/frmts/webp/webp_headers.h",
        "../gdal/frmts/webp/webpdrivercore.h",
			],
			"include_dirs": [
				"../gdal/frmts/webp"
			]
		}
	]
}
