"""
Log Analyzer module.

InvalidLogFormatException: Exception which may be used to propagate errors related to log file format.
LogAnalyzer: Analyzes log file.

"""
from datetime import datetime
import collections

import util


class InvalidLogFormatException(Exception):
    pass # Could be used if needed to propagate for any invalid log format exception.


class LogAnalyzer(object):
    """ Analyzes log file. 
    
    Attributes:
        logPath: @string path to the log file.
        delim: @string delimiter used in the log file.
        dFormat: @string Date format used in the log file. 
    """
    
    ERR_SUCESS = 200
    IDX_DATE = 0
    D_FORMAT = '%m-%d-%Y'

    def __init__(self, logPath, delim='\t', dFormat='%Y-%m-%dT%H:%M:%S'):
        
        self.logPath = logPath
        self.delim = delim
        self.dFormat = dFormat
        self._logs = []
        self._errors = 0
        self._requests = 0
        self._users = set()
        self._dailyUniques = collections.OrderedDict()
        self._parse_log()
    
    def _parse_log(self):
        with open(self.logPath, 'r') as infile:
            for line in infile:
                if not line.strip():
                    continue
                try:
                    dt, usr, err = line.split(self.delim)
                    d = datetime.strptime(dt, self.dFormat)
    
                    self._logs.append((d, usr, err))
                    self._users.add(usr)
                    if int(err) != self.ERR_SUCESS:
                        self._errors += 1
                except ValueError:
                    pass
    
    """Returns number for requests."""
    def requests(self):
        return len(self._logs)

    """Returns number of error requests, any requests not 200 is considered as errors"""
    def errors(self):
        return self._errors
    
    """Number of unique days."""
    def days(self):
        if not  self._logs:
            return 0
        if len(self._logs) == 1:
                return 1
        return abs((self._logs[0][self.IDX_DATE] - self._logs[-1][self.IDX_DATE]).days)
    
    """Number of unique users."""
    def users(self):
        return len(self._users)
 
    """Daily unique requests."""
    def users_daily(self):
        if self._dailyUniques or not self._logs:
            return self._dailyUniques
        for dt in util.daterange(self._logs[0][self.IDX_DATE],
                                 self._logs[-1][self.IDX_DATE]):
            self._dailyUniques.update({dt.strftime(self.D_FORMAT): 0})
            
        for l in self._logs:
            dailyCount = self._dailyUniques[l[self.IDX_DATE].strftime(self.D_FORMAT)]
            self._dailyUniques.update({l[self.IDX_DATE].strftime(self.D_FORMAT): dailyCount + 1})
        return self._dailyUniques
    
    @classmethod
    def report(cls, pathFile):
        lA = LogAnalyzer(pathFile)
        print  'Totals \n ---- \n Requests {} \n Errors {} \n Days {} \n Unique Users {} \n'.format(
            lA.requests(), lA.errors(), lA.days(), lA.users())
        
        print 'Daily Uniques \n ----------- \n'
        for k, v in lA.users_daily().iteritems():
            print k, v
            
        
        
        



