This is the repository that contains the analysis of the lung adenocarcinoma single cell dataset

## Getting started

Clone the repo
Download the Data_input folder from the link below into the repo
https://drive.google.com/drive/folders/1nONsp9VuhmPzuDvMet0i8x26eV9r5lkT?usp=sharing 

## Scripts

### Importing and Creating Seurat Object

**_01_Import_data_and_metadata.Rmd_**: Import raw data and metadata. Output of this scipt is saved as _"S01_Data_and_metadata.RData"_.

**_02_Create_Seurat_object.Rmd_**: Imports .RData object from script 01. Creates initial Seurat object and performs initial quality control. Final output object is saved as _"S02_Main_Seurat_object_filtered.RData"_. 

**_03_Subset_and_general_annotations.Rmd_**: Imports final .RData object from script 02. In this script we subset samples to those with greater than 10 cells and perform clustering. The cells are annotated and subset to immune or non-immune cells datasets. Produced obejects are _"S03_Main_Seurat_object_filtered_and_subset.RData"_, _"S03_Immuune_Seurat_object.RData"_, and _"S03_Nonimmune_Seurat_object.RData"_. 

### Immune Compartment Analysis

**_IM01_Subset_cluster_annotate_immune_cells.Rmd_**: Imports .RData object from script 03 above that includes only immune cells. In the script cells are clustered and annotated. Object that is produced and saved at the end of the script is called _"IM01_Immune_Seurat_object.RData"_.

![Image of Immune cell tSNE with marker gene colors](Immune_cells_TSNE_with_average_expression_of_cell_markers.pdf)


**_IM02_immune_cell_changes_with_response_to_treatment.Rmd_**: Imports .RData object from script IM01. Within the  script we investigate changes in the fraction of immune populations in regard to treatment status across all patients.

**_IM03_Subset_cluster_annotate_MFs-monocytes_LUNG.Rmd_**: Subsetting and clustering of all macrophages/monocytes from Lung biopsies followed by treatment stage specific analysis of resulting populations. Output object is called _IM03_MFs_Seurat_object.RData_.

**_IM04_Subset_cluster_annotate_T-cells_LUNG.Rmd_**: Subsetting and clustering of all macrophages/monocytes from Lung biopsies followed by treatment stage specific analysis of resulting populations. Output object is called _IM04_Tcells_Seurat_object.RData_.

**_IM05_Immune_cells_across_pats_with_multiple_biopsies.Rmd_**: Analysis of fractional population changes in patients with multiple biopsies. 


### Non-Immune Compartment Analysis

**_NI01_General_annotation_of_nonimmune_cells.Rmd_**: Imports .RData object from script 03 that included only non-immune cells. In the script cells are clustered and annotated. Objects that is produced and saved at the end of the script is called _"NI01_Nonimmune_Seurat_object_annotated.RData"_.

**_NI02_epi_subset_and_cluster.Rmd_**: Imports .RData object from NI01. In this script we subset the cells to only those that are epithelial and re cluster cells. The resulting subset object is saved at the end of the script as _"NI02_Epi_Seurat_object_clustered.RData"_.

**_NI03_inferCNV.Rmd_**: Imports .RData object from NI02. In this script we use InferCNV to identify cancer and non-cancer epithelial cells. The cells are annotated and the resulting object is saved at the end of the script as "NI03_epithelial_annotated_tumor.RData".

**_NI04_Cancer_cells_DEgenes.Rmd_**: Imports .RData object generated from NI03. In this script we subset the data to cancer cells only and then find the differenitailly expressed genes from three comparisions: 1. TN vs PER, 2. TN vs PD, and 3. PER vs PD. The cancer cell only object is saved as _"NI04_tumor_seurat_object.RData"_.

**_NI05_Annotation_of_Nontumor_epi.Rmd_**: Imports .RData object generated from NI03. In this script we subset the data to non-cancer cells only. The non-cancer epithelial cells are then clustered and annotated. The non-cancer epithelial cell object is saved as _"NI05_normalepi_seurat_object_annotated.RData"_.

**_NI06_mutation_analysis.Rmd_**: Imports .RData object generated from NI04. In this script we combine outputs from cerebra to a create mutational table.

**_NI07_TH226_cancercell_analysis.Rmd_**: Imports .RData object generated from NI04. In this script we subset the data to a single patient with mutliple biopsies and find the differenitailly expressed genes from three comparisions: 1. TN vs PER, 2. TN vs PD, and 3. PER vs PD. We also investigate the expression of five gene expression signatures found within the grouped ananlysis in NI04. 

**_NI08_Gene_expression_plotting.Rmd_**: Imports .RData object generated from NI04. In this script we investigate the expression of five gene expression signatures found within the grouped ananlysis in NI04. 

**_NI09_AT2_sig_compare.Rmd_**: Imports .RData objects from NI04 and NI05 as well as data and metadata files in /Data_input/GSE130148_data. In this script we compare cancers cells from each treatment timepoint (TN, PER, PD), as well as non-cancer AT2 cells to an outside dataset of healthy AT2 cells. 

**_NI10_TCGA_clinical_outcomes.Rmd_**: Imports three input files from /Data_input/TCGA. We compare the five gene expression signatures found within the grouped analysis of NI04 to patient surival outcomes within the TCGA. 

**_NI11_WES_analysis.ipynb_**: This notebook compares the mutations identified in whole-exome-seq to those identified with scRNA-seq, for the same patient samples.  

**_NI12_msk_analysis.ipynb_**: This notebook creates figures 2D & E. Takes as input msk_impact_2017/MSK-IMPACT_cosmic_tier1.txt, msk_impact_2017data_clinical_patient_edit.txt and mutation_input/coverage_all_cells_cerebra.csv from Data_input/. Investigates survival outcomes of a large cohort of LAUD patients with similar/different mutational profiles as the ones we identify in our patient samples. 

**_NI13_get_ercc_substitution_rate.py_**: python script for calculating per-base substitution rates in ERCC standards, for a large group of scRNA-seq bam files. 


## Cerebra

We used the Cerebra tool (https://github.com/czbiohub/cerebra) report mutations and read coverage of regions of interest within genes. Cerebra uses GATK output files (.vcfs) as input and is comprised of several modules which do the following: 1) generate a cell_x_gene mutation-counts matrix, 2) generate a cell_x_ROI summary table that reports amino acid level mutations for a user-defined list of genes, 3) report read coverage (variant vs total reads) to each ROI.

