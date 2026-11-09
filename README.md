# Timothy Brennan

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
- Presented at **SCORED '26** (OpenSSF Community Day Europe, Prague, October 2026): [watch the talk](https://www.youtube.com/watch?v=im2n_blOmoU)

## 🎓 Verified badges

<!--START_SECTION:badges-->
[![Speaker: OpenSSF Community Day Europe 2026](https://images.credly.com/size/80x80/images/aabe48ec-d181-4101-ac27-af7bcec7eaed/blob)](https://www.credly.com/badges/642dafd5-dca2-42c8-bffd-9d1d997bb6a7)
[![Certified Secure Software Lifecycle Professional (CSSLP)](https://images.credly.com/size/80x80/images/2ca15936-bd13-4db9-86cb-8da72a71d701/image.png)](https://www.credly.com/badges/baade269-535c-4d3e-ac0f-437cdd9ecd4a)
[![AWS Certified Cloud Practitioner](https://images.credly.com/size/80x80/images/00634f82-b07f-4bbd-a6bb-53de397fc3a6/image.png)](https://www.credly.com/badges/d5fb8677-153f-493d-b06a-2a52f3953608)
[![AWS Certified AI Practitioner](https://images.credly.com/size/80x80/images/4d4693bb-530e-4bca-9327-de07f3aa2348/image.png)](https://www.credly.com/badges/cb1f903f-9135-49e0-9f93-5191837bb49d)
[![CompTIA AutoOps+ Certification](https://images.credly.com/size/80x80/images/8211c6cc-1e3c-4f82-98d9-776c4614212f/blob)](https://www.credly.com/badges/ef1804b3-47e8-42e2-b827-8f9179fc0e77)
[![CompTIA Data+ ce](https://images.credly.com/size/80x80/images/eef81318-aaa6-4e40-83bd-d40a6ee27b28/blob)](https://www.credly.com/badges/16eb22ae-d46e-419a-88b3-6df5a8fff1a7)
[![CompTIA SecAI+ Certification](https://images.credly.com/size/80x80/images/7c798dfc-1610-42c6-8729-2b735f88fab0/blob)](https://www.credly.com/badges/4a0a9aa5-5ed5-4c7a-bdaa-4d94fb8b047e)
[![CompTIA Cloud Admin Professional – CCAP Stackable Certification](https://images.credly.com/size/80x80/images/18218ce6-e7d4-4479-9500-b7499645b763/CompTIA_CCAP.png)](https://www.credly.com/badges/d8c39918-fecf-4e69-8790-a9980e4c2e97)
[![CompTIA IT Operations Specialist – CIOS Stackable Certification](https://images.credly.com/size/80x80/images/7f7657b9-4d1b-4b8d-b5ee-5fdf6d7ccd71/04294_CompTIA_Cert_Badges_Specialist_-_CIOS.png)](https://www.credly.com/badges/e15cffab-08a0-4dd4-91df-c1c5a2808761)
[![CompTIA Network+ ce Certification](https://images.credly.com/size/80x80/images/c70ba73e-3c8a-46fa-9d60-4a9af94ad662/blob)](https://www.credly.com/badges/4f0363fb-41eb-4320-88d8-af0a95406499)
[![CompTIA Secure Infrastructure Specialist – CSIS Stackable Certification](https://images.credly.com/size/80x80/images/8090280a-311f-425f-a1cd-a32770b5a444/CompTIA_CSIS.png)](https://www.credly.com/badges/7d297965-c045-4181-8ede-0fa151fb52eb)
[![CompTIA A+ ce Certification](https://images.credly.com/size/80x80/images/f6d62c5d-1e1d-4de6-92ee-8dc8c80b1c7b/blob)](https://www.credly.com/badges/f421a06e-4c08-4035-8242-0dbbb3a951ae)
[![CompTIA Cloud+ ce Certification](https://images.credly.com/size/80x80/images/b2e3c623-cc4a-4f0c-8a3b-aa6231e138fe/blob)](https://www.credly.com/badges/ce1a9960-4a98-448c-9fec-66e27a2aa16b)
[![CompTIA Secure Cloud Professional – CSCP Stackable Certification](https://images.credly.com/size/80x80/images/9f54bf46-dc18-408c-a74e-2637facd1856/CompTIA_CSCP.png)](https://www.credly.com/badges/e8a30a91-9f63-499b-8c05-9ad8c4f6f1bd)
[![CompTIA CySA+ ce Certification](https://images.credly.com/size/80x80/images/dcd99b5b-da24-40a6-9364-62126d590c37/blob)](https://www.credly.com/badges/cc1422d9-1335-4861-96fc-561d116aeca1)
[![CompTIA Security Analytics Professional – CSAP Stackable Certification](https://images.credly.com/size/80x80/images/ba1b8072-8ebe-432c-88e5-05bc809c624a/CompTIA_CSAP.png)](https://www.credly.com/badges/d8a7d4eb-6deb-4869-a3eb-ec9469113510)
[![CompTIA Security+ ce Certification](https://images.credly.com/size/80x80/images/80d8a06a-c384-42bf-ad36-db81bce5adce/blob)](https://www.credly.com/badges/42853aeb-6fe0-4f6b-8308-560de89d793c)
<!--END_SECTION:badges-->

## 🔍 Interests

Open source supply chain security · vulnerability prediction · interpretable ML · DevSecOps · CI/CD automation

## 📫 Connect

- Email: tebrennan@gwu.edu
- ORCID: [0009-0001-6376-410X](https://orcid.org/0009-0001-6376-410X)
