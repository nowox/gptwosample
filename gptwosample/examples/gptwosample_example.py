'''
Created on Mar 30, 2013

@author: Max
'''
import numpy
from pygp.covar.se import SqexpCFARD
from gptwosample.twosample.twosample import TwoSample
import pylab

if __name__ == '__main__':
    Tt = numpy.arange(0, 16, 2)[:, None]
    Tr = numpy.tile(Tt, 3).T
    Ts = numpy.array([Tr, Tr],dtype=float)

    n, r, t, d = nrtd = Ts.shape + (12,)

    covar = SqexpCFARD(1)
    K = covar.K(covar.get_de_reparametrized_theta([1, 13]), Tt)
    m = numpy.zeros(t)

    try:
        from scikits.learn.mixture import sample_gaussian
    except:
        raise "scikits needed for this example"
        # raise r

    y1 = sample_gaussian(m, K, cvtype='full', n_samples=d)
    y2 = sample_gaussian(m, K, cvtype='full', n_samples=d)

    Y1 = numpy.zeros((t, d + d / 2))
    Y2 = numpy.zeros((t, d + d / 2))

    Y1[:, :d] = y1
    Y2[:, :d] = y2

    sames = numpy.random.randint(0, d, size=d / 2)

    Y1[:, d:] = y2[:, sames]
    Y2[:, d:] = y1[:, sames]

    Y = numpy.zeros((n, r, t, d + d / 2))

    sigma = .5
    Y[0, :, :, :] = Y1 + sigma * numpy.random.randn(r, t, d + d / 2)
    Y[1, :, :, :] = Y2 + sigma * numpy.random.randn(r, t, d + d / 2)

    n, r, t, d = Y.shape

    for _ in range((n*r*t*d)/4):
        #Ts[numpy.random.randint(n),numpy.random.randint(r),numpy.random.randint(t)] = numpy.nan
        Y[numpy.random.randint(n),numpy.random.randint(r),numpy.random.randint(t),numpy.random.randint(d)] = numpy.nan

    

    c = TwoSample(Ts, Y)

    c.predict_likelihoods(Ts, Y)
    c.predict_means_variances(numpy.linspace(Ts.min(), Ts.max(), 100))

    pylab.ion()
    pylab.figure()
    for _ in c.plot():
        raw_input("enter to continue")

