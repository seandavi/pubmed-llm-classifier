# gpt-examples
gpt-examples

## pubmed classifier

The pubmed abstract associated with this pubmed ID is:

> Cancer nanotheranostics combining therapeutic and imaging functions within a
> single nanoplatform are extremely important for nanomedicine. In this study,
> carbon dots (C-dots) with intrinsic theranostic properties are prepared by
> using polythiophene benzoic acid as carbon source. The obtained C-dots absorb
> light in the range of 400-700 nm and emit bright fluorescence in the red
> region (peaking from 640 to 680 nm at different excitations). More
> importantly, the obtained C-dots exhibit dual photodynamic and photothermal
> effects under 635 nm laser irradiation with a singlet oxygen ((1)O2)
> generating efficiency of 27% and high photothermal conversion efficiency of
> 36.2%. These unique properties enable C-dots to act as a red-light-triggered
> theranostic agent for imaging-guided photodynamic-photothermal simultaneous
> therapy in vitro and in vivo within the therapeutic window (600-1000 nm).


```sh
python pubmed_cancer_classifier.py 26696330
```

Output:

```json
{
  "cancer-related": true,
  "confidence": 4,
  "concepts": [
    {
      "concept": "Theranostics",
      "concept_description": "A combination of therapeutic and diagnostic capabilities within a single agent or platform.",
      "cancer-related": true
    },
    {
      "concept": "Carbon dots (C-dots)",
      "concept_description": "Small carbon nanoparticles with unique optical properties.",
      "cancer-related": true
    },
    {
      "concept": "Photodynamic therapy",
      "concept_description": "A treatment using a photosensitizing agent and a specific wavelength of light to produce singlet oxygen that can kill cancer cells.",
      "cancer-related": true
    },
    {
      "concept": "Photothermal therapy",
      "concept_description": "A treatment that uses light-absorbing agents to generate heat and destroy cancer cells.",
      "cancer-related": true
    }
  ],
  "pmid": 26696330
}
```
