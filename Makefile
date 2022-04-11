SRC_DIR := src
MAIN := main.py
SAMPLE_DIR := samples
ARGS := -f $(SAMPLE_DIR)/a.mp3

all:
	python3 $(SRC_DIR)/$(MAIN) $(ARGS)

clean: format

format: 
	black $(SRC_DIR)