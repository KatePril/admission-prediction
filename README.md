## Problem
The admission process is equally important for both universities and applicants.
While universities aim to select the best students, applicants are eager to secure a spot in their dream college.

Universities need an unbiased tool to make the selection process more effective and fair,
while applicants can utilize this tool to estimate their chances of being accepted.

To address this problem, I have trained several classic machine learning models,
including Logistic Regression, Decision Tree, Random Forest, and XGBoost,
and selected the model with the best performance.


## Data

I used the [MBA Admission dataset, Class 2025](https://www.kaggle.com/datasets/taweilo/mba-admission-dataset), which is available for download directly from Kaggle. The exploratory data analysis (EDA) for this dataset is documented in this [notebook](https://github.com/KatePril/admission-prediction/blob/main/notebook.ipynb).

## Models

To select the best-performing model, I trained several models, including Logistic Regression, Decision Tree, Random Forest, and XGBoost, with different parameters. Each model was evaluated using the ROC AUC score. The training and evaluation for all models can be found in the [notebook](https://github.com/KatePril/admission-prediction/blob/main/notebook.ipynb). 

## Final model
The model with the highest ROC AUC score (0.8937) is the [RandomForestClassifier from Scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) library, trained with the following parameters:

- `max_depth=5`
- `n_estimators=80`
- `min_samples_leaf=15`
- `max_features="sqrt"`
- `bootstrap=True`

The training process for the final model is available in the [`train.py`](https://github.com/KatePril/admission-prediction/blob/main/train.py) file, 
and the API source code is provided in the [`predict.py`](https://github.com/KatePril/admission-prediction/blob/main/predict.py) file. 
For the simplier user interaction I also developed a gradio application, source code of which is provided in [`gradio_interface.py`](https://github.com/KatePril/admission-prediction/blob/main/gradio/gradio_interface.py)
