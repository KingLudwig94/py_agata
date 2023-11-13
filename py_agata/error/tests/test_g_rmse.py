import pandas as pd
import numpy as np
import datetime
from datetime import datetime, timedelta

from py_agata.error import g_rmse


def test_g_rmse():
    """
    Unit test of g_rmse function.

    Parameters
    ----------
    None

    Returns
    -------
    None

    Raises
    ------
    None

    See Also
    --------
    None

    Examples
    --------
    None

    References
    ----------
    None
    """
    # Set test data
    t = np.arange(datetime(2000, 1, 1, 0, 0, 0), datetime(2000, 1, 1, 0, 55, 0), timedelta(minutes=5)).astype(
        datetime)
    glucose = np.zeros(shape=(t.shape[0],))
    glucose[0] = 40
    glucose[1:3] = [50, 50]
    glucose[3] = 80
    glucose[4:6] = [120, 120]
    glucose[6:8] = [200, 200]
    glucose[8:10] = [260, 260]
    glucose[10] = np.nan
    d = {'t': t, 'glucose': glucose}
    data = pd.DataFrame(data=d)

    t = np.arange(datetime(2000, 1, 1, 0, 0, 0), datetime(2000, 1, 1, 0, 55, 0), timedelta(minutes=5)).astype(
        datetime)
    glucose = np.zeros(shape=(t.shape[0],))
    glucose[0] = 30
    glucose[1:3] = [70, 70]
    glucose[3] = 70
    glucose[4:6] = [130, 130]
    glucose[6:8] = [np.nan, np.nan]
    glucose[8:10] = [260, 260]
    glucose[10] = 260
    d = {'t': t, 'glucose': glucose}
    data_hat = pd.DataFrame(data=d)

    #Tests
    assert np.isnan(g_rmse(data,data_hat)) == False
    assert np.round(g_rmse(data,data_hat)*1000)/1000 == 12.990

    d = {'t': [], 'glucose': []}
    data_hat = pd.DataFrame(data=d)
    d = {'t': [], 'glucose': []}
    data = pd.DataFrame(data=d)

    # Tests
    assert np.isnan(g_rmse(data, data_hat))

    d = {'t': [t[0]], 'glucose': [np.nan]}
    data_hat = pd.DataFrame(data=d)
    d = {'t': [t[0]], 'glucose': [120]}
    data = pd.DataFrame(data=d)

    # Tests
    assert np.isnan(g_rmse(data, data_hat))