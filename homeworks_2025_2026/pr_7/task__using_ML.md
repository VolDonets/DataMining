# Task Description

## Overall description

In this work, we finally put our prepared, fully numeric datasets to work. 
You will learn the core workflow of machine learning: splitting data, training baseline models, 
evaluating their performance using statistical metrics, and tuning their parameters to achieve the best possible predictive results.

## Detailed description

### N. Make data visualizations

With respect to class in classification problem (distinct color for each dot);
or with respect to value in regression problem (gradient color for each dot) do data visualization
using 2D and 3D PCA, t-SNE, UMAP plots

### I. Data Splitting and Baseline

1. Load your fully cleaned and prepared `.csv` dataset from the previous lab work.
2. Separate your dataset into a feature matrix (`X`) and a target vector (`y`).
3. Use `train_test_split` from `sklearn.model_selection` to split your data into training and testing sets. 
   Use a standard split (e.g., 80% training, 20% testing) and set a `random_state` for reproducibility.
4. Train a simple "baseline" model (e.g., `LogisticRegression` for classification (class prediction), or a `DummyClassifier` 
   to just guess the most frequent class, or `LinearRegression` for regression problem (value prediction)). 
   This gives us a minimum score to beat.

### II. Training Basic Models

1. Select and initialize at least two different basic machine learning models from `scikit-learn` 
   (e.g., `DecisionTreeClassifier`, `KNeighborsClassifier`, `SVC`, or `RandomForestClassifier` (or regression equivalent)).
2. Train (fit) both of these models on your **training** data.
3. Generate predictions using both models on your **testing** data.

### III. Model Evaluation

1. Do not just use simple accuracy! Calculate and display a comprehensive classification report
   (using `classification_report`) for both models to see Precision, Recall, and the F1-Score.
   For regression problem consider MAE (mean absolute error), MSE (mean squared error), RMSE (root MSE) and R2
2. Create a Confusion Matrix for your best-performing model to visualize exactly where the model is making mistakes 
   (True Positives vs. False Positives, etc.). Use `ConfusionMatrixDisplay` or a Seaborn heatmap to make it readable.
3. Compare the training score vs. the testing score for your models to check for signs of overfitting or underfitting.

### IV. `BONUS TASK` (+2)

Use data produced by PCA, t-SNE and UMAP and train used methods & models.
Consider different number of target dimensions.
Make conclusion on applicability of such methods.

## Important

1. Do your work in sections, which is identical to the task.
2. Do NOT train your model on the entire dataset and test it on the same dataset, such works will be worth 0 !!! 
   If you can't work with Jupyter Notebook use .py scripts, but your report should be in a .pdf file. 
   Or just ask for help, I'm not a some kind of monster.
3. Don't forget to leave comments and conclusions.

## How to get max points without personal work presentation

1. **Explain the "Why" in Metrics:** Don't just print the classification report. 
   In a Markdown cell, briefly explain *which* metric matters most for your specific dataset.
   (e.g., "Because I am predicting a rare disease, Recall is more important to me than pure Accuracy, 
   so I chose the model with the highest Recall").
2. **Analyze Overfitting/Underfitting:** Look at your train vs. test scores. 
   Write 1-2 sentences explaining if your model memorized the training data (overfitting) 
   or if it generalized well to the unseen test data.
3. **The Final Verdict:** At the very end of your notebook, write a final conclusion stating definitively which model 
   you would deploy to production and why it won.
