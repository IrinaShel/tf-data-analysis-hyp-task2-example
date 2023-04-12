import pandas as pd
import numpy as np
import plotly.graph_objects as go
import warnings

from hyppo.ksample import Energy, MMD, DISCO
from scipy.stats import laplace, norm, ks_2samp, anderson_ksamp, cramervonmises_2samp
from statsmodels.stats.weightstats import ztest
from statsmodels.distributions.empirical_distribution import ECDF
from scipy import stats

chat_id = 5351182285 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    res = stats.cramervonmises_2samp(x, y)
    Result = bool (res.pvalue<=0.06)
    return Result # Ваш ответ, True или False
