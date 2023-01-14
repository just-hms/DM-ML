
import pickle
import pandas as pd

from utils import plot

assets_folder = './../../assets/'

# load data to classify
learning_data = pd.read_csv(assets_folder + 'UNSW-NB15-preprocessed.csv', low_memory=False)
learning_data_baseline = learning_data[learning_data['Label'] == 0]

pcap_baseline = pd.read_csv(assets_folder + 'CC22-final-only-bots.csv').iloc[:, 1:30]
pcap_also_attacks = pd.read_csv(assets_folder + 'CC22-final-also-attacks.csv').iloc[:, 1:30]

pcap_baseline_scaled = pcap_baseline 
pcap_also_attacks_scaled = pcap_also_attacks
# load the models

models_folder = assets_folder + 'models/'

binary_model = pickle.load(open(models_folder + 'binary_model', 'rb'))
multiclass_model = pickle.load(open(models_folder + 'multiclass_model', 'rb'))

pca_model = pickle.load(open(models_folder + 'pca_model', 'rb'))
std_scaler = pickle.load(open(models_folder + 'std_scaler', 'rb'))

binary_pca_model = pickle.load(open(models_folder + 'binary_pca_model', 'rb'))
multiclass_pca_model = pickle.load(open(models_folder + 'multiclass_pca_model', 'rb'))

# scale features based on the dataset baseline
features_to_scale = [
    'dur', 'sbytes', 'dbytes', 'Sload', 'Dload', 'swin',  
    'Sjit', 'Djit', 'Stime', 'Sintpkt', 'Dintpkt', 'tcprtt',

    # integers
    'smeansz', 'dmeansz','ct_state_ttl', 'ct_flw_http_mthd', 
    'ct_srv_src', 'ct_dst_ltm'
]

for feature in features_to_scale:

    avg = sum(pcap_baseline[feature])/len(pcap_baseline)
    avg_learning = sum(learning_data_baseline[feature])/len(pcap_baseline)

    ratio = avg / avg_learning

    print(feature, ratio)

    pcap_baseline_scaled[feature] *= ratio 
    pcap_also_attacks_scaled[feature] *= ratio


print('\nBASELINE')

binary_labels = binary_model.predict(pcap_baseline_scaled)
plot(
    ['Attack' if x == 1 else 'Normal' for x in binary_labels], 
    title = 'Binary classification of the pcap_baseline (only normal traffic)'
)

print('\nATTACKS')

binary_labels = binary_model.predict(pcap_also_attacks_scaled)
plot(
    ['Attack' if x == 1 else 'Normal' for x in binary_labels], 
    title = 'Binary classification of the pcap'
)

labels = multiclass_model.predict(pcap_also_attacks_scaled[binary_labels != 0])
plot(labels, title = 'Multiclass classification of the pcap')

print('\n\nPCA\n\n')

print('\nBASELINE')

pcap_baseline_pca = pca_model.transform(std_scaler.transform(pcap_baseline_scaled))

binary_labels = binary_pca_model.predict(pcap_baseline_pca)
plot(
    ['Attack' if x == 1 else 'Normal' for x in binary_labels], 
    title = 'Binary classification of the pcap_baseline (only normal traffic)'
)

print('\nATTACKS')

pcap_also_attacks_pca = pca_model.transform(std_scaler.transform(pcap_also_attacks_scaled))

binary_labels = binary_pca_model.predict(pcap_also_attacks_pca)
plot(
    ['Attack' if x == 1 else 'Normal' for x in binary_labels], 
    title = 'Binary classification of the pcap using PCA'
)

labels = multiclass_pca_model.predict(pcap_also_attacks_pca[binary_labels != 0])
plot(labels, title = 'Multiclass classification of the pcap using PCA')