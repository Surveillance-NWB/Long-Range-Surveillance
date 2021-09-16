import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

psnr_values = [11.73443930864366, 12.68676006415393, 13.879334937649377, 13.779041709426757, 13.331917545111885, 13.374542424160417, 12.985116908578775, 11.469910884492162, 10.502700119707796, 10.587873774429537, 11.185090879462171, 12.9664136065446, 13.044202235085688, 12.655916567478098, 13.355309340342014, 15.6653517579375, 10.638300004977406, 9.126427068146791, 9.366980546861537, 9.998192624657406, 10.869049484937959, 13.496017577699941, 15.20971418145277, 14.338435035409127, 
               12.957531383954935, 12.968465932577129, 12.798420747788006, 13.125943329853705, 13.868786649568715, 13.539050746545438, 12.50405888199487, 13.056218375389562, 13.240763159236181, 13.133407507293857, 13.633274752466704, 13.608978783412054, 13.122106967085783, 12.871340506975502, 12.85853977099541, 13.162944640825952, 13.462486449926395, 13.082990861359583, 13.113744389231258, 13.211715516958103, 12.565710163000718, 11.232493006465095, 10.314470365240126, 10.29877559227353, 10.197577656581366, 10.195400894695947, 10.548332390586285, 11.49708106887958, 10.958272047450226, 10.020847634060889, 9.923661030935975, 10.285910538109704, 10.369812476144258, 10.035073295689731, 9.721867238648699, 9.441774860981354, 9.580251580255208, 10.127936672030986, 9.859272117032065, 9.790509952184681, 9.981427941656678, 10.227007306580727, 10.325944692388392, 10.541012614291006, 11.02046789738562, 12.643697600565368, 13.564968131687035, 13.520312677122273, 13.536991411190176, 12.799469710059748, 11.176319095656257, 10.479535427820931, 10.3643732071469, 10.475069193172516, 10.964300942877527, 11.679171569786636, 12.247740052458989, 12.535375283637688, 12.550417107870047, 12.456047304136995, 12.257994143210816, 12.089635553479116, 11.936681833045832, 11.844470740983521, 11.630283294139439, 11.107200582763173, 10.565268262837343, 10.065830381168483, 9.903572321278515, 9.99712235424402, 10.26543615879107, 10.34642088443066, 10.24307023945103, 10.05252744860708, 9.903943222375815, 9.72810286354469, 9.72984586954994, 9.706431675611691, 9.732010262041499, 9.764175375408053, 9.74044584613848, 9.758992295787115, 9.774924753515963, 9.76996214480222, 9.756871605582818, 9.884770149901861, 9.909863780521171, 9.96564573330683, 9.96900617916957, 9.992394960238297, 10.063334599106575, 10.020170991976627, 10.051865379385754, 10.081704045532975, 10.046257050729006, 10.04598966802493, 9.984628694642781, 9.956278946378529, 10.266863063309657, 12.26007059669162, 12.768685733878698, 11.853780450363484, 11.09774554283369, 11.158673456396082, 11.217770116540146, 11.461817594974848, 11.635904594389494, 11.620633035377582, 11.797109514345907, 11.690406322417893, 11.991653995812062, 11.560444375467254, 10.779482059012329, 10.532036854350093, 12.702871857232221, 14.664905236010686, 14.55101573404341, 14.231955774261195, 12.834841618060226, 9.63551312303644, 9.5343801528685, 9.537468184478481, 9.521425105325946, 9.443493464566943, 9.4374924081071, 9.971830227231095, 10.133400538957346, 9.734087083827976, 9.532804139229635, 9.601024814501324, 9.873906160008918, 10.167198743599675, 10.56350710645444, 10.749625364327448, 11.074186443859833, 12.265854192261811, 13.355302510966965, 13.92374968774005, 14.42560178035749, 14.525329118313884, 14.476013978729952, 13.922257628131442, 11.282331547719703, 10.269758551785092, 9.902727568915816, 9.82886607089361, 9.698170523801915, 9.63054055217016]

sns.set_style('darkgrid')

sns.distplot(psnr_values)
plt.ylabel('PSNR VALUE')

plt.title('Peak Signal-to-Noise Ratio Distribution')

plt.show()