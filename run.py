from config_private import MY_MUID
from microprediction import MicroCrawler
import numpy as np

class MyCrawler(MicroCrawler):

    def __init__(self,write_key):
        super().__init__(stop_loss=10,min_lags=0,sleep_time=15*60,write_key=write_key,quietude=1,verbose=False)

    def candidate_streams(self):
        return [name for name, sponsor in self.get_sponsors().items() if name[:2]=='z1' ]

    def sample(self, lagged_values, lagged_times=None ):
        """ Fat tails """
        return [1.05*s*(1+0.1*abs(s)) for s in sorted(np.random.randn(self.num_predictions)) ]  # Not to bad for z1-streams, terrible for most others

if __name__=="__main__":
    mw = MyCrawler(write_key=MY_MUID)
    mw.run()