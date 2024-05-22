# Thin-Section-Semantic-Segmentation-Of-Rock-Minerals


## Requirements

- Python 3.7+
- mmsegmentation
- numpy
- pillow
- glob

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install MMSegmentation(It would be advised to use official installiation directions from https://github.com/open-mmlab/mmsegmentation):
    ```bash
    git clone https://github.com/open-mmlab/mmsegmentation.git
    cd mmsegmentation
    pip install -e .
    ```

## Running the Prediction Script

1. Ensure you have your model and config file in the `Model/` directory.
2. Place your example images in the `Example Dataset/` directory.
3. Run the prediction script:
    ```bash
    python predict.py
    ```

This will generate segmentation predictions and save them in the `Predictions/` directory.

## Notes

- The latest model and full dataset are not included due to a TUBİTAK agreement.
- The example dataset is provided for demonstration purposes only.
- Link to paper will be added.
- Link to Trained Model:[![Download](https://img.icons8.com/fluency/48/download.png)](https://drive.google.com/file/d/1-Er1iENJV4wzsQEGFO4pZzu0MbPtG7Ch/view?usp=sharing).

## License

[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)


This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License].