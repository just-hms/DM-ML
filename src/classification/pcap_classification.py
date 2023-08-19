
import pickle
import pandas as pd

from utils import plot

assets_folder = './../../assets/'

# load data to classify
learning_data = pd.read_csv(assets_folder + 'UNSW-NB15-preprocessed.csv', low_memory=False)
learning_data_baseline = learning_data[learning_data['Label'] == 0]

pcap_baseline = pd.read_csv(assets_folder + 'CC22-final-only-bots.csv').iloc[:, 1:30]
pcap_also_attacks = pd.read_csv(assets_folder + 'CC22-final-also-attacks.csv').iloc[:, 1:30]

# load the models

models_folder = assets_folder + 'models/'

binary_model = pickle.load(open(models_folder + 'binary_model', 'rb'))
multiclass_model = pickle.load(open(models_folder + 'multiclass_model', 'rb'))

# scale features based on the dataset baseline

pcap_baseline_scaled = pcap_baseline.copy() 
pcap_also_attacks_scaled = pcap_also_attacks

print('SCALING FACTORS')

float_features_to_scale = [
    'dur', 'sbytes', 'dbytes', 'Sload', 'Dload', 'swin', 'res_bdy_len',
    'Sjit', 'Djit', 'Stime', 'Sintpkt', 'Dintpkt', 'tcprtt',
]


for f in float_features_to_scale:

    avg = sum(pcap_baseline[f])/len(pcap_baseline)
    avg_learning = sum(learning_data_baseline[f])/len(pcap_baseline)

    ratio = avg / avg_learning

    print(f, ratio)

    pcap_baseline_scaled[f] *= ratio 
    pcap_also_attacks_scaled[f] *= ratio

int_features_to_scale = [
    'smeansz', 'dmeansz', 'trans_depth', 'ct_state_ttl', 'ct_flw_http_mthd', 
    'ct_srv_src', 'ct_dst_ltm'
]

for f in int_features_to_scale:

    avg = sum(pcap_baseline[f])/len(pcap_baseline)
    avg_learning = sum(learning_data_baseline[f])/len(pcap_baseline)

    ratio = avg / avg_learning

    print(f, ratio)

    pcap_baseline_scaled[f] = round(ratio * pcap_baseline_scaled[f])
    pcap_also_attacks_scaled[f] = round(ratio * pcap_also_attacks_scaled[f])



print('\nPCAP BASELINE WITHOUT SCALING')

binary_labels = binary_model.predict(pcap_baseline)
plot(
    ['Attack' if x == 1 else 'Normal' for x in binary_labels], 
    title = 'Binary classification of the pcap_baseline without scaling'
)

print('false positive [%]: ', (sum(binary_labels)/len(binary_labels))*100)


print('\nBASELINE')

binary_labels = binary_model.predict(pcap_baseline_scaled)
plot(
    ['Attack' if x == 1 else 'Normal' for x in binary_labels], 
    title = 'Binary classification of the pcap_baseline (only normal traffic)'
)

print('false positive [%]: ', (sum(binary_labels)/len(binary_labels))*100)
print('accuracy on baseline [%]: ', (1-sum(binary_labels)/len(binary_labels))*100)


print('\nATTACKS')

binary_labels = binary_model.predict(pcap_also_attacks_scaled)
labels = multiclass_model.predict(pcap_also_attacks_scaled)
labels[binary_labels == 0] = "Normal"

plot(labels, title = 'Classification of the pcap')
