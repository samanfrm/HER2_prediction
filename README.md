For details and citations about this work, please check:

Farahmand, S., Fernandez, A.I., Ahmed, F.S. et al. Deep learning trained on hematoxylin and eosin tumor region of Interest predicts HER2 status and trastuzumab treatment response in HER2+ breast cancer. Mod Pathol (2021). https://doi.org/10.1038/s41379-021-00911-w


https://www.nature.com/articles/s41379-021-00911-w

The deep learning architecture is based on the inception v3 architecture from Google and the procedure is taken from [Coudray et. al.](https://github.com/ncoudray/DeepPATH) study. 



# HER2_prediction
Deep learning trained on hematoxylin and eosin tumor region of Interest predicts HER2 status and trastuzumab treatment response in HER2+ breast cancer

## Overview
The current standard of care for many patients with HER2-positive breast cancer is neoadjuvant chemotherapy in combination with anti-HER2 agents, based on HER2 amplification as detected by in situ hybridization (ISH) or protein immunohistochemistry (IHC). However, hematoxylin & eosin (H&E) tumor stains are more commonly available, and accurate prediction of HER2 status and anti-HER2 treatment response from H&E would reduce costs and increase the speed of treatment selection. Computational algorithms for H&E have been effective in predicting a variety of cancer features and clinical outcomes, including moderate success in predicting HER2 status. In this work, we present a novel convolutional neural network (CNN) approach able to predict HER2 status with increased accuracy over prior methods. We trained a CNN classifier on 188 H&E whole slide images (WSIs) manually annotated for tumor Regions of interest (ROIs) by our pathology team. Our classifier achieved an area under the curve (AUC) of 0.90 in cross-validation of slide-level HER2 status and 0.81 on an independent TCGA test set. Within slides, we observed strong agreement between pathologist annotated ROIs and blinded computational predictions of tumor regions / HER2 status. Moreover, we trained our classifier on pre-treatment samples from 187 HER2+ patients that subsequently received trastuzumab therapy. Our classifier achieved an AUC of 0.80 in a five-fold cross validation. Our work provides an H&E-based algorithm that can predict HER2 status and trastuzumab response in breast cancer at an accuracy that may benefit clinical evaluations.


## Datasets

The datasets will be uploaded and available on [The Cancer Imaging Archive](https://www.cancerimagingarchive.net/) soon!
* **Yale HER2 cohort**: 188 HER2 positive and negative invasive breast carcinomas were identified by retrospective search of the Yale Pathology electronic database with HER2 positive cases defined as those with 3+ score by immunohistochemistry (IHC) as defined by American Society of Clinical Oncology/College of American Pathologists (ASCO/CAP) clinical practice guidelines.

* **Yale trastuzumab response cohort**: The response cohort cases were identified also by retrospective search of the Yale Pathology electronic database. Cases included those patients with a pre-treatment breast core biopsy with HER2 positive invasive breast carcinoma who then received neoadjuvant targeted therapy with trastuzumab +/- pertuzumab prior to definitive surgery.

* **TCGA HER2 cohort**: A total of 668 TCGA-BRCA HER2+/- samples with available HER2 status were downloaded from the [GDC portal](https://portal.gdc.cancer.gov/).


## Histopathology stain color normalization

Histopathology stain color normalization procedure is taken from [Zanjani et. al.] (https://github.com/FarhadZanjani/Histopathology-Stain-Color-Normalization).

## System requirement

This pipeline is currently developed on the University of Massachusetts Green High Performance Computing Cluster" (GHPCC) and is running on GPU nodes with Tesla V100 GPUs.

Major dependencies are:
- python 3.6.5 
- tensorflow-gpu 1.9.0
- numpy 1.14.3
- matplotlib 2.1.2
- sklearn
- scipy 1.1.0
- openslide-python 1.1.1
- Pillow 5.1.0

