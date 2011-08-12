'''
Small Example application of GPTwoSample with confounder detection
==================================================================

Created on Jun 9, 2011

@author: Max Zwiessele, Oliver Stegle
'''
import os
import csv
import scipy

try:
    from gptwosample.data import toy_data_generator
except:
    import sys
    sys.path.append('../../')
    sys.path.append("../../../pygp")
finally:
    from gptwosample.data import toy_data_generator
from gptwosample.data.dataIO import get_data_from_csv
from gptwosample.data.data_base import get_training_data_structure,\
    get_model_structure, common_id, individual_id
from pygp.covar import linear, se, noise, combinators
from pygp.priors import lnpriors
import logging as LG
#import pylab as PL
import scipy as SP
#from gptwosample.plot.plot_basic import plot_results
from gptwosample.twosample.twosample_compare import GPTwoSample_individual_covariance
from pygp.gp import gplvm
from pygp import likelihood as lik
from pygp.optimize.optimize_base import opt_hyper
from pygp.covar.fixed import FixedCF
import pdb

def run_demo(cond1_file, cond2_file):
    #full debug info:
    LG.basicConfig(level=LG.INFO)

    #1. read csv file
    print 'reading files'
    cond1 = get_data_from_csv(cond1_file, delimiter=',')
    cond2 = get_data_from_csv(cond2_file, delimiter=",")

#range where to create time local predictions ? 
    #note: this need to be [T x 1] dimensional: (newaxis)
    Tpredict = SP.linspace(cond1["input"].min(), cond1["input"].max(), 100)[:, SP.newaxis]
    T1 = cond1.pop("input")
    T2 = cond2.pop("input")
    
    gene_names = sorted(cond1.keys()) 
    assert gene_names == sorted(cond2.keys())
    
    n_replicates = cond1[gene_names[0]].shape[0]
    n_replicates_1 = n_replicates_2 = n_replicates/2
    gene_length = len(T1)
    
    components = 4
    
    Y1 = SP.array(cond1.values()).reshape(T1.shape[0]*n_replicates,-1)
    Y2 = SP.array(cond2.values()).reshape(T2.shape[0]*n_replicates,-1)

#    X01 = gplvm.PCA(Y1, components)[0]
#    X02 = gplvm.PCA(Y2, components)[0]
#    
    lvm_covariance = linear.LinearCFISO(n_dimensions=4)
#    
#    X0=X01
#    hyperparams = {'covar': SP.log([1.2])}   
#    likelihood = lik.GaussLikISO()
#    hyperparams['lik'] = SP.log([0.1])
#    bounds = {}
#    bounds['lik'] = SP.array([[-5.,5.]]*Y1.shape[1])
#    hyperparams['x'] = X0.copy()

#    g = gplvm.GPLVM(covar_func=lvm_covariance,likelihood=likelihood,x=hyperparams['x'],y=Y1)
    
#    print "running standard gplvm"
#    [opt_hyperparams_1,opt_lml2] = opt_hyper(g,hyperparams,gradcheck=False)
#
#    X0=X02.copy()
#    hyperparams = {'covar': SP.log([1.2])}
#    hyperparams['x'] = X0
#    
#    likelihood = lik.GaussLikISO()
#    hyperparams['lik'] = SP.log([0.1])
#    g = gplvm.GPLVM(covar_func=lvm_covariance,likelihood=likelihood,x=X0,y=Y2)
#    
#    bounds = {}
#    bounds['lik'] = SP.array([[-5.,5.]]*Y2.shape[1])
#    
#    print "running standard gplvm"
#    [opt_hyperparams_2,opt_lml2] = opt_hyper(g,hyperparams,gradcheck=False)
#    
    Y_comm = SP.concatenate((Y1,Y2))#.reshape(T1.shape[0]*n_replicates*2,-1)
    X0 = gplvm.PCA(Y_comm, components)[0]
    #SP.concatenate((X01, X02)).copy()#
    
    hyperparams = {'covar': SP.log([1.2])}
    hyperparams['x'] = X0
    
    likelihood = lik.GaussLikISO()
    hyperparams['lik'] = SP.log([0.1])
    g = gplvm.GPLVM(covar_func=lvm_covariance,likelihood=likelihood,x=X0,y=Y_comm)
    
    bounds = {}
    bounds['lik'] = SP.array([[-5.,5.]]*Y2.shape[1])
    
    print "running standard gplvm"
    [opt_hyperparams_comm,opt_lml2] = opt_hyper(g,hyperparams,gradcheck=False)
    
    #X_conf_1 = opt_hyperparams_1['x'] * opt_hyperparams_1['covar']
    #X_conf_2 = opt_hyperparams_2['x'] * opt_hyperparams_2['covar']
    #SP.concatenate((X_conf_1, X_conf_2))
    X_conf_comm = opt_hyperparams_comm['x'] * opt_hyperparams_comm['covar']

#    X_conf_1 = SP.dot(X_conf_1,X_conf_1.T) \

#    X_conf_2 = SP.dot(X_conf_2,X_conf_2.T) \
    X_len = X_conf_comm.shape[0]
    X_conf_1 = X_conf_comm[:X_len/2]
    X_conf_2 = X_conf_comm[X_len/2:]

    X_conf_1 = SP.dot(X_conf_1, X_conf_1.T)
    X_conf_2 = SP.dot(X_conf_2, X_conf_2.T)
    
    X_conf_comm = SP.dot(X_conf_comm, X_conf_comm.T) \


    #hyperparamters
    dim = 1
    replicate_indices = []
    for rep in SP.arange(n_replicates):
        replicate_indices.extend(SP.repeat(rep,gene_length))
    replicate_indices = SP.array(replicate_indices)
    #n_replicates = len(SP.unique(replicate_indices))
#    
#    logthetaCOVAR = [1,1]
#    logthetaCOVAR.extend(SP.repeat(SP.exp(1),n_replicates))
#    logthetaCOVAR.extend([sigma1])
#    logthetaCOVAR = SP.log(logthetaCOVAR)#,sigma2])
#    hyperparams = {'covar':logthetaCOVAR}
#    
    SECF = se.SqexpCFARD(dim)
    #noiseCF = noise.NoiseReplicateCF(replicate_indices)
    noiseCF = noise.NoiseCFISO()
    
    shiftCFInd1 = combinators.ShiftCF(SECF,replicate_indices)
    shiftCFInd2 = combinators.ShiftCF(SECF,replicate_indices)
    shiftCFCom = combinators.ShiftCF(SECF,SP.concatenate((replicate_indices,replicate_indices+n_replicates)))

    CovFun = combinators.SumCF((SECF,noiseCF))
    
    covar_priors_common = []
    covar_priors_individual = []
    covar_priors = []
    #scale
    covar_priors_common.append([lnpriors.lnGammaExp,[1,2]])
    covar_priors_individual.append([lnpriors.lnGammaExp,[1,2]])
    covar_priors.append([lnpriors.lnGammaExp,[1,2]])
    for i in range(dim):
        covar_priors_common.append([lnpriors.lnGammaExp,[1,1]])
        covar_priors_individual.append([lnpriors.lnGammaExp,[1,1]])
        covar_priors.append([lnpriors.lnGammaExp,[1,1]])
    #shift
    for i in range(2*n_replicates):
        covar_priors_common.append([lnpriors.lnGauss,[0,.5]])
    for i in range(n_replicates):
        covar_priors_individual.append([lnpriors.lnGauss,[0,.5]])
        
    covar_priors_common.append([lnpriors.lnuniformpdf,[0,0]])
    covar_priors_individual.append([lnpriors.lnuniformpdf,[0,0]])
    covar_priors.append([lnpriors.lnuniformpdf,[0,0]])
    #noise
    for i in range(1):
        covar_priors_common.append([lnpriors.lnGammaExp,[1,1]])
        covar_priors_individual.append([lnpriors.lnGammaExp,[1,1]])
        covar_priors.append([lnpriors.lnGammaExp,[1,1]])
    
    priors = get_model_structure({'covar':SP.array(covar_priors_individual)}, {'covar':SP.array(covar_priors_common)})
    #Ifilter = {'covar': SP.ones(n_replicates+3)}
    covar = [combinators.SumCF((combinators.SumCF((shiftCFInd1,FixedCF(X_conf_1))),noiseCF)),
             combinators.SumCF((combinators.SumCF((shiftCFInd2,FixedCF(X_conf_2))),noiseCF)),
             combinators.SumCF((combinators.SumCF((shiftCFCom,
                                                   FixedCF(X_conf_comm))),
                                noiseCF))]
    
    csv_out_file = open(os.path.join('out', "result.csv"), 'wb')
    csv_out = csv.writer(csv_out_file)
    header = ["Gene", "Bayes Factor"]
    
    header.extend(map(lambda x:'Common '+x,covar[2].get_hyperparameter_names()))
    header.extend(map(lambda x:'Individual '+x,covar[0].get_hyperparameter_names()))
    csv_out.writerow(header)
    
    twosample_object = GPTwoSample_individual_covariance(covar,
                                                         priors=priors)
    print 'sorting out genes not in ground truth'
    gt_reader = csv.reader(open('./ground_truth_random_genes.csv','r'))
    gene_names = []
    for line in gt_reader:
        gene_names.append(line[0].upper())
    still_to_go = len(gene_names)
    #loop through genes
    for gene_name in gene_names:
        try:
            #PL.close()
            #PL.close()
            if gene_name is "input":
                continue
            #expression levels: replicates x #time points
            Y0 = cond1[gene_name]
            Y1 = cond2[gene_name]
            #create data structure for GPTwwoSample:
            #note; there is no need for the time points to be aligned for all replicates
            #creates score and time local predictions
            twosample_object.set_data(get_training_data_structure(SP.tile(T1,Y0.shape[0]).reshape(-1, 1),
                                                                  SP.tile(T2,Y1.shape[0]).reshape(-1, 1),
                                                                  Y0.reshape(-1, 1),
                                                                  Y1.reshape(-1, 1)))
            print 'processing %s, genes still to come: %i'%(gene_name,still_to_go)
            twosample_object.predict_model_likelihoods()
            twosample_object.predict_mean_variance(Tpredict)
    
            line = [gene_name, twosample_object.bayes_factor()]
            common = twosample_object.get_learned_hyperparameters()[common_id]['covar']
            individual = twosample_object.get_learned_hyperparameters()[individual_id]['covar']
            timeshift_index = scipy.array(scipy.ones_like(common), dtype='bool')
            timeshift_index[dim + 1:dim + 1 + n_replicates_1+n_replicates_2] = 0
            common[timeshift_index] = scipy.exp(common[timeshift_index])
            timeshift_index = scipy.array(scipy.ones_like(individual), dtype='bool')
            timeshift_index[dim + 1:dim + 1 + n_replicates_1] = 0
            individual[timeshift_index] = scipy.exp(individual[timeshift_index])
            line.extend(common)
            line.extend(individual)
            csv_out.writerow(line)
            
            #print 'plotting %s'%(gene_name)
            #plot_results(twosample_object,
            #             title=r'%s: $\log(p(\mathcal{H}_I)/p(\mathcal{H}_S)) = %.2f $' % (gene_name, twosample_object.bayes_factor()),
            #             shift=twosample_object.get_learned_hyperparameters()[common_id]['covar'][2:2+2*n_replicates],
            #             draw_arrows=1)
            #PL.xlim(T1.min(), T1.max())
            #PL.savefig("out/GPTwoSample_%s_raw.png"%(gene_name),format='png')
            #PL.figure()
            
            #yres_1 = g.predict(opt_hyperparams_1,opt_hyperparams_1['x'],var=False,output=components)
            #yres_2 = g.predict(opt_hyperparams_2,opt_hyperparams_2['x'],var=False,output=components)
            yres_comm = g.predict(opt_hyperparams_comm,opt_hyperparams_comm['x'],var=False,output=components)
            yres_len = yres_comm.shape[0]
            yres_1 = yres_comm[:yres_len/2]
            yres_2 = yres_comm[yres_len/2:]
            
            twosample_object.set_data(get_training_data_structure(SP.tile(T1,Y0.shape[0]).reshape(-1, 1),
                                                                  SP.tile(T2,Y1.shape[0]).reshape(-1, 1),
                                                                  (Y0.reshape(-1)-yres_1).reshape(-1, 1),
                                                                  (Y1.reshape(-1)-yres_2).reshape(-1, 1)))
            twosample_object.predict_model_likelihoods()
            twosample_object.predict_mean_variance(Tpredict)
    #        plot_results(twosample_object,
    #                     title=r'%s: $\log(p(\mathcal{H}_I)/p(\mathcal{H}_S)) = %.2f $' % (gene_name, twosample_object.bayes_factor()),
    #                     shift=twosample_object.get_learned_hyperparameters()[common_id]['covar'][2:2+2*n_replicates],
    #                     draw_arrows=1)
    #        PL.xlim(T1.min(), T1.max())
    #        
    #        PL.savefig("out/GPTwoSample_%s_confounder.png"%(gene_name),format='png')
            ## wait for window close
            #import pdb;pdb.set_trace()
        except:
            import sys
            print "Caught Failure on gene %s: " % (gene_name),sys.exc_info()[0]
            print "Genes left: %i"%(still_to_go)
        finally:
            still_to_go -= 1
        pass

if __name__ == '__main__':
    run_demo(cond1_file = './warwick_control.csv', cond2_file = 'warwick_treatment.csv')
