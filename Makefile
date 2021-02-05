build:
	esphome firmware.yaml compile

upload: build
	esphome firmware.yaml upload