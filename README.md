# Classification d’images de plancton par Deep Learning ou apprentissage hybride Deep Features/Random Forest

Le Laboratoire d'Océanographie de VilleFranche-Sur-Mer a besoin de classer de grande quantité d'image de plancton dans une centaine de classes différentes. Dans le cadre de notre Projet de Fin d'édude nous souhaitons classifier les différentes espèces en utilisant de nouvelles architecture de deep learning pour exploiter la taxonomie des espèces de plancton.

## Organisation des répertoires

* Architectures
    * Hierarchiques:
        * LayerClassifieur : Classifieur à niveaux
        * TreeClassifieur : Classifieur en arbre
    * Classiques
        * MVP: Classifier classique avec data augmentation
    * Autres:
        * Ecotaxa-codebase:
        * training darkflow:
        * wildcat:
        * YOLO: You Look Only Once Algorithm
* Cluster: Folder running the learning on the INRIA cluster
* Datasets: Folder with the differents dataset 
    * Kaggle: kaggle dataset
    * uvp5ccelter : dataset of the LOV
    * level0_new_hierarchique2_datagen: uvp5ccelter dataset removing some classes and dataugmented




## Installation

Le Laboratoire d'Océanographie de VilleFranche-Sur-Mer nous fourni un dataset sur lequel tester nos architectures.
Il est possible de récupérer le dataset : [plankton data](ftp://oceane.obs-vlfr.fr/pub/irisson/plankton_data/)
Un projet kaggle en relation avec la classification de plancton est disponible : [projet kaggle](https://www.kaggle.com/c/datasciencebowl/)

## Paquets nécéssaires

```
* OpenCV
* Tensorflow
* Keras
```

## Auteurs

* [**Thomas Mahiout**](https://github.com/thomasmahiout)
* [**Cédric Bailly**](https://github.com/CedricBailly)
* [**Thomas Jalabert**](https://github.com/atthom/)


## Acknowledgments

* Mr Precioso et Mr Debreuve nos tuteurs de PFE.
* Jean-Olivier Irisson du LOV qui nous a fourni son dataset.