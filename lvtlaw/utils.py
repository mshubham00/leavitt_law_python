### File: ./lvtlaw/utils.py

data_dir = './data/input/'
data_file = 'cleaned_data.csv'
data_out='./data/output/'

"""
Extinction Law from Fouque 2007 &

"""
Ab_v = 1.31                                             #          = A_b / A_v
Av_v = 1                                                #          = A_v / A_v
Ai_v = 0.608                                            #          = A_i / A_v
Aj_v = 0.292                                            #          = A_j / A_v
Ah_v = 0.181                                            #          = A_h / A_v
Ak_v = 0.119                                            #          = A_k / A_v
'''
Ratio of total to selective absorption (Sandage 2004)- driving wavelength dependent value of R
'''
R_v = 3.23                                              #      R_V = A_v / E(B-V)
R_b = Ab_v*R_v                                          #      R_B = (A_b / A_v) * (A_v / E(B-V))
R_i = Ai_v*R_v                                          #          = (A_i / A_v) * (A_v / E(B-V))
R_j = Aj_v*R_v                                          #          = (A_j / A_v) * (A_v / E(B-V))
R_h = Ah_v*R_v                                          #          = (A_h / A_v) * (A_v / E(B-V))
R_k = Ak_v*R_v                                          #          = (A_k / A_v) * (A_v / E(B-V))


A = [Ab_v, Av_v, Ai_v, Aj_v, Ah_v, Ak_v]
R = [R_b, R_v, R_i, R_j, R_h, R_k]

def band_tick_genrate(data):
    pass

mag = ['B', 'V', 'I','J','H','K'];
bands = ['M_B', 'M_V', 'M_I', 'M_J', 'M_H', 'M_K']; 
band = len(bands);
ap_bands = ['B_mag', 'V_mag' ,'I_mag', 'J_mag', 'H_mag', 'K_mag']
col_dot = ['b.', 'g*', 'y+', 'r*', 'c+', 'g.', 'y+', 'b+'] ;
col_lin = ['b-', 'g-', 'y-', 'r-', 'c-', 'g-', 'y-', 'b-'] ;
col_das = ['b--', 'g--', 'y--', 'r--', 'c--', 'g--', 'y--', 'b--']
col_ = ['b', 'g', 'y', 'r', 'c', 'g', 'y', 'b'] ;


def color_index(mag = mag):
    color_index = []
    for i in range(0,len(mag)):
        for j in range(i+1,len(mag)):
            color_index.append(mag[i]+mag[j])
    print('Possible %i combinations of color indexes (str): \n'%(len(color_index)), color_index)
    return color_index

from scipy import stats
def regression(x: list, y: list, x_str: str, y_str: str, p = 0):
    regression_line = stats.linregress(x, y); 
    m = regression_line.slope; 
    c = regression_line.intercept
    prediction = m * x + c; 
    residue = y-prediction 
    m_error = regression_line.stderr; 
    c_error = regression_line.intercept_stderr
    if p == 1:
        print('%s = %f %s ( %f) + %f ( %f)'%(y_str, m, x_str, m_error, c, c_error))
    return m, c, prediction, residue, m_error, c_error

