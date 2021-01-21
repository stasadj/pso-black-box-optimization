import numpy as np
from pso import get_options, pso
from ann_criterion import get_ann_output

'''
******************* Projektni zadatak 12 *******************
Autori: Anastasija Đurić SW48-2018, Nenad Petković SW37-2018 
'''


if __name__ == "__main__":

    opts = get_options()

    print('\nVALUES OF THE PARAMETERS ON THE BEGIN')
    print('********************************************************')
    print('w: ', opts['w'])
    print('cp: ', opts['cp'])
    print('cg: ', opts['cg'])
    print('********************************************************\n')

    w, y = pso(opts)

    print("OPTIMAL SET OF SYNAPTIC WEIGHTS:\n")
    print(w)
    print("\nMEAN ABSOLUTE ERROR FOR OPTIMAL SET OF SYNAPTIC WEIGHTS: ",  y)

    print('\nVALUES OF THE PARAMETERS ON THE END')
    print('********************************************************')
    print('w: ', opts['w'])
    print('cp: ', opts['cp'])
    print('cg: ', opts['cg'])
    print('********************************************************\n')

    x1 = np.array([0.5819, 0.3683, 0.4413])
    y1 = 0.3675
    x2 = np.array([0.5257, 0.8034, 0.3369])
    y2 = 0.4502
    x3 = np.array([0.5464, 0.5087, 0.2151])
    y3 = 0.323
    x4 = np.array([0.0368, 0.4483, 0.1082])
    y4 = 0.0932
    x5 = np.array([0.3923, 0.8577, 0.844])
    y5 = 0.554
    x6 = np.array([0.2598, 0.8384, 0.4308])
    y6 = 0.3847
    x7 = np.array([0.2948, 0.7698, 0.8535])
    y7 = 0.4811
    x8 = np.array([0.3932, 0.6851, 0.5644])
    y8 = 0.4076
    x9 = np.array([0.3504, 0.1667, 0.0203])
    y9 = 0.1258
    x10 = np.array([0.5699, 0.083, 0.2821])
    y10 = 0.2843

    print('\n******************* TEST *******************')
    print('TEST 1')
    print('*********************************************')
    print('EXPECTED: ', y1)
    print('AFTER OPTIMIZATION: %f' % get_ann_output(x1, w))
    print('*********************************************')
    print('TEST 2')
    print('*********************************************')
    print('EXPECTED: ', y2)
    print('AFTER OPTIMIZATION: %f' % get_ann_output(x2, w))
    print('*********************************************')
    print('TEST 3')
    print('*********************************************')
    print('EXPECTED: ', y3)
    print('AFTER OPTIMIZATION: %f' % get_ann_output(x3, w))
    print('*********************************************')
    print('TEST 4')
    print('*********************************************')
    print('EXPECTED: ', y4)
    print('AFTER OPTIMIZATION: %f' % get_ann_output(x4, w))
    print('*********************************************')
    print('TEST 5')
    print('*********************************************')
    print('EXPECTED: ', y5)
    print('AFTER OPTIMIZATION: %f' % get_ann_output(x5, w))
    print('*********************************************')
    print('TEST 6')
    print('*********************************************')
    print('EXPECTED: ', y6)
    print('AFTER OPTIMIZATION: %f' % get_ann_output(x6, w))
    print('*********************************************')
    print('TEST 7')
    print('*********************************************')
    print('EXPECTED: ', y7)
    print('AFTER OPTIMIZATION: %f' % get_ann_output(x7, w))
    print('*********************************************')
    print('TEST 8')
    print('*********************************************')
    print('EXPECTED: ', y8)
    print('AFTER OPTIMIZATION: %f' % get_ann_output(x8, w))
    print('*********************************************')
    print('TEST 9')
    print('*********************************************')
    print('EXPECTED: ', y9)
    print('AFTER OPTIMIZATION: %f' % get_ann_output(x9, w))
    print('*********************************************')
    print('TEST 10')
    print('*********************************************')
    print('EXPECTED: ', y10)
    print('AFTER OPTIMIZATION: %f' % get_ann_output(x10, w))
    print('*********************************************')
