
# Integrating Medical Imaging and Genetics for Type 2 Diabetes Risk Assessment

This repository provides computational workflows for integrating medical imaging, genetic information, and clinical characteristics to assess the risk of type 2 diabetes (T2D).

Five major research components are included:

1. **Polygenic Risk Score Construction (Step 1):** Construct polygenic risk scores (PRS) and calculate individual PRS values using genetic data, external GWAS summary statistics, and linkage disequilibrium (LD) reference data.

2. **Medical Image Feature Extraction and Multimodal Integration (Steps 2–4):** Extract imaging features using modality-specific DenseNet121 models, aggregate abdominal ultrasound features using a graph neural network (GNN), and integrate imaging representations with genetic and clinical characteristics.

3. **Multimodal T2D Risk Prediction (Step 5):** Develop and evaluate T2D classification models using XGBoost and TabPFN with integrated multimodal features.

4. **Longitudinal T2D Risk Assessment (Step 6):** Perform longitudinal analyses using Cox proportional hazards models to evaluate associations between baseline risk factors and subsequent T2D status.

5. **Genetic Association and Statistical Inference (Steps 7–9):** Conduct genome-wide association studies (GWAS), Mendelian randomization (MR) analyses, and estimate the effective numbers of independent genetic and phenotypic tests to account for multiple testing.

The repository includes demonstration data, Jupyter notebooks, trained model artifacts, and example outputs.

Due to access restrictions on certain research datasets and supporting resources, most analyses in this repository are provided as demonstration workflows using example data rather than the original study cohort. Nevertheless, to facilitate the application and evaluation of the developed models, we additionally provide selected model weights trained on the original research data, including DenseNet121 and graph neural network (GNN) checkpoints, along with a reconstructed XGBoost model. These study-derived models are provided separately from the models trained using the demonstration dataset. Results obtained from the demonstration workflows should therefore not be interpreted as findings or performance estimates from the original research cohort.


## Repository structure

```text
GitHub/
├── Demo_data/
│   ├── 1-1.Sample_information/
│   ├── 1-2.Sample_image/
│   └── 1-3.Sample_genotype/
├── External_data/
├── Outputs/
├── model_weights/
│   ├── Demo-trained_models/
│   └── Study-trained_models/
├── docs/
├── environments/
├── local_data/
├── 0.Read_demo_data.ipynb
├── 1.Step1_PRS_Construction.ipynb
├── 2-1.Step2_DenseNet_ABD.ipynb
├── 2-2.Step2_DenseNet_BMD_left_hip.ipynb
├── 2-3.Step2_DenseNet_BMD_right_hip.ipynb
├── 2-4.Step2_DenseNet_BMD_spine.ipynb
├── 3.Step3_GNN.ipynb
├── 4.Step4_PRS_Integration_and_Feature_Assembly.ipynb
├── 5-1.Step5_XGBoost.ipynb
├── 5-2.Step5_TabPFN.ipynb
├── 6.Step6_Early_Detection.ipynb
├── 7.Step7_Genetic_Analysis.ipynb
├── 8.Step8_MR.ipynb
├── 9.Step9_Independent_Test_Counts.ipynb
└── README.md
```

Some analyses require external datasets and reference resources that are not distributed with this repository. Specifically, **Step 1** requires GWAS summary statistics and linkage disequilibrium (LD) reference data under `External_data/`, while **Step 8** requires GWAS summary statistics and LD reference files under `local_data/`.

These directories are excluded from Git version control. Users must obtain the required external resources separately and place them in the designated directories according to the instructions provided in the corresponding notebooks.



## Quick Start

### 1. Clone the Repository

Clone the repository and switch to the `First_time_revision` branch using the following commands:

```bash
git clone https://github.com/yjhuang1119/Medical_Image_Risk_Assessment_Model.git
cd Medical_Image_Risk_Assessment_Model
```

All subsequent commands should be executed from the repository's root directory unless otherwise specified.


### 2. Set Up the Environment

The computational environments are managed using Conda. Five environment configuration files are provided in the `environments/` directory to support different components of the analysis workflows.

| Environment file | Environment name | Primary purpose |
|---|---|---|
| `main.yml` | `t2d-main` | General data processing, statistical analyses, and PLINK2 |
| `gpu.yml` | `t2d-gpu` | Deep learning, medical image analysis, XGBoost, TabPFN, and Cox regression |
| `prscsx.yml` | `t2d_prscsx` | PRS-CSx analysis |
| `jointprs.yml` | `t2d_jointprs` | JointPRS analysis |
| `mr.yml` | `t2d-mr` | Mendelian randomization (MR) analysis using R |

**Create the main and GPU environments:**

Run the following commands from the repository root:

```bash
conda env create -f environments/main.yml
conda env create -f environments/gpu.yml
```

**Create additional environments as needed:**

For PRS construction and MR analyses, additional environments can be created using:

```bash
conda env create -f environments/prscsx.yml
conda env create -f environments/jointprs.yml
conda env create -f environments/mr.yml
```

The PRS-CSx, JointPRS, and MR workflows may require additional software installations and external reference resources beyond those specified in the environment files.

In particular, Step 8 requires additional R packages, including TwoSampleMR and MR-PRESSO. Installation instructions are provided in `docs/software_requirements.md`.

GPU-based analyses require a compatible NVIDIA GPU and CUDA software environment. Package compatibility may vary across operating systems and hardware configurations.


### 3. Launch JupyterLab and Select a Kernel

The analysis notebooks can be executed using JupyterLab. The main and GPU environments include `ipykernel`, allowing them to be registered as separate Jupyter kernels.

**Register the Python environments as Jupyter kernels:**

```bash
conda activate t2d-main
python -m ipykernel install --user --name t2d-main --display-name "Python (t2d-main)"

conda activate t2d-gpu
python -m ipykernel install --user --name t2d-gpu --display-name "Python (t2d-gpu)"
```

**Install JupyterLab if it is not already available:**

JupyterLab can be installed in a separate environment to avoid modifying the analysis environments.

```bash
conda create -n t2d-jupyter -c conda-forge python=3.11 jupyterlab -y
```

**Launch JupyterLab from the repository root:**

```bash
conda activate t2d-jupyter
jupyter lab
```

Open the desired notebook and select the appropriate kernel:

- **Python (t2d-main):** General data processing and statistical analyses.
- **Python (t2d-gpu):** Medical image analysis, deep learning, XGBoost, TabPFN, and Cox regression.

The PRS-CSx, JointPRS, and MR workflows use additional software environments, as described in their respective notebooks.

Ensure that the selected kernel matches the software requirements of each notebook before execution.


### 4. Run the Demonstration

The demonstration workflows are organized into sequential analysis steps, with separate notebooks for each component.

**Begin with Step 0:**

Open `0.Read_demo_data.ipynb` to inspect the demonstration dataset, verify the input files, and review the predefined data partitions.

**Run the multimodal prediction workflow (Steps 1–5):**

1. **Step 1 – PRS Construction:** Construct and calculate PRS features using the required genetic and external reference data.
2. **Step 2 – DenseNet121:** Train four modality-specific DenseNet121 models to extract medical imaging features.
3. **Step 3 – GNN:** Train a graph neural network to aggregate abdominal ultrasound image features.
4. **Step 4 – Feature Integration:** Combine imaging representations with genetic and clinical characteristics.
5. **Step 5 – T2D Prediction:** Train and evaluate XGBoost models and perform TabPFN-based prediction using the integrated features.

**Run additional analyses (Steps 6–9):**

Steps 6–9 provide complementary analyses, including Cox proportional hazards modeling, GWAS, Mendelian randomization, and estimation of effective independent tests. These analyses can be performed separately according to the research objectives and do not need to be completed before the multimodal prediction workflow.

Each notebook should be executed using its corresponding computational environment. Some steps require additional software or external reference data that are not included in this repository.

Example results are provided in the `Outputs/` directory, organized by analysis step. Users can compare their results with these outputs to examine the execution of the demonstration workflows.

**Note:** The demonstration models are developed using the provided example data. Study-trained model artifacts are provided separately under `model_weights/Study-trained_models/` and should not be confused with the models trained during the demonstration.


## Demonstration Workflow

To demonstrate the complete multimodal model-development process, we provide a demonstration dataset comprising 100 participants. The dataset is divided into four mutually exclusive subsets:

| Dataset | N | Purpose |
|---|---:|---|
| Training1 | 32 | Train four modality-specific DenseNet121 models for image feature extraction. |
| Training2 | 32 | Train the abdominal GNN and XGBoost models, and provide in-context training data for TabPFN. |
| Validation | 16 | Perform model validation and selection during model development. |
| Testing | 20 | Independently evaluate the final demonstration models using performance metrics, including the area under the ROC curve (AUC) and confusion matrices. |

The demonstration workflow integrates the following data components:

- **Abdominal ultrasound (ABD) images**
- **Bone mineral density (BMD) images:** left hip, right hip, and spine
- **Demographic and clinical characteristics**
- **Genetic information and polygenic risk scores (PRS)**
- **Type 2 diabetes (T2D) outcome labels**

The demonstration follows the model-development procedures used in the original study. The DenseNet121, GNN, and XGBoost models are trained using the demonstration data, while TabPFN uses its pretrained foundation model with demonstration-based in-context learning.

These demonstration-trained models are distinct from the study-trained models provided separately in `model_weights/Study-trained_models/`.


## Notebook Execution Order

The Jupyter notebooks are organized according to the following analysis steps:

| Step | Notebook | Description |
|---|---|---|
| 0 | `0.Read_demo_data.ipynb` | Load and validate the demonstration dataset. |
| 1 | `1.Step1_PRS_Construction.ipynb` | Construct and calculate polygenic risk scores (PRS). |
| 2-1 | `2-1.Step2_DenseNet_ABD.ipynb` | Train a DenseNet121 model for abdominal ultrasound images. |
| 2-2 | `2-2.Step2_DenseNet_BMD_left_hip.ipynb` | Train a DenseNet121 model for left hip BMD images. |
| 2-3 | `2-3.Step2_DenseNet_BMD_right_hip.ipynb` | Train a DenseNet121 model for right hip BMD images. |
| 2-4 | `2-4.Step2_DenseNet_BMD_spine.ipynb` | Train a DenseNet121 model for spine BMD images. |
| 3 | `3.Step3_GNN.ipynb` | Train a graph neural network (GNN) to aggregate abdominal ultrasound image features. |
| 4 | `4.Step4_PRS_Integration_and_Feature_Assembly.ipynb` | Integrate imaging, genetic, and clinical features into a multimodal dataset. |
| 5-1 | `5-1.Step5_XGBoost.ipynb` | Train and evaluate T2D prediction models using XGBoost. |
| 5-2 | `5-2.Step5_TabPFN.ipynb` | Perform T2D prediction and evaluation using TabPFN with in-context learning. |
| 6 | `6.Step6_Early_Detection.ipynb` | Perform early-detection and survival analyses using Cox proportional hazards models. |
| 7 | `7.Step7_Genetic_Analysis.ipynb` | Conduct demonstration genome-wide association analyses (GWAS). |
| 8 | `8.Step8_MR.ipynb` | Conduct Mendelian randomization (MR) analyses. |
| 9 | `9.Step9_Independent_Test_Counts.ipynb` | Estimate the effective numbers of independent genetic and phenotypic tests. |

Users are recommended to begin with Step 0 to inspect and validate the demonstration data. Steps 1–5 cover the multimodal prediction workflow, while Steps 6–9 provide additional survival, genetic, and statistical analyses.

Each notebook contains the corresponding analysis procedures and required configurations. Example results are provided in the `Outputs/` directory, organized by analysis step.


## Multimodal Feature Structure

The multimodal T2D prediction framework integrates imaging-derived representations with demographic, clinical, and genetic characteristics, resulting in a total of **4,100 input features**.

The imaging features are extracted using modality-specific DenseNet121 models. For abdominal ultrasound (ABD) images, a graph neural network (GNN) further aggregates multiple image-level representations into a single participant-level feature vector. For bone mineral density (BMD) images, DenseNet121 representations are obtained separately for the left hip, right hip, and spine.

The final feature composition is summarized below:

| Feature group | Number of features |
|---|---:|
| Abdominal ultrasound (ABD-GNN) | 1,024 |
| BMD – Left hip (DenseNet121) | 1,024 |
| BMD – Right hip (DenseNet121) | 1,024 |
| BMD – Spine (DenseNet121) | 1,024 |
| Demographic and clinical characteristics (age, sex, and family history) | 3 |
| Polygenic risk score (PRS) | 1 |
| **Total** | **4,100** |

These features are concatenated into a participant-level feature vector and subsequently used for T2D risk prediction using XGBoost or TabPFN.

To ensure consistency between model development and inference, the feature definitions, preprocessing procedures, and feature ordering must be preserved. The feature ordering associated with the reconstructed study-trained XGBoost model is provided in `model_weights/Study-trained_models/XGBoost/feature_order_4100.json`.

The corresponding feature extraction and integration procedures are demonstrated in Steps 2–4.


## Trained Model Artifacts

The repository provides two categories of model artifacts under `model_weights/`: **Demo-trained Models** and **Study-trained Models**. These artifacts serve different purposes and should not be used interchangeably.

### Demo-trained Models

The `model_weights/Demo-trained_models/` directory contains models generated through the 100-participant demonstration workflow.

| Model | Description |
|---|---|
| DenseNet121 | Four modality-specific models trained on demonstration images (ABD, BMD left hip, BMD right hip, and BMD spine). |
| Graph Neural Network (GNN) | A model trained to aggregate abdominal ultrasound image representations at the participant level. |
| XGBoost | A classification model trained using integrated multimodal features. |
| TabPFN | Configuration files documenting the demonstration-based prediction workflow. |
| Cox Proportional Hazards | A fitted survival model generated from the demonstration data. |

These artifacts are provided to illustrate the model-development procedures and enable users to examine the outputs of the demonstration workflows.

### Study-trained Models

The `model_weights/Study-trained_models/` directory contains selected model artifacts derived from the original research.

| Model | Available artifacts | Description |
|---|---|---|
| DenseNet121 | Four study-trained model checkpoints (`.pth`) | Models trained on the original research images for modality-specific feature extraction. |
| ABD-GNN/GCN | One study-trained model checkpoint (`.pth`) | A model trained to aggregate abdominal ultrasound image features. |
| XGBoost (M12) | `M12_XGBoost.json` | A reconstructed version of the study-trained XGBoost model using 4,100 input features. |
| Feature configuration | `feature_order_4100.json` | The feature names and ordering required for applying the reconstructed XGBoost model. |
| Cox Proportional Hazards | `Cox_SCORESUM01_Scaler.json` | PRS scaling parameters used in the study-trained Cox model (provided separately from the serialized model). |

The DenseNet121 and ABD-GNN/GCN checkpoints were obtained from the original study-trained models. In contrast, the M12 XGBoost artifact is a reconstructed model rather than the original serialized checkpoint.

When applying these models to new data, users must preserve the corresponding input definitions, preprocessing procedures, feature ordering, and model configurations.

### Model Availability and Limitations

**TabPFN:** A study-specific TabPFN checkpoint cannot be provided because standard TabPFN relies on pretrained foundation-model weights and in-context learning rather than generating a separately trained neural-network checkpoint for the study dataset. Reproducing the original study predictions also requires the corresponding support data and model configurations, which are not fully available for public distribution.

**Cox proportional hazards model:** The study-trained Cox model was refitted using the original research data after applying a 0–1 transformation to the PRS variable `SCORESUM`. The corresponding scaling parameters are provided in `model_weights/Study-trained_models/Cox/Cox_SCORESUM01_Scaler.json` to document the preprocessing procedure used in the original study.

However, the serialized Cox model (`Cox_SCORESUM01_Model.joblib`) contains individual-level training information and is therefore not included in the public repository. The provided scaling parameters do not constitute a standalone prediction model.

The study-trained model artifacts are intended to support further model application and evaluation where the necessary input data and configurations are available. They are distinct from the models trained using the 100-participant demonstration dataset.
separately.

The study-trained model artifacts are intended to support further model application and evaluation where the necessary input data and configurations are available. They are distinct from the models trained using the 100-participant demonstration dataset.




## Effective Independent Tests

To account for multiple testing across correlated genetic variants and phenotypes, the original study estimated the effective numbers of independent tests rather than treating all tests as statistically independent.

### Original Study

The effective number of independent genetic tests was estimated using KGGSEE/GEC, accounting for linkage disequilibrium (LD) among genetic variants.

For correlated phenotypes, the effective number of independent tests was estimated using an eigenvalue-based approach.

The original study obtained the following results:

| Analysis component | Number of variables | Effective independent tests |
|---|---:|---:|
| Genetic variants | Genome-wide SNPs | 768,377.22 |
| Imaging-derived phenotypes | 37 | 23 |
| Imaging and glycemic phenotypes | 40 | 25 |

The 40 phenotypes comprised 37 imaging-derived phenotypes and three additional traits: T2D, fasting glucose, and HbA1c.

Based on the effective numbers of genetic and phenotypic tests, the study-wide significance threshold was calculated as:

\[
\alpha = \frac{0.05}{768,377.22 \times 25}
\approx 2.6 \times 10^{-9}
\]

This threshold was used to account for multiple testing across genetic variants and phenotypes in the original study.

### Demonstration Analysis (Step 9)

The notebook `9.Step9_Independent_Test_Counts.ipynb` demonstrates the estimation of effective independent tests using example data.

The demonstration includes two components:

1. **Genetic variants:** A subset of chromosome 22 SNPs from the demonstration PLINK dataset is used to calculate an LD correlation matrix, perform eigenvalue decomposition, and estimate the effective number of genetic tests.

2. **Correlated phenotypes:** Synthetic imaging-derived and glycemic phenotypes are generated to demonstrate correlation matrix construction and the Li–Ji (2005) eigenvalue-based method for estimating effective independent phenotype tests.

The demonstration produces effective test estimates and corresponding multiple-testing thresholds using the example datasets.

Importantly, the demonstration uses only a limited SNP subset and synthetic phenotypes. It does not reproduce the original genome-wide KGGSEE/GEC analysis or the original study's phenotype correlation structure.

The original study's significance threshold of approximately \(2.6 \times 10^{-9}\) is therefore provided as a reference and should not be confused with the threshold calculated from the demonstration data.

Example outputs are available in `Outputs/Step9_Independent_Test_Counts/`.



## Data Availability and Reproducibility

### Original Research Data

The original study was conducted using data from the Taiwan Biobank (TWB). Due to data access and privacy restrictions, the original participant-level genetic, medical imaging, and clinical data are not publicly distributed through this repository.

Access to the original research data is subject to the relevant data access procedures, institutional approvals, and data-use agreements. Consequently, reproducing the exact numerical findings of the original study requires access to the corresponding research datasets.

### Demonstration Data and External Resources

To facilitate the examination and execution of the analytical workflows, this repository provides a demonstration dataset comprising 100 participants, organized into predefined training, validation, and testing subsets.

The demonstration includes example medical images, demographic and clinical characteristics, simulated genetic data, and T2D outcome information. Some demonstration inputs are modified from research inputs, while others are simulated. These data are intended to illustrate the analytical procedures rather than reproduce the original study population or its statistical results.

Additional external resources are required for certain analyses:

- **Step 1 (PRS Construction):** External GWAS summary statistics and linkage disequilibrium (LD) reference data must be prepared under `External_data/`.
- **Step 8 (Mendelian Randomization):** GWAS summary statistics and an LD reference panel must be prepared under `local_data/Step8_MR/`.

These external datasets and reference resources are not distributed with the repository. Users are responsible for obtaining the required resources from their respective providers and complying with applicable data-use conditions.

The original study's Taiwan Biobank-derived LD reference data are not publicly distributed.

### Computational Reproducibility and Interpretation

The repository provides Jupyter notebooks, Conda environment specifications, demonstration data, selected study-trained model artifacts, and example outputs to facilitate examination and reproduction of the computational workflows.

The environment configuration files are available in `environments/`, and additional software requirements are documented in `docs/software_requirements.md`.

Although the notebooks contain executable analytical procedures and example outputs, successful execution may depend on external reference resources, software dependencies, hardware compatibility, and computational configurations. The complete repository has not been independently validated in every supported computing environment.

In addition, differences in demonstration inputs, random initialization, software versions, and computational environments may lead to results that differ from the provided example outputs.

**The primary purpose of this repository is to demonstrate the computational methodology and model-development workflows.** Results generated using the demonstration data should not be interpreted as independent validation or exact reproduction of the original study findings.

Reproducing the original study's numerical results may require access to restricted research data and the corresponding historical analysis configurations.

## Citation

If you use the code, computational workflows, or model artifacts
provided in this repository, please cite the associated research
publication.

Citation details and the repository DOI will be updated upon
publication and release.
