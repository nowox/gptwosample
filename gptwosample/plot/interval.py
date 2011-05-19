'''
Created on Feb 18, 2011

@author: maxz
'''
import pylab as PL
import scipy as SP
from gptwosample.plot.plot_basic import plot_results
from gptwosample.data.data_base import individual_id, common_id

def plot_results_interval(twosample_interval_object, xlabel='Time/hr', ylabel='expression level'):
        """
        Plot results of resampling of a (subclass of) 
        :py:class:`gptwosample.twosample.twosample_interval`.
        This method will predict some data new, for plotting purpose.
        
        **Parameters:**
        
        twosample_interval_object: :py:class:`gptwosample.twosample.twosample_interval`
            The GPTwosample resample object, from which to take the results.
        """
        
        predicted_indicators = twosample_interval_object.get_predicted_indicators()
        model_dist,Xp = twosample_interval_object.get_predicted_model_distribution()
        
        IS = predicted_indicators
        IJ = ~predicted_indicators
        IS = SP.tile(~IS, twosample_interval_object._n_replicates_comm/2)
        IJ = SP.tile(~IJ, twosample_interval_object._n_replicates_comm)

        # predict GPTwoSample object with indicators as interval_indices
        twosample_interval_object._twosample_object.predict_model_likelihoods(\
                                            interval_indices={individual_id:IS, common_id:IJ})
        twosample_interval_object._twosample_object.predict_mean_variance(Xp,\
                                            interval_indices={individual_id:IS, common_id:IJ})
                    
        #now plot stuff
        ax1 = PL.axes([0.15, 0.1, 0.8, 0.7])

        plot_results(twosample_interval_object._twosample_object, 
                     alpha=model_dist, 
                     legend=False,interval_indices={individual_id:IS, common_id:IJ},
                     xlabel=xlabel,
                     ylabel=ylabel)
        
        PL.xlim([Xp.min(), Xp.max()])
        yticks = ax1.get_yticks()[0:-2]
        ax1.set_yticks(yticks)
        
        data = twosample_interval_object._twosample_object.get_data(common_id)
        Ymax = data[1].max()
        Ymin = data[1].min()
        
        DY = Ymax - Ymin
        PL.ylim([Ymin - 0.1 * DY, Ymax + 0.1 * DY])
        #2nd. plot prob. of diff
        ax2 = PL.axes([0.15, 0.8, 0.8, 0.10], sharex=ax1)
        PL.plot(Xp, model_dist, 'k-', linewidth=2)
        PL.ylabel('$P(z(t)=1)$')
#            PL.yticks([0.0,0.5,1.0])
        PL.yticks([0.5])           
        #horizontal bar
        PL.axhline(linewidth=0.5, color='#aaaaaa', y=0.5)
        PL.ylim([0, 1])
        PL.setp(ax2.get_xticklabels(), visible=False)
