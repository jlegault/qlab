# Blast Project Analysis Documentation

Included here are the most up-to-date progresses on blast MRI analyses

## FSL Statistical Learning fMRI analyses

### Cope Organization
#### Task
Runs 1 & 2: Tone is Random; Speech is Structured
Runs 3 & 4: Tone is Structured; Speech is Random

⋅⋅*For specific information about copes used, for each round of analysis, and information specific to blast SL fMRI processing, please see the blast_SL_fmri_documentation.md document.

#### Some important notes
Copes 5-7 were all calculated using the cope_normalization_sylvian_asl.sh script 

Using rename.sh script, Copes 1-3 were moved up one directory and Copes 5-7 were renamed as Copes 1-3, respectively.

### Progress report
#### First-Level Analysis: Complete, using FSL FEAT
#### Higher-Level Analysis: Complete, using FSL OLS
#### Group-Level Analysis: Complete, using FSL Randomise

### Participants used in FSL analyses
Adult participants were used in these analyses, here is a compiled table with which participants had what kind of data.  

| VSL           | ASL           | VSL and ASL   |
| ------------- | ------------- | ------------- |
| blast\_a\_001 | blast\_a\_001 | blast\_a\_001 |
| blast\_a\_002 | blast\_a\_002 | blast\_a\_002 |
| blast\_a\_004 | blast\_a\_004 | blast\_a\_004 |
| blast\_a\_005 | blast\_a\_005 | blast\_a\_005 |
| blast\_a\_006 | blast\_a\_006 | blast\_a\_006 |
| blast\_a\_007 | blast\_a\_007 | blast\_a\_007 |
| blast\_a\_008 | blast\_a\_010 | blast\_a\_010 |
| blast\_a\_010 | blast\_a\_011 | blast\_a\_011 |
| blast\_a\_011 | blast\_a\_012 | blast\_a\_012 |
| blast\_a\_012 | blast\_a\_013 | blast\_a\_013 |
| blast\_a\_013 | blast\_a\_014 | blast\_a\_014 |
| blast\_a\_014 | blast\_a\_017 | blast\_a\_017 |
| blast\_a\_015 | blast\_a\_018 | blast\_a\_018 |
| blast\_a\_017 | blast\_a\_020 | blast\_a\_020 |
| blast\_a\_018 | blast\_a\_021 | blast\_a\_024 |
| blast\_a\_020 | blast\_a\_023 | blast\_a\_038 |
| blast\_a\_022 | blast\_a\_024 | blast\_a\_039 |
| blast\_a\_024 | blast\_a\_027 | blast\_a\_044 |
| blast\_a\_038 | blast\_a\_029 |               |
| blast\_a\_039 | blast\_a\_035 |               |
| blast\_a\_044 | blast\_a\_038 |               |
|               | blast\_a\_039 |               |


## SPM Localizer fMRI analyses
### Main goals of analyses
Make subject-specific ROI masks of language-processing related regions to be used as structural masks in sMRI analyses

⋅⋅*For more information about this project, please see the blast_localizer_documentation.md document

### Progress report

#### Research questions, analysis plans, and hypotheses formulated (updated 4.23.2020)

#### Software installation
Progress: complete (updated 4.16.2020)

##### Software Used
2020 updated SPM_ss toolbox 
SPM 12: Installed updates and compiled via Catalina OS compilation.  See here: https://en.wikibooks.org/wiki/SPM/Installation_on_64bit_Mac_OS_(Intel)

#### Preprocessing in SPM12

#### Analyses in SPM12

#### Masks using SPM_ss Toolbox


