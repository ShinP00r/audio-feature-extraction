SRC_DIR := src
MAIN := main.py
SAMPLE_DIR := samples
ARGS := -f $(SAMPLE_DIR)/kam_000.aac
PYTHON := python3

all:
	$(PYTHON) $(SRC_DIR)/$(MAIN) $(ARGS)

clean: format

format:
	black $(SRC_DIR)

lint: clean
	$(PYTHON) -m pylint $(SRC_DIR)
