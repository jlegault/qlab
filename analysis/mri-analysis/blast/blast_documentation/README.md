# blast Project Analysis Documentation

Included here are the most up-to-date progresses on blast MRI analyses

## FSL Statistical Learning fMRI analyses

### Cope Organization
#### Task
Runs 1 & 2: Tone is Random; Speech is Structured
Runs 3 & 4: Tone is Structured; Speech is Random
#### First Level Analysis

Runs 1 & 2
|   Cope | Name                                  | TSL Random  | SSL Structured     |
|-------:|--------------------------------------:|------------:|--------------------|
| Cope 1 | Tone Rand > Rest                      |           1 |                  0 |
| Cope 2 | Speech Struct > Rest                  |           0 |                  1 |
| Cope 3 | Speech  > Tone                        |          -1 |                  1 |
| Cope 4 | Mean                                  |           1 |                  1 |
|std_func| StDev in time for filtered_func       |                                  |
| Cope 5 | Normalized Tone Rand > Rest           |Cope calculation: Cope 1/std_func |                               
|        |                                       |No changes to varcopes            |
| Cope 6 | Normalized Speech Struct > Rest       |Cope calculation: Cope 2/std_func |
|        |                                       |No changes to varcopes            |
| Cope 7 | Normalized Speech > Tone              |Cope calculation: Cope 6 -Cope 5  |
|        |                                       |No changes to varcopes            |

 
## SPM Localizer fMRI analyses
### Preprocessing
### Analyses
### Masks
