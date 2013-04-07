Hands on tutorial for ``gptwosample``
=========================================

In this tutorial we will process a full run example of
``gptwosample``. See the full usage information in :ref:`usage`. See
format for input data ``.csv`` files in :ref:`dataformat`. Make sure
you ``cd`` into the extracted gptwosample folder before running this tutorial. 
Try printing the full help of the script using::

 python gptwosample --help

If an error occurs, you probably ``cd`` one level too deep and you can
``cd ..`` up one level.

We will build up the whole running signature step by step in the following.
We want to run the script verbosly and with that the script so far looks like::

 python gptwosample -v

To enable plotting we provide the switch ``-p`` to the script::

 python gptwosample -v -p

We want to correct for timeshifts (more on :ref:`timeshift`), thus we
enable the timeshift switch ``-t``::

 python gptwosample -v -p -t

Next we could additionally learn x confounding factors (see
:ref:`confounders` for details on confounding factors) and account
for them while two-sampling::

 python gptwosample -v -p -t -c x

but we do not want to account for confounders in this tutorial,
leaving the data files to run on.

The output of the script shall be in the subfolder ``./tutorial/``, so
we add the output flag ``-o ./tutorial/``:

 python gptwosample -v -p -t -o ./tutorial/

The script shall be run on the two toy condition files ``ToyCondition{1,2}.csv``
given in ``examples/ToyCondition{1,2}.csv``. These files
are non optional as this package is only for comparing two timeseries
experiments to each other::

 python gptwosample -v -p -t -o ./tutorial/ examples/ToyCondition1.csv examples/ToyCondition2.csv

Note that the optional parameters could be collected together to give
rise to a more compact call signature::

 python gptwosample -vpto tutorial examples/ToyCondition1.csv
 examples/ToyCondition2.csv

After hitting return the script runs gptwosample on every gene given
in the ToyCondition files and plots each gene into
``tutorial/plots/``. One example plot will look like:

.. image:: ../images/timeshiftexample.pdf
        :height: 12cm

The results are saved in the ``results.csv``, which contains all
predicted Bayes Factors and learnt covariance function parameters for
all genes (:ref:`results`).