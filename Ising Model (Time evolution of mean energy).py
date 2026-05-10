import numpy as np
import matplotlib.pyplot as plt
import random
import copy
import seaborn as sns
import math
N = 30
L=500
k_B=1
T=10
Xk = [1] * N

def X_kEnergy(config): #tabe mohasebeye energie har listi k bkhahim , har listi na lozuman list avalie
    energy_config=0
    N=len(config)
    for i in range (N):
        j=(i+1)%N
        energy_config+=config[i]*config[j]
    return -energy_config
#print(X_kEnergy(Xk))
def EnergyDif(initial_list,trial_list): #tafavot energie list avalie(ghabli dar har marhale) va trial list
    energy_value_initial = X_kEnergy(initial_list)
    energy_value_trial = X_kEnergy(trial_list)
    DeltaE=-energy_value_initial - (-energy_value_trial)
    return DeltaE
def P(initial_list,trial_list,k_B,T):
    DeltaE=EnergyDif(initial_list,trial_list)
    probability=np.exp(-DeltaE/(k_B*T))
    return probability
def trial_maker(source_list): #sakhte yek list trial (yek spin flip emal shode nesbat be list ghabli)
    index_to_change = random.randint(0, len(source_list) - 1)
    X_trial=copy.deepcopy(source_list)
    X_trial[index_to_change] *= -1 #in yani alamate un onsor zarbdar manfi shavad na lozuman 1 b -1 tabdil shavad
    return X_trial
def examiner (source_list,trial_list):
    r=random.uniform(0,1)
    DeltaE=EnergyDif(source_list,trial_list)
    probability=P(source_list,trial_list,k_B,T)
    if DeltaE <= 0:
        return True
    elif probability >= r:
        return True
    else: #(in line lozumi nadarad , chon agar ghabliha sadegh bashand khode tabe az tabe kharej mishavad va agar ham sadesgh nabashand b har tartib kharej mikonad)
        return False

# for i in range(1000):
    # codi ke hezar bar anjam mishe

# while SHART: ta vaghti ke SHART bargharar BASHE
    # codi ke ta bargharari yek shart anjam beshe hey
aaallenergy = []
for j in range(100):
    random.seed()
    allconfig = [Xk]
    allenergy = [-30]
    for i in range(1000):
        X_trial= trial_maker(allconfig[i]) # ye dune X_trial aval mikhaym ke avvalin bar sharto check mikone bedune X_trial chi hast asan
        #in ham doros ast: X_trial = trial_maker(allconfig[-1])
        while examiner (allconfig[i],X_trial) != True: # ta vaghti ke sharte jelo while barghar bashe (yani examiner != True) code dakhele while ejra mishe
            X_trial = trial_maker(allconfig[i]) # age goft na, ye X_trial jadid besaz. Enghad in karo bokon ta bege Are
        allconfig.append(X_trial)  #in triale taaid shde ast k dar marhaleye examine aval mishod X2 (X2=X_trial)
        allenergy.append(X_kEnergy(X_trial))
    aaallenergy.append(allenergy)
#how to convert a list to a matrix:
b=np.array(aaallenergy)
#print(b.shape)
a=np.array(allconfig)

# list_length = len(b[0])
# mean_energy = []
# for m in range(list_length):
#     total_at_position = sum(element[m] for element in b)
#     average_at_position = total_at_position / len(b)
#     mean_energy.append(average_at_position)
# print('mean energy=',mean_energy)

mean_energy = b.mean(axis=0) #ravesh mean gereftan tavasote numpy, axis=0 yani miangin giri ruye satrha va axis=1 yani ruye sotunha
# Monte carlo error is: std / sqrt(num_simulations)
std = b.std(axis=0)
monte_carlo_error = std/10

# raveshe 2 (dasti)
# np.sqrt(((b**2).mean(axis=0) - b.mean(axis=0)**2)/100)
#print(me)
#print(me.shape)

#print(b)
#print(a)
# baraks kardane matrix
# a[::-1]


# plt.figure(figsize=(15, 20))
# myplot = sns.heatmap(a[::-5], cmap='crest', cbar=False)
# myplot.set_xticks(np.arange(0, 30), labels = np.arange(0, 30))
# myplot.set_yticks(np.arange(0, 101))
# myplot.set_yticklabels(reversed(np.arange(0, 101)))
# #plt.xticks(np.arange(0,30, 2))
#
# plt.show()

plt.figure(figsize=(20, 15))
Numebr_of_flips= list(range(1, 1002))
plt.plot(Numebr_of_flips,mean_energy)
plt.xticks(np.arange(0,1001, 100))
plt.xlabel('Time(Trial Flips)')
plt.ylabel('Mean Energy')
plt.title(r'$k_{B}T=10$')
plt.show()

plt.figure(figsize=(20, 15))
Numebr_of_flips= np.arange(1,1002)
plt.plot(Numebr_of_flips,monte_carlo_error)
plt.xticks(np.arange(0,1001, 100))
plt.xlabel('Time(Trial Flips)')
plt.ylabel('Monte Carlo erro')
plt.title(r'$k_{B}T=10$')
plt.show()

#X_trial2=trial_maker(X2)
# while examiner (X2,X_trial2) != True:
#     print("Nashod")
#     X_trial2=trial_maker(X2)
# X3=X_trial2
# print(X3)
plt.plot
