
## Step 8 - MR Environment

Step 8 requires a separate R environment.

### 1. Create the environment

Run from the GitHub repository root:

    conda env create -f environments/mr.yml

### 2. Install TwoSampleMR

    conda run -n t2d-mr Rscript -e 'install.packages("TwoSampleMR", repos=c("https://mrcieu.r-universe.dev","https://cloud.r-project.org"), dependencies=c("Depends","Imports","LinkingTo"))'

### 3. Install MR-PRESSO

    conda run -n t2d-mr Rscript -e 'remotes::install_github("rondolab/MR-PRESSO", upgrade="never", dependencies=FALSE)'

### 4. Register the Jupyter R kernel

    conda run -n t2d-mr Rscript -e 'IRkernel::installspec(user=TRUE, name="t2d-mr", displayname="R (T2D MR)")'

### 5. Verify installation

    conda run -n t2d-mr Rscript -e 'stopifnot(requireNamespace("TwoSampleMR",quietly=TRUE), requireNamespace("MRPRESSO",quietly=TRUE)); cat("MR environment ready\n")'

Select R (T2D MR) when running 8.Step8_MR.ipynb.

### Verified development environment

- R: 4.3.3
- PLINK2: 2.0.0-a.7.13
- TwoSampleMR: 0.7.13
- MRPRESSO: 1.0
- data.table: 1.17.8
- ggplot2: 3.5.2
- IRkernel: 1.3.2

These are verified development versions, not fully locked dependencies.

If conda is not on PATH, use the full path to the local Conda executable.

