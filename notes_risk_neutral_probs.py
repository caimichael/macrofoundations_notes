# notes_risk_neutral_probs.m translation from matlab to python
# mike saint-antoine


# -------------------------------------------------------------------------
# Take arbitrary distribution over a state space and compute
# pricing kernel and risk neutral probabilities for power utility.
# Notation:  c^(1-alpha)/(1-alpha)
# Written by:  Dave Backus @ NYU
# -------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
import math

print(' ')
print('------------------------------------------------------------------')
print('Pricing kernel and risk-neutral probs with power utility')
print('------------------------------------------------------------------')
print(' ')

# disp(' ')
print('1. Basic inputs')
# risk aversion

alpha = 10
beta = 0.99
lambda_ = 1
# can't use lambda for a variable in python so i made it lambda_

# arbitrary state grid
zmax = 4
dz = 0.1




# generating z array
z = []
# had to multiply everything by 10 and then divide by 10 when appending to get rid of the .1 + .2 = .30000004 problem that computers have
i = -40
while i <=40:
    z.append(i/10)
    i = i + dz * 10


# nz = length(z);
# skewness and (excess) kurtosis
gamma1 = -0.5
gamma2 = 0.0

# Gram-Charlier distribution (normal if gamma1 = gamma2 = 0)

#p = exp(-z.^2/2).*(1 + gamma1*(z.^3-3*z)/6 + gamma2*(z.^4-6*z.^2+3)/24);

# generating p array from z array
p = []
for item in range(len(z)):
    p.append(math.exp(-z[item]**2/2)*(1 + gamma1*(z[item]**3-3*z[item])/6 + gamma2*(z[item]**4-6*z[item]**2+3)/24))


checkprobssum2one = sum(p)*dz/math.sqrt(2*math.pi)

# changing p array
probSum = sum(p)
for x in range(len(p)):
    p[x] = p[x]/probSum



#{
# Bernoulli (an alternative, comment out if not needed)
# have to change variable names since p is already used
z1 = [-1, 1]
p1 = [0.5, 0.5]
#}

# logg is a linear function of z
mug = 0.02
sigmag = 0.035

#logg = mug + sigmag*z;
# generating logg array
logg = []
for x in range(len(z)):
    logg.append(mug + sigmag * z[x])


# generating g array
g = []
for x in range(len(logg)):
    g.append(math.exp(logg[x]))


print(' ')
print('Properties of log g (check to see if we replicate inputs)')
print('mean, std, gamma1, gamma2')

# generating kappa1 array
kappa1 = []
for x in range(len(p)):
    kappa1.append(p[x]*logg[x])


# generating dev array
dev = []
for x in range(len(logg)):
    dev.append(logg[x]-kappa1[x])

# generating kappa2 array
kappa2 = []
for x in range(len(p)):
    kappa2.append(p[x]*dev[x]**2)

# generating kappa3 array
kappa3 = []
for x in range(len(p)):
    kappa3.append(p[x]*dev[x]**3)

# generating kappa4 array
kappa4 = []
for x in range(len(p)):
    kappa4.append(p[x]*dev[x]**4)


#[kappa1 sqrt(kappa2) kappa3/kappa2^1.5 kappa4/kappa2^2-3]
#
# pricing kernel
# generating m array
m = []
for x in range(len(g)):
    m.append(beta*g[x]**(-alpha))

print(m)

#m = beta*g.^(-alpha);
# entropy
print(' ')
print('Moments of log m (mean, std, gamma1, gamma2)')

# generating logm array
logm = []
for x in range(len(m)):
    logm.append(math.log(m[x]))


# for the next part a lot of the variables were already being used, so i had to change the names a little

kappa1_ = []
for x in range(len(p)):
    kappa1_.append(p[x]*logm[x])

dev_ = []
for x in range(len(logm)):
    dev_.append(logm[x]-kappa1_[x])

kappa2_ = []
for x in range(len(p)):
    kappa2_.append(p[x]*dev[x]**2)

kappa3_ = []
for x in range(len(p)):
    kappa3_.append(p[x]*dev[x]**3)

kappa4_ = []
for x in range(len(p)):
    kappa4_.append(p[x]*dev[x]**4)


# [kappa1 sqrt(kappa2) kappa3/kappa2^1.5 kappa4/kappa2^2-3]

Elogm = kappa1_

logEm = []
print(len(p))
print()
for x in range(len(p)):
    if (p[x]*m[x]) > 0:
    # had to add this cuz i was getting an error at the point where p*m becomes negative
        logEm.append(math.log(p[x]*m[x]))


Lm = []
for x in range(len(logEm)):
    Lm.append(logEm[x] - Elogm[x])



Lm_lognormal = []
for x in range(len(kappa2_)):
    Lm_lognormal.append(kappa2_[x]/2)



# p*

q1 = []
for x in range(len(p)):
    q1.append(p[x]*m[x])

q1 = sum(q1)

pstar = []
for x in range(len(p)):
    print(p[x]*m[x])
    pstar.append(p[x]*m[x]/q1)

checkonepstar = sum(pstar)

# equity

array = []
for x in range(len(p)):
    array.append(p[x]*m[x]*g[x])

qe = sum(array)



# Figures
FontSize = 12
FontName = 'Helvetica'  # or 'Times'
LineWidth = 1.5







# figure(1)
# bar(z, [p pstar])
# line([0 0], [-0.005 0.045])
# title('True (blue) and Risk-Neutral (red) Probabilities','FontSize',FontSize,'FontName',FontName)
# xlabel('State z','FontSize',FontSize,'FontName',FontName)
# ylabel('Probability density function','FontSize',FontSize,'FontName',FontName)
print(z)
print()
print(pstar)

plt.bar(z,p)
plt.bar(z,pstar)
plt.show()

print("done")
