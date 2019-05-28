RV analysis example including a Gaussian process activity model
===============================================================

This repository contains an `ipython notebook <https://github.com/r-cloutier/RV_GP_example/blob/master/GP_RVanalysis_example.ipynb>`_ that demonstrates the steps that I take in a typical analysis of an RV time series of a planetary system that contains at least one planet and stellar activity. The example contained herein is based on the analysis of the `K2-18 multi-planetary system <https://arxiv.org/abs/1707.04292>`_ using K2 photometry and HARPS RV measurements. 

Basic Usage
-----------

All of the required data and code-specific python functions are included in this repository. As such, one just needs to clone this repository via::

	git clone https://github.com/r-cloutier/RV_GP_example.git

and open the ipython notebook describing the analysis steps via::

	jupyter notebook GP_RVanalysis_example.ipynb

Alternatively, if the user does not have `jupyter <https://jupyter.org/>`_ installed, use::

	ipython notebook GP_RVanalysis_example.ipynb

Requirements
------------

The notebook was written and tested in python version 2.7 and requires the following libraries

- numpy 1.16.3
- scipy 1.1.0
- mpmath 0.19
- matplotlib 2.1.1
- `george 0.2.1 <https://george.readthedocs.io/en/latest/>`_
- `emcee 2.2.1 <http://dfm.io/emcee/current/>`_
- `corner 2.0.1 <https://github.com/dfm/corner.py>`_
- `PyAstronomy 0.11.0 <https://www.hs.uni-hamburg.de/DE/Ins/Per/Czesla/PyA/PyA/index.html>`_
