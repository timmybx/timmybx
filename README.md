# Hi, I'm Tim Brennan

**Principal Software Engineer** · **Doctor of Engineering candidate, Cybersecurity Analytics** at The George Washington University (defense scheduled January 2027) · CSSLP

I build practical, explainable, reproducible security analytics tools. My research is on open source software supply chain risk: which public signals carry forward information about where the next security advisories will land.

---

## 🐤 CANARY — doctoral research project

**Live: [canary-score.com](https://canary-score.com)** · **Code: [timmybx/canary](https://github.com/timmybx/canary)**

CANARY (Component Analytics & Near-term Advisory Risk Yardstick) scores open source components by the likelihood that a security advisory will be published for them in the next six months, using only publicly observable project signals. The score is a ranking, not a probability. It is a prioritization aid: point limited security review time at the components most likely to need it.

- Monthly panel of all 2,053 Jenkins plugins, January 2018 to June 2026, from four public data sources (plugin registry and advisories, install statistics, GitHub Archive, Software Heritage)
- Evaluated with a label embargo and rolling-origin backtests, then on a pre-registered out-of-time holdout the model had never seen: ROC-AUC 0.67, with the top-scoring tenth of plugins carrying about four times the base advisory rate
- The honest finding is weak but measurable discrimination, not operational triage. The study also documents how label leakage produced a 0.93 ROC-AUC that fell to chance once training labels were rebuilt as of the forecast date
- Cross-ecosystem check on the 8,000 most downloaded PyPI packages
- Explainable by construction: the champion is a logistic regression over 18 columns, with SHAP for the tree-model runner up
- Open research record: pre-registered protocol, containerized and hash-pinned pipeline, dataset and model artifacts on Zenodo

## 🎓 Verified badges

<!--START_SECTION:badges-->
<!--END_SECTION:badges-->

## 🔍 Interests

Open source supply chain security · vulnerability prediction · interpretable ML · DevSecOps · CI/CD automation

## 📫 Connect

- Email: tebrennan@gwu.edu
- ORCID: [0009-0001-6376-410X](https://orcid.org/0009-0001-6376-410X)
