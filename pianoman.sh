#!/bin/bash

python hardware/camera_test.py
python omr/binarize.py
python omr/truncate.py
python tf-end-to-end/ctc_predict.py -image ./omr/images/truncated.png -model ./tf-end-to-end/Models/semantic_model.meta -vocabulary ./tf-end-to-end/Data/vocabulary_semantic.txt > music_ir/ir_csv/input.txt
python music_ir/omr_to_csv.py
python hardware/pianoman.py
