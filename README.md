# desa_d_hydrogel-widefield-ORI
### description of code and data for "Optical redox imaging to screen synthetic hydrogels for stem cell-derived cardiomyocyte differentiation and maturation" by DE Desa, MJ Amitrano, WL Murphy, MC Skala.

* To reproduce scatter plots/heatmaps, the included Excel files can be used ('data' folder).
* To reproduce histograms, seaborn = 0.12.0 (histoplot) is required.
* Raw images can be provided upon request:
  * To reproduce 2-photon FLIM data, the cell-analysis-tools repository (https://github.com/skalalab/cell-analysis-tools) can be used. Dependencies and instructions can be found in the linked repository. Raw fluorescence decays and/or exponential fits can be provided as needed.
  * To generate widefield ORR, the ImageJ script can be run on each individual folder, which includes a matched NAD(P)H and FAD intensity tiff, available upon request.
