# Computer Vision Assignment

**Name:** Junhyeok Jo
**Student ID:** 2019113634

---

## Overview

* **Dataset:** CIFAR-10 (local `cifar-10-batches-py`)
* **Model:** K-Nearest Neighbors (L2 distance)
* **Preprocessing:** Standardization (feature-wise), no other transforms
* **Metrics:** Accuracy, Precision (macro), Recall (macro), F1 (macro)

---

## Message to Professor

Due to runtime constraints, I completed the work on Google Colab.

1. I first performed KNN using only a train/test split.
2. I then used a train/validation/test split, selected **k** on the validation set, and trained KNN.
3. Finally, using this optimal **k**, I conducted **5-fold cross-validation**.

For each setting, I computed **accuracy**, **precision**, **recall**, and **F1-score**, and produced a final plot of performance.

---

## Experimental Setup

* **Split A:** Train (50k) → Test (10k)
* **Split B:** Train (50k) → Train / Validation (10% of Train Dataset) → Test (10k)
  * Select **k** on validation, retrain on full train, evaluate on test
* **Split C:** 5-fold Cross-Validation on the training set using the selected **k**

---

## Results Summary

### A) Train → Test

| Setting    |    k | Accuracy | Precision (macro) | Recall (macro) | F1 (macro) |
| ---------- | ---: | -------: | ----------------: | -------------: | ---------: |
| Train→Test |    3 |   0.3308 |            0.4336 |         0.3308 |     0.3186 |

### B) Train / Validation / Test

* **Selected k:** `1`, **Validation Accuracy:** `0.3480`

| Setting                      |    k | Test Accuracy | Test Precision | Test Recall | Test F1 |
| ---------------------------- | ---: | ------------: | -------------: | ----------: | ------: |
| Retrain on full train → Test |    1 |        0.3567 |         0.4154 |      0.3566 |  0.3521 |

### C) 5-Fold Cross-Validation (using selected k)

|    k | CV Accuracy (Mean ± Std) |
| ---: | :----------------------: |
|    1 |      0.3410 ± 0.0018     |

**Plot:** *CV Accuracy vs. k* with error bars (std).

---

## Environment

* Google Colab, Python 3.x
* `scikit-learn`, `numpy`, `matplotlib`
