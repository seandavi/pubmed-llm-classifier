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
      "concept": "Cancer nanotheranostics",
      "mesh_identifier": "D000068877",
      "cancer-related": true
    },
    {
      "concept": "Carbon dots (C-dots)",
      "mesh_identifier": "D000066448",
      "cancer-related": false
    },
    {
      "concept": "Photodynamic therapy",
      "mesh_identifier": "D017145",
      "cancer-related": true
    },
    {
      "concept": "Photothermal therapy",
      "mesh_identifier": "D000069447",
      "cancer-related": true
    },
    {
      "concept": "Bioimaging",
      "mesh_identifier": "D000067297",
      "cancer-related": false
    }
  ],
  "pmid": 26696330
}
```
