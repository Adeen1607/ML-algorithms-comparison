Historical saved notebook outputs, **not a fresh rerun**. Ten-fold cross-validation on the 320-row training partition reports LR, LDA and CART at 0.996875 mean accuracy, KNN at 0.993750, and NB and SVM at 0.990625. The separate SVM holdout demonstration reports 0.985 accuracy on a different 50% split. Differences this small on a 400-row sample do not establish a reliable winning algorithm.

| Algorithm | Mean fold accuracy | Fold standard deviation |
|---|---:|---:|
| LR | 0.996875 | 0.009375 |
| LDA | 0.996875 | 0.009375 |
| KNN | 0.993750 | 0.018750 |
| CART | 0.996875 | 0.009375 |
| NB | 0.990625 | 0.020010 |
| SVM | 0.990625 | 0.020010 |
