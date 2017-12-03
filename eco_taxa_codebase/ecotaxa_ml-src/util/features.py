# -*- coding: utf-8 -*-

"""
Helper to load SparseConvNet features and perform a PCA on them.

A features file has the form:
    
    /path/to/<objid>.jpg,<numeric label>,<Features,*>
    
(This also allows the reading of feature files generated by newer versions
of SparseConvNet, that just contain the objid.)

See also zooscan.py, that loads ZooProcess features.
"""

import os
import numpy as np
from functools import partial
from itertools import count
import joblib
from sklearn.decomposition import PCA
import time

def count_newlines(f):
    BUFFER_SIZE = 16384
    return sum(chunk.count('\n') for chunk in iter(partial(f.read, BUFFER_SIZE), ''))

## DEPRECATED
#def load_features(fname, use_cache=True):
#    cache_fn = fname + ".npy"
#    
#    if use_cache and os.path.isfile(cache_fn) and os.path.getmtime(cache_fn) > os.path.getmtime(fname):
#        print("Using cached version: {}.".format(cache_fn))
#        return np.load(cache_fn)
#    
#    with open(fname) as f:
#        first_line = next(f).split()
#        n_cols = len(first_line)
#        
#    dtype = np.dtype([("i", np.int), ("y", np.int), ("X", np.float, n_cols - 2)])
#    
#    data = np.genfromtxt(fname, dtype = dtype)
#    
#    if use_cache:
#        np.save(cache_fn, data)
#            
#    return data

def load_features2(fname, use_cache=True):
    """
    Load SparseConvNet features.
    
    Because the loading of the data in the textfile is slow, the results can be
    cached.
    
    Parameters
        fname: Filename of the SparseConvNet features file.
        use_cache: Cache the result? (Default: True)
            The cached file is stored next to the features file and is
            only used if its newer than the features file.
    
    Returns
        A structured array of shape (N,) with fields "objid", "y", "X".
        "X" is a multidimensional field.
    """
    cache_fn = fname + ".npy"
    delimiter=","
    
    # Try to load a cached version
    if use_cache and os.path.isfile(cache_fn) and os.path.getmtime(cache_fn) > os.path.getmtime(fname):
        print("Using cached version: {}.".format(cache_fn))
        return np.load(cache_fn)
    
    # Otherwise read the features file
    with open(fname) as f:
        first_line = f.readline().rstrip("\n").split(delimiter)
        n_cols = len(first_line)
        n_rows = count_newlines(f) + 1
        
        if n_cols <= 2:
            raise Exception("Line does not contain enough columns:", first_line)
        
        dtype = np.dtype([("objid", "<U32"), ("y", np.int), ("X", np.float, n_cols - 2)])
        
        data = np.zeros(n_rows, dtype)
        
        f.seek(0)
        
        line_count = count()
        while True:
            line = f.readline()
            if line == "":
                break
            
            objid, y, *X = line.rstrip("\n").split(delimiter)
            idx = next(line_count)
            
            try:
                data["objid"][idx] = os.path.splitext(os.path.basename(objid))[0]
                data["y"][idx] = int(y)
                data["X"][idx] = np.array(X, np.float)
            except:
                print(line)
                print(objid, y, X)
                raise
            
    if use_cache:
        np.save(cache_fn, data)
            
    return data

def train_feature_pca(features, data_filename=None, verbose = True, n_components=None):
    """
    Perform PCA on a feature array and store the trained PCA model next to the
    structured feature array.
    
    Parameters:
        features: Structured array of features (as returned by load_features2).
        data_filename: That was used to load the features
            (parameter fname of load_features2).
        verbose: Print what is done.
    """
    pca = None
    
    # Construct filename for the pca model
    if data_filename is not None:
        if n_components is None:
            pca_model_fname = data_filename + ".pca.jbl"
        else:
            pca_model_fname = data_filename + ".pca_{}.jbl".format(n_components)
    else:
        pca_model_fname = None
        
    # Try to load a stored model (if its newer than the source file)
    if pca_model_fname and os.path.isfile(pca_model_fname) \
        and os.path.isfile(data_filename) \
        and os.path.getmtime(pca_model_fname) > os.path.getmtime(data_filename):
        if verbose:
            print("Loading PCA... ({})".format(pca_model_fname))
        
        try:
            with open(pca_model_fname, "rb") as f:
                pca = joblib.load(f)
        except Exception as e:
            print(" Error:", e)
            
    # Otherwise perform PCA and store the model
    if pca is None:
        if verbose:
            print("Fitting PCA...")
        pca = PCA(n_components=n_components, svd_solver='full')
        start = time.perf_counter()
        pca.fit(features["X"])
        time_taken = time.perf_counter() - start
        
        if verbose:
            print("Done ({:f}s).".format(time_taken))
    
        if pca_model_fname:
            if verbose:
                print("Saving PCA model to {}.".format(pca_model_fname))
            with open(pca_model_fname, "wb") as f:
                joblib.dump(pca, f)
    
    return pca

if __name__ == "__main__":
#    print("load_features...")
#    start = time.perf_counter()
#    result = load_features("/data1/mschroeder/Ecotaxa/Results/SCN_uvp5ccelter_group2_2_2017-08-18-15-56/_val.features", use_cache=False)
#    time_taken = time.perf_counter() - start
#    print("Done ({:f}s).".format(time_taken))
    
    print("load_features2...")
    start = time.perf_counter()
    result2 = load_features2("/data1/mschroeder/Ecotaxa/Results/SCN_uvp5ccelter_group2_2_2017-08-18-15-56/_val.features", use_cache=False)
    time_taken = time.perf_counter() - start
    print("Done ({:f}s).".format(time_taken))
    
#    assert np.allclose(result, result2)