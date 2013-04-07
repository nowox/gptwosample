'''
Created on Apr 3, 2013

@author: Max
'''
import unittest
import numpy
from gptwosample.twosample.twosample import TwoSample
from numpy.core.numeric import nan

class TwoSampleTest(unittest.TestCase):

    T = numpy.array([[[  0., 2., 4., 6., 8., 10., 12., 14.],
            [  0., 2., 4., 6., 8., 10., 12., 14.],
            [  0., 2., 4., 6., 8., 10., 12., 14.]],
           [[  0., 2., 4., 6., 8., 10., 12., 14.],
            [  0., 2., 4., 6., 8., 10., 12., 14.],
            [  0., 2., 4., 6., 8., 10., 12., 14.]]])
    
    Y = numpy.array([[[[  2.14579517e+00, 2.96579595e-01, 1.38920467e+00,
                1.62477024e+00, 2.21869490e+00, -1.18969549e+00,
                6.93117644e-01, -3.03311252e-01, nan,
                3.02391619e-01, nan, 1.21613243e+00,
                2.39684579e+00, -3.97906432e-02, 5.80740179e-02,
                5.95675943e-01, nan, 3.08722056e-01],
             [  2.65333710e+00, 3.19203533e-01, 6.37226195e-01,
                2.10687791e+00, 2.47249846e+00, nan,
                2.34241260e-01, nan, -2.17574541e+00,
               - 1.43970754e-01, -5.19409109e-01, nan,
                1.25490245e+00, nan, 5.87588930e-01,
               - 3.49621566e-01, nan, 1.03119718e+00],
             [  1.59889719e+00, -8.81133965e-01, -7.70939019e-01,
                           nan, nan, -2.92455085e-01,
               - 4.65845206e-01, 7.04523668e-01, nan,
               - 1.26463088e+00, -8.11280446e-02, nan,
                1.79157238e+00, 1.12607610e+00, 6.48103683e-02,
                1.05253533e+00, nan, nan],
             [  1.57269151e+00, -8.35945985e-01, -1.46347229e+00,
               - 1.83542757e+00, nan, nan,
               - 7.37408479e-01, 1.53185219e+00, -8.34120232e-01,
                           nan, -1.41739630e+00, nan,
                1.19370108e+00, nan, nan,
                6.49709800e-01, 1.42063351e+00, -7.75979160e-01],
             [  5.43180505e-02, 3.49192860e-02, -2.61302147e+00,
                           nan, -6.24082233e-01, -9.57452300e-01,
                           nan, nan, -3.93662153e-01,
               - 1.90737426e-01, -1.20684981e+00, 4.20406647e-02,
                1.32387960e+00, -8.53394165e-02, -1.72852733e+00,
               - 5.09919196e-01, 1.08639922e+00, -1.29440182e+00],
             [  3.60738472e-02, -9.41766954e-01, nan,
               - 2.68274712e+00, -5.49459700e-02, nan,
               - 2.18390232e+00, 7.83417692e-01, nan,
                           nan, -2.29213282e-01, -4.89329851e-01,
                6.78126579e-01, nan, nan,
               - 1.08302447e+00, 1.06360703e+00, -6.33152700e-01],
             [  1.41712556e+00, 3.39646495e-01, nan,
               - 1.52452184e+00, -2.23450284e+00, -9.05167846e-01,
               - 6.82578422e-01, nan, -1.82236522e-01,
                1.35852244e+00, 2.63874879e-01, nan,
               - 9.11938564e-01, -5.19549554e-01, -1.41349887e+00,
                           nan, 1.92456649e+00, -3.38953237e-01],
             [             nan, 9.59506204e-01, nan,
               - 5.77781354e-01, -1.41815031e+00, -6.96559853e-01,
               - 1.03946168e+00, 1.11583081e+00, -1.12461577e-01,
                1.03486792e+00, nan, nan,
               - 2.48504724e+00, -1.85738243e+00, -2.00528806e+00,
                6.89585899e-01, 7.80645476e-01, -2.47209153e-01]],
    
            [[  2.32985312e+00, 7.70399030e-01, 1.66513978e+00,
                           nan, 2.37318602e+00, 9.84400888e-02,
                8.74605969e-01, nan, -7.83750457e-01,
                           nan, 7.81780865e-01, 8.89828168e-01,
                7.21540140e-01, -9.50591166e-01, 1.25939924e-01,
                9.41682868e-02, 1.35571466e+00, 8.06203878e-01],
             [  2.63397357e+00, -9.87015269e-01, 5.50224639e-01,
                1.59465974e+00, 2.84875038e+00, -3.33675641e-01,
                5.69518160e-01, -5.17941981e-01, nan,
               - 8.53880543e-01, 8.33086885e-01, -1.69782215e-01,
                1.65709572e+00, 1.26732009e+00, nan,
                4.49338894e-01, nan, 9.38717887e-01],
             [  1.79213259e+00, -1.93210092e-01, 5.95990927e-01,
                1.69106966e+00, 1.44845312e+00, -2.45026071e-01,
                           nan, nan, -1.34634039e+00,
               - 5.73288654e-01, 4.29912373e-01, 7.25578195e-02,
                1.53061214e+00, 3.45181325e-01, -5.03956361e-01,
                           nan, 1.81447116e+00, -9.64521892e-02],
             [  1.45639034e+00, 2.32695343e-01, -4.07450887e-01,
               - 4.63731069e-01, 1.90114591e-01, -1.12438933e+00,
                           nan, nan, -1.08746520e+00,
                           nan, 2.18190717e-01, 1.70827165e+00,
                2.06044998e+00, -9.56532861e-01, 1.19846714e-01,
                           nan, nan, -3.66402086e-01],
             [ -7.51847812e-01, 3.15871349e-01, nan,
               - 8.96961312e-01, -1.61934696e+00, -1.05106457e+00,
               - 2.28004207e+00, 1.56679661e+00, -7.11034020e-01,
                           nan, -9.17289122e-01, 9.08843010e-02,
                1.29571698e+00, nan, -1.10847685e+00,
                           nan, 1.05851630e+00, -1.95211310e+00],
             [  5.12637637e-02, -1.17030867e-01, 2.83494215e-01,
                           nan, -9.86308341e-01, -1.11379648e+00,
               - 1.61637039e+00, nan, nan,
                1.32247106e+00, 2.97574956e-01, 8.80528163e-02,
                           nan, -4.19104285e-01, -8.66732961e-02,
               - 7.55252269e-01, 1.49148144e+00, -2.09112601e+00],
             [             nan, -4.74957305e-01, -2.78203021e-01,
               - 1.74538416e+00, nan, -2.90755657e-01,
               - 3.77456789e-01, 1.77391437e+00, -9.34031104e-01,
                4.20555369e-01, 4.68035016e-01, nan,
                           nan, 2.66176663e-01, nan,
                           nan, 1.58970987e-01, -4.88304750e-01],
             [  9.85096153e-01, 7.98817176e-01, 1.10799756e+00,
                1.17976805e-01, -4.81783928e-01, nan,
               - 1.43217469e+00, 1.67692210e+00, -9.79427225e-01,
                4.70942650e-01, 1.04677995e+00, -8.40005013e-04,
               - 1.38946873e+00, -1.40728383e+00, -2.23266264e+00,
                9.02795220e-01, -4.07139508e-01, 2.07558151e-01]],
    
            [[  2.96675258e+00, 8.35277412e-01, nan,
                2.62697702e+00, 2.90949418e+00, -7.70232874e-01,
                3.23164682e-01, 4.39047921e-02, -1.24668506e+00,
                3.29268293e-01, 2.60240917e-01, 6.47438400e-01,
                           nan, -3.29411841e-01, 1.11432749e-01,
               - 2.51144865e-01, 1.38862744e+00, 4.11887446e-01],
             [  3.08321168e+00, -1.08602916e+00, 7.58407751e-01,
                9.02018189e-01, 2.59206512e+00, nan,
                           nan, nan, nan,
                3.66955156e-01, 9.13426491e-02, nan,
                6.57172095e-01, nan, 1.31554877e-01,
                6.26140166e-01, 3.51437921e-01, 7.75019827e-01],
             [  1.66124288e+00, -1.02031061e+00, 4.78695349e-03,
                1.93768881e-01, 2.07364063e+00, 5.16568103e-01,
               - 3.50178576e-01, nan, -2.73174355e+00,
               - 1.65626791e+00, -2.44743553e-01, nan,
                2.42511257e+00, nan, nan,
                1.41924915e+00, nan, 6.33617617e-01],
             [  1.23964729e+00, nan, -5.16101318e-01,
                4.25505873e-02, 6.43570336e-01, nan,
               - 9.30713294e-01, nan, -2.17320614e+00,
                           nan, -1.85539682e+00, 4.46283568e-01,
                           nan, -3.74613066e-01, -7.29506570e-01,
               - 4.21009861e-01, 1.86187024e+00, -1.03281563e+00],
             [ -9.15503534e-01, -4.81578357e-01, -1.08997849e+00,
               - 1.24107772e+00, -1.15866119e+00, -1.65475413e+00,
               - 2.03490935e+00, nan, nan,
                2.87356716e-01, -1.23734116e+00, 1.08401910e+00,
                4.76756428e-01, nan, nan,
               - 6.57739357e-01, 1.21759047e+00, -1.90741274e+00],
             [ -7.68250888e-01, -6.98520740e-01, 1.19338433e-01,
               - 1.13991008e+00, -2.07349707e-01, -2.20002840e-01,
               - 1.39890845e+00, 7.02367140e-01, -1.22239392e+00,
                7.79945276e-01, 7.44498502e-01, -8.50916874e-01,
                4.05873770e-02, 1.01166859e+00, -8.41316356e-01,
               - 1.22041649e+00, 6.75747300e-01, nan],
             [  9.79268207e-01, 7.78612252e-02, -3.85010347e-01,
               - 6.42887469e-01, -7.84525549e-01, nan,
                           nan, 1.12944519e+00, -7.21194459e-01,
                1.05434802e+00, 7.70188759e-01, -9.11000374e-01,
                           nan, nan, -1.08305038e+00,
               - 2.93932251e-01, 7.63281938e-01, 4.63934743e-01],
             [  1.36063260e+00, nan, -2.00289981e-01,
               - 1.01174837e-01, -1.23277441e+00, 2.95254707e-01,
               - 3.19203240e-01, 1.06069339e+00, -1.41155496e+00,
                           nan, 7.32463404e-01, nan,
                           nan, -8.29407654e-01, -1.05592696e+00,
                1.09937917e+00, 1.58877614e+00, -8.46351437e-01]]],
    
    
           [[[  3.98782477e-01, 2.78997848e+00, 7.93521975e-01,
                2.06136083e+00, 1.00441074e+00, nan,
                           nan, 1.23821346e+00, -1.26399375e+00,
                2.32841004e+00, 2.74766963e-01, 5.23738395e-01,
                1.90967388e+00, -8.50437648e-01, 3.80819007e-01,
                8.45006737e-01, -7.33408015e-01, 9.12421200e-01],
             [  2.28187863e+00, 1.78482665e+00, 1.11789869e+00,
                1.16565894e+00, 4.86071106e-01, 1.16093684e+00,
               - 8.57517925e-01, 2.36797012e+00, 1.02518852e-01,
                6.82659182e-01, 5.16035765e-01, nan,
                1.46204262e+00, 7.56929191e-01, 6.84115347e-01,
                5.08375160e-01, nan, nan],
             [  8.94559007e-01, nan, 8.37835148e-01,
                1.49516300e+00, -5.12803593e-01, 1.07718726e+00,
                           nan, 1.14843855e+00, 1.00245428e-01,
                           nan, -6.02205190e-01, 9.49724621e-01,
                1.56862958e+00, -5.72564533e-01, -8.77057524e-01,
               - 3.12969807e-03, 1.50744143e+00, nan],
             [  2.21646599e+00, -3.60754769e-01, nan,
                1.93126757e+00, -4.38991256e-01, -8.95418799e-02,
               - 4.06004767e-01, 7.21731442e-01, -1.12957578e+00,
                           nan, -1.10489599e+00, -1.11772584e-01,
                2.52230659e-01, -3.73152542e-01, -1.04013083e+00,
                1.51382632e-01, 9.76180660e-01, -6.87060028e-01],
             [  2.13191248e+00, -4.38754118e-01, -8.48839747e-01,
                           nan, nan, nan,
                5.19933675e-01, 3.84920564e-01, -1.53289570e+00,
               - 3.03570663e-01, nan, nan,
               - 1.26247709e+00, -1.21660256e+00, -6.14312302e-01,
                7.79002146e-01, nan, -1.40439587e+00],
             [  2.60238317e+00, 4.08097022e-01, -6.71847048e-01,
                2.40952896e-01, nan, 1.31977958e+00,
                6.84863622e-01, nan, -2.39819834e+00,
                6.09691684e-01, -1.85852673e+00, nan,
                           nan, nan, nan,
                           nan, 1.18515283e+00, -1.27281954e+00],
             [             nan, -3.54190845e-01, -2.86666905e-02,
               - 1.28715319e+00, nan, -1.84771662e-01,
                           nan, nan, nan,
                1.02331724e+00, -1.29124136e+00, -3.87234966e-01,
               - 2.04756250e+00, nan, 1.27133285e+00,
               - 3.07635564e-01, 9.79032149e-01, 1.52762202e+00],
             [  7.18605160e-01, -1.34774330e+00, 2.39931936e-01,
               - 1.77662235e+00, 4.13720202e-01, -1.35667376e+00,
                           nan, 3.21806006e-01, -1.23678332e+00,
                1.07714440e+00, nan, -5.04512001e-01,
               - 8.74677276e-01, 1.21039833e+00, 6.70048663e-01,
                5.93010386e-01, 1.52704886e+00, 1.81923032e+00]],
    
            [[  5.24095832e-01, 2.74672747e+00, 5.48077089e-01,
                2.05924894e+00, 2.31038657e-01, -1.09314886e+00,
                           nan, 1.93265272e+00, -6.87450081e-01,
                1.51561715e+00, -1.97541252e-01, -3.49549181e-01,
                2.46513500e+00, -6.30837680e-01, 3.19974300e-01,
                           nan, -3.54308434e-01, 1.41368731e+00],
             [  8.74497482e-01, 1.55837396e+00, 1.18278763e+00,
                1.41152540e+00, -1.14416186e-01, nan,
                           nan, 1.85712325e+00, -8.16611679e-03,
                           nan, nan, -1.65800000e-01,
                           nan, 1.39177428e-02, -5.62861141e-03,
                2.27154239e-01, nan, 9.51289917e-01],
             [  1.21267775e+00, 6.91676347e-01, 4.25500613e-01,
                1.49804775e+00, -6.28483779e-01, 4.11697481e-01,
                           nan, 1.99167522e+00, -1.11737609e+00,
                4.33878036e-01, -3.25705872e-01, nan,
               - 8.65370657e-01, 6.51103821e-01, -1.08855885e+00,
               - 2.05198960e-01, 4.52031600e-01, -2.88402817e-01],
             [  4.49263361e-01, nan, nan,
                1.65390984e+00, nan, nan,
               - 6.50692134e-01, 1.13630035e+00, -1.62441467e+00,
                2.63439706e-01, -6.49327697e-02, -3.23511441e-01,
                9.95626187e-01, -2.97210799e-01, -8.48672263e-01,
                6.59634312e-01, 1.49299418e+00, -6.41087842e-01],
             [  2.04648760e+00, -5.05478499e-01, -1.00701023e+00,
                1.89583965e+00, -1.22235460e+00, 6.91465120e-01,
                2.39330703e-01, -1.33931077e-01, -1.46288364e+00,
                           nan, -3.86375796e-01, -8.21413425e-01,
                           nan, -1.71446033e+00, -4.64321033e-01,
               - 1.04773380e+00, 1.59735112e+00, -1.00826545e+00],
             [  2.16946048e+00, nan, -5.83818359e-01,
               - 1.19321630e-01, -1.69294216e-01, nan,
                           nan, 1.33071099e+00, -2.49719850e+00,
               - 1.25035045e+00, -1.25639899e+00, -1.04826883e+00,
               - 6.62771373e-01, nan, nan,
               - 5.03608105e-01, 8.35325805e-01, -1.13841680e+00],
             [  1.25526450e+00, -1.12291342e+00, -5.37206490e-01,
               - 1.15544168e+00, nan, 1.84855081e-03,
                           nan, 5.03794627e-01, nan,
                1.39219328e+00, nan, -4.62707506e-01,
               - 1.49577793e+00, nan, nan,
               - 7.70578702e-01, 2.10344471e-03, nan],
             [  3.81958497e-01, -1.36738488e+00, -7.28363423e-01,
               - 2.11679141e+00, 1.29598104e+00, nan,
               - 1.79025734e+00, nan, -1.97099099e+00,
                1.68650819e+00, -2.36869099e+00, 4.92759157e-01,
                           nan, 7.12536640e-01, -2.17916789e-02,
                           nan, nan, 9.99625217e-01]],
    
            [[             nan, nan, 1.24151980e+00,
                1.15620081e+00, 1.83959673e+00, 5.80402427e-01,
               - 8.26155182e-01, 1.99243731e+00, -3.55964955e-02,
                1.33847663e+00, -1.10631942e-01, 4.72001880e-02,
                2.10363319e+00, -6.48307656e-01, 7.73295591e-01,
                6.64164906e-01, nan, 1.62754446e+00],
             [  2.09607326e+00, 2.01153684e+00, 2.01623449e+00,
                2.22342599e+00, nan, 7.41981629e-01,
               - 1.16468464e+00, 1.40461738e+00, -2.88115532e-01,
                           nan, 6.84297515e-01, 1.31532552e+00,
                           nan, nan, nan,
                7.69270993e-01, -6.99649913e-01, 1.48073564e+00],
             [  1.34514240e+00, nan, -5.64919284e-01,
                           nan, -9.75555879e-01, 4.09633665e-01,
                           nan, 2.08020849e+00, -1.64386313e-02,
                2.61636744e-01, -4.69131478e-01, 8.41451499e-01,
                8.23486808e-01, -1.28471467e+00, 1.69057316e-01,
               - 3.97273333e-01, 1.92517297e+00, -2.38795496e-01],
             [             nan, 3.33120912e-01, -1.18183280e+00,
                1.22892872e+00, -7.54333822e-01, 5.35064178e-01,
                1.68251061e-01, nan, -1.51262490e+00,
                           nan, -3.48335432e-01, 2.11943797e-01,
               - 3.43698382e-02, -8.84563501e-01, nan,
                6.64040618e-01, nan, nan],
             [  2.28690422e+00, 3.10386948e-01, nan,
                9.05585346e-01, nan, -1.90522436e-01,
                1.62991828e-01, nan, -2.59803302e+00,
                           nan, -1.11295053e+00, nan,
               - 8.04008039e-01, nan, -7.41289686e-01,
               - 2.30112976e-01, 1.47629390e+00, -7.28842714e-01],
             [  2.11363682e+00, -1.46541713e+00, -1.80418289e+00,
               - 3.45606112e-01, 1.01448970e-01, 2.54664848e-01,
               - 9.87889076e-02, 1.19596778e+00, nan,
               - 6.37070653e-02, -1.14579385e+00, -1.96904860e+00,
               - 1.02147878e+00, nan, nan,
                           nan, 2.19443502e+00, -2.86768507e-01],
             [             nan, -5.47459943e-01, -7.00267728e-01,
                           nan, 7.99903885e-01, nan,
                           nan, 2.05875959e+00, -2.04075940e+00,
                4.47700713e-01, -1.62873252e+00, -1.38862941e+00,
               - 9.96899188e-01, 6.47022697e-01, nan,
               - 1.26806179e+00, 7.69166998e-01, 5.00449704e-01],
             [  6.00481312e-01, nan, -6.98694503e-01,
               - 2.12879532e+00, 7.11558217e-01, 3.68626669e-01,
               - 1.27077656e+00, 8.56908073e-01, -1.36523367e+00,
                6.95057788e-01, nan, 5.57781532e-02,
                2.56002517e-01, 2.90105557e-01, 8.64209525e-01,
                4.75897616e-01, nan, 1.69169376e+00]]]])
    
    @classmethod
    def setUpClass(cls):
        #cls.Y = Y
        #cls.T = T
        cls.n, cls.r, cls.t, cls.d = cls.Y.shape
        cls.twosample = TwoSample(cls.T, cls.Y)

    def setUp(self):
        pass


    def testLikelihoods(self):
        self.twosample.predict_likelihoods(self.T, self.Y, "Testing likelihoods...", False)
        pass

    def testPredict(self):
        interpolation_interval = numpy.linspace(self.T.min(), self.T.max(), 100)
        indices = numpy.random.randint(self.d, size=(self.d / 2))
        self.twosample.predict_means_variances(interpolation_interval, indices, "Testing Predictions...")
        pass

    def testBayesFactors(self):
        try:
            self.twosample.bayes_factors()
        except RuntimeError:
            self.twosample.predict_likelihoods(self.T, self.Y)
            self.twosample.bayes_factors()

#    def testPlot(self):
#        interpolation_interval = numpy.linspace(self.T.min(), self.T.max(), 100)
#        indices = numpy.random.randint(self.d, size=(self.d))
#        self.twosample.predict_means_variances(interpolation_interval, indices, "Testing Predictions")
#        pylab.ion()
#        pylab.figure()
#        for p in self.twosample.plot():
#            pylab.draw()
#            raw_input("enter continue...")


if __name__ == "__main__":

    import sys;sys.argv = ['',
                           'TwoSampleTest.testLikelihoods',
                           'TwoSampleTest.testPredict',
                           'TwoSampleTest.testBayesFactors',
                           # 'TwoSampleTest.testPlot',
                           ]
    unittest.main()
