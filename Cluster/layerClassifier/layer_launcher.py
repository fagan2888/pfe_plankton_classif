import os
from LayerClassifier import LayerClassifier

super_path = "E:\\Polytech_Projects\\pfe_plankton_classif\\LOOV\\super_classif"
super_path = "E:\\Polytech_Projects\\pfe_plankton_classif\\Dataset\\DATASET\\level0_new_hierarchique"
super_path = "/home/tjalaber/pfe_plankton_classif/Cluster/Classif2"

lc = LayerClassifier(super_path)
lc.create_achitecture(1000, 5)

# lc.load_achitecture()
