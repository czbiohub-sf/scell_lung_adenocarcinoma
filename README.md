# scell_lung_adenocarcinoma
This is the repository that contains the analysis of the lung adenocarcinoma single cell dataset


## Getting started
Clone the repo
Download the Data_input folder from the link below into the repo
https://drive.google.com/drive/folders/1nONsp9VuhmPzuDvMet0i8x26eV9r5lkT?usp=sharing 

## Scripts

### Importing and Creating Seurat Object
01_Import_data_and_metadata.Rmd: Import raw data and metadata

02_Create_Seurat_object.Rmd: Create initial Seurat object

03_Subset_and_general_annotations.Rmd: Inital quality control, general cell annotations, and splitting of data into immune and non-immune subsets.

### Immune Compartment Analysis


IM01_Subset_cluster_annotate_immune_cells.Rmd: Imports .RData object from script 03 above that includes only immune cells. In the script cells are clustered and annotated. Object that is produced and saved at the end of the script is called "IM01_Immune_Seurat_object.RData"


IM02_immune_cell_changes_with_response_to_treatment.Rmd: Imports .RData object from script IM01. The  script investigates changes in the fraction of immune populations in regard to treatment status across all patients.  

I06_TCR_analysis.nb.html


IM04a_Subset_cluster_annotate_MFs-monocytes_LIVER.Rmd
IM04a_Subset_cluster_annotate_MFs-monocytes_LUNG.Rmd
IM04b_Subset_cluster_annotate_T-cells_LIVER.Rmd
IM04b_Subset_cluster_annotate_T-cells_LUNG.Rmd
IM05_interaction_analysis.Rmd
IM06_expression_of_selected_genes_across_immune_cells.Rmd
IXX_Immune_cells_across_pats_with_multiple_biopsies-copy.Rmd
IXX_Immune_cells_across_pats_with_multiple_biopsies.Rmd

### Non-Immune Compartment Analysis
NI01_General_annotation_of_nonimmune_cells.Rmd

NI02_epi_subset_and_cluster.Rmd

NI03_inferCNV.Rmd
NI04_Cancer_cells_DEgenes.Rmd

NI05_Annotation_of_Nontumor_epi.Rmd	updates
NI06_mutation_analysis.Rmd
NI07_TH226_cancercell_analysis.Rmd
NI08_dor_clinical_regression.Rmd

NI09_PER_clincal_workbook.Rmd

NI10_Gene_expression_plotting.Rmd	

NI11_AT2_sig_compare.Rmd	updates	

NI12_endothelial_subset.Rmd	

NI13_Fibro_subset.Rmd	

NI14_TCGA_clinical_outcomes.Rmd	

seurat_to_IPA.R
