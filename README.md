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

## License

This project is licensed under the GPL-2.0 License.


