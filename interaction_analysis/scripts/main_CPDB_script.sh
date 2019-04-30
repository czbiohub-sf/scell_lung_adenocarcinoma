# Activate environment 
source /myVolume/scell_lung_adenocarcinoma/interaction_analysis/cpdb-venv/bin/activate
# Run main command 
cellphonedb method statistical_analysis /myVolume/scell_lung_adenocarcinoma/interaction_analysis/data/in/grouped_pr_CPDB_meta_collapsed.txt /myVolume/scell_lung_adenocarcinoma/interaction_analysis/data/in/grouped_pr_CPDB_counts_collapsed.txt --threads=15 --project-name=grouped_PR ; cellphonedb method statistical_analysis /myVolume/scell_lung_adenocarcinoma/interaction_analysis/data/in/grouped_pd_CPDB_meta_collapsed.txt /myVolume/scell_lung_adenocarcinoma/interaction_analysis/data/in/grouped_pd_CPDB_counts_collapsed.txt --threads=15 --project-name=grouped_PD ; cellphonedb method statistical_analysis /myVolume/scell_lung_adenocarcinoma/interaction_analysis/data/in/naive_CPDB_meta_collapsed.txt /myVolume/scell_lung_adenocarcinoma/interaction_analysis/data/in/naive_CPDB_counts_collapsed.txt --threads=15 --project-name=NAIVE

