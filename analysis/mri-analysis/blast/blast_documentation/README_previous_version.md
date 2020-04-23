# Blast Project Analysis Documentation

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

Runs 3 & 4
|   Cope | Name                                  | TSL Structured  | SSL Random     |
|-------:|--------------------------------------:|----------------:|----------------|
| Cope 1 | Tone Struct > Rest                    |               1 |              0 |
| Cope 2 | Speech Rand > Rest                    |               0 |              1 |
| Cope 3 | Speech  > Tone                        |              -1 |              1 |
| Cope 4 | Mean                                  |               1 |              1 |
|std_func| StDev in time for filtered_func       |                                  |
| Cope 5 | Normalized Tone Struct > Rest         |Cope calculation: Cope 1/std_func |
|        |                                       |No changes to varcopes            |
| Cope 6 | Normalized Speech Rand > Rest         |Cope calculation: Cope 2/std_func |
|        |                                       |No changes to varcopes            |
| Cope 7 | Normalized Speech > Tone              |Cope calculation: Cope 6 -Cope 5  |
|        |                                       |No changes to varcopes            |

Copes 5-7 were all calculated using the cope_normalization_sylvian_asl.sh script 

Important:  Using rename.sh script, Copes 1-3 were moved up one directory and Copes 5-7 were renamed as Copes 1-3, respectively.

#### Higher-Level Analysis

|   Cope | Name                   | Run 1 | Run 2 | Run 3 | Run 4 |
|-------:|-----------------------:|------:|------:|------:|------:|
| Cope 1 | Run 3-4 vs Run 1-2     |    -1 |    -1 |      1|     1 |
| Cope 2 | Run 3-4 vs Run 1-2     |     1 |     1 |     -1|   - 1 |
| Cope 3 | Run 3-4 vs Run 1-2     |     1 |     1 |      1|     1 |

#### Group-Level Analysis

| Cope 1 |           |                                               |
|-------:|----------:|----------------------------------------------:|
|        |**Cope 1** | Tone Structured > Tone Random                 |
|        |  Cope 2   | Tone Random > Tone Structured                 |
|        |  Cope 3   | Tone > Rest                                   |
| Cope 2 |           |                                               |
|        |  Cope 1   | Speech Random > Speech Structured             |
|        |**Cope 2** | Speech Structured > Speech Random             |
|        |  Cope 3   | Speech > Rest                                 |
| Cope 3 |           |                                               |
|        |  Cope 1   | Random > Structured                           |
|        |  Cope 2   | Structured > Random                           |
|        |**Cope 3** | Speech > Tone                                 |
| Cope 4 |           |                                               |
|        |  Cope 1   | Run 3-4 task > Run 1-2 task                   |
|        |  Cope 2   | Run 1-2 task > Run 3-4 task                   |
|        |**Cope 3** | Task > Rest                                   |
| Cope 5 |**Cope 1** | Normalized Tone Structured > Tone Random      |
|        |  Cope 2   | Normalized Tone Random > Structured           |
|        |  Cope 3   | Normalized Mean Tone > Rest                   |
| Cope 6 |  Cope 1   | Normalized Speech Random > Speech Structured  |
|        |**Cope 2** | Normalized Speech Structured > Speech Random  |
|        |  Cope 3   | Normalized Mean Speech > Rest                 |
| Cope 7 |**Cope 1** | Normalized Random > Structured                |
|        |**Cope 2** | Normalized Structured > Random                |
|        |**Cope 3** | Normalized Speech > Rest                      |

## SPM Localizer fMRI analyses

### Preprocessing
### Analyses
### Masks
