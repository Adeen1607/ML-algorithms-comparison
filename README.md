# ML-algorithms-comparison
used different ML algorithms on the same dataset and plotted them


## Rebuild the reading edition

```bash
python -m pip install -r requirements-research.txt
python scripts/build_research_site.py
```

This renders saved notebook outputs without rerunning model training or external APIs. To refresh findings, run the analysis commands above first, update `reports/research-findings.md`, and rebuild.

<!-- research-edition:start -->
## Research edition

[Research report and final visual results](research/report.md) · [Browser-ready notebook catalogue](research/notebooks.html)

Historical saved notebook outputs, **not a fresh rerun**. Ten-fold cross-validation on the 320-row training partition reports LR, LDA and CART at 0.996875 mean accuracy, KNN at 0.993750, and NB and SVM at 0.990625. The separate SVM holdout demonstration reports 0.985 accuracy on a different 50% split. Differences this small on a 400-row sample do not establish a reliable winning algorithm.

| Algorithm | Mean fold accuracy | Fold standard deviation |
|---|---:|---:|
| LR | 0.996875 | 0.009375 |
| LDA | 0.996875 | 0.009375 |
| KNN | 0.993750 | 0.018750 |
| CART | 0.996875 | 0.009375 |
| NB | 0.990625 | 0.020010 |
| SVM | 0.990625 | 0.020010 |


The `research/` folder contains a professional static reading edition. The Pages workflow deploys it after GitHub Pages is enabled with **GitHub Actions** as the publishing source. Intended URL: `https://adeen1607.github.io/ML-algorithms-comparison/`. Deployment status must be checked in Actions before treating that address as live.

<!-- research-edition:end -->
