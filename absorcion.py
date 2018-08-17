        fondo[i,1]=yerrfondo

#%%
mejor peron



absorcion=np.zeros((3648,3), dtype=float)
absorcion[:,0]=fondo[:,0]
absorcion[:,1]=-np.log(flu[:,1]/fondo[:,1])
absorcion[:,2]=((yerr/flu[:,1])**2+(yerrfondo/fondo[:,1])**2)**0.5

plt.errorbar(absorcion[:,0],absorcion[:,1],yerr=absorcion[:,2],fmt='g.', ecolor='g', ms=2,label='0,5um')
#plt.title('Emisión fluoresceína 5 uM')
#plt.xlabel('Longitud de onda [nm]')
#plt.ylabel('Intensidad [UA]')
#plt.xlim(350,550)
plt.legend(loc = 'best')
plt.savefig('absfluo', dpi=350)
#%%
flu=aR6G50
yerr=np.std(flu[0:500,1])
for i in range(len(flu[:,1])):
    if flu[i,1] <= yerr:
        flu[i,1]=yerr


absorcion=np.zeros((3648,3), dtype=float)
absorcion[:,0]=fondo[:,0]
absorcion[:,1]=-np.log(flu[:,1]/fondo[:,1])
absorcion[:,2]=((yerr/flu[:,1])**2+(yerrfondo/fondo[:,1])**2)**0.5

plt.errorbar(absorcion[:,0],absorcion[:,1],yerr=absorcion[:,2],fmt='b.', errorevery = 10, ecolor='b', ms=2, label='50um')
plt.title('Espectro de absorción de la rodamina')
plt.xlabel('Longitud de onda [nm]')
plt.ylabel('Absorbancia')
plt.xlim(350,700)
plt.ylim(-1.5,6)


flu=aR6G5
yerr=np.std(flu[0:500,1])
for i in range(len(flu[:,1])):
    if flu[i,1] <= yerr:
        flu[i,1]=yerr


absorcion=np.zeros((3648,3), dtype=float)
absorcion[:,0]=fondo[:,0]
absorcion[:,1]=-np.log(flu[:,1]/fondo[:,1])
absorcion[:,2]=((yerr/flu[:,1])**2+(yerrfondo/fondo[:,1])**2)**0.5

plt.errorbar(absorcion[:,0],absorcion[:,1],yerr=absorcion[:,2],fmt='r.', ecolor='r', ms=2,label='5um')
#plt.title('Emisión fluoresceína 5 uM')
#plt.xlabel('Longitud de onda [nm]')
#plt.ylabel('Intensidad [UA]')
#plt.xlim(350,550)


flu=aR6G
yerr=np.std(flu[0:500,1])
for i in range(len(flu[:,1])):
    if flu[i,1] <= yerr:
        flu[i,1]=yerr


absorcion=np.zeros((3648,3), dtype=float)
absorcion[:,0]=fondo[:,0]
absorcion[:,1]=-np.log(flu[:,1]/fondo[:,1])
absorcion[:,2]=((yerr/flu[:,1])**2+(yerrfondo/fondo[:,1])**2)**0.5

plt.errorbar(absorcion[:,0],absorcion[:,1],yerr=absorcion[:,2],fmt='g.', ecolor='g', ms=2,label='0,5um')
#plt.title('Emisión fluoresceína 5 uM')
#plt.xlabel('Longitud de onda [nm]')
#plt.ylabel('Intensidad [UA]')
#plt.xlim(350,550)
plt.legend(loc = 'best')
plt.savefig('absroda', dpi=350)

#%%

#dia 3


aFRET50b = np.loadtxt('BufFRET50uM0.005s3.csv', delimiter=',')
aFlu50b = np.loadtxt('BufFlu50uM0.005s3.csv', delimiter=',')
aR6G50b = np.loadtxt('BufR6G50uM0.005s3.csv', delimiter=',')
aR6G50 = np.loadtxt('AbsR6G50uM0.005s3.csv', delimiter=',')
aFlu50 = np.loadtxt('AbsFlu50uM0.005s3.csv', delimiter=',')
aFRET50 = np.loadtxt('AbsFRET50uM0.005s3.csv', delimiter=',')


f=np.loadtxt('Fondo0.5M0.0050sprom(ldo,int,err).csv', delimiter=',')
fondo=np.zeros((3648,3), dtype=float)
fondo[:,0]=f[0:3648]
fondo[:,1]=f[3648:7296]
yerrfondo=np.std(fondo[0:500,1])
for i in range(len(fondo[:,1])):
    if fondo[i,1] <= yerrfondo:
        fondo[i,1]=yerrfondo

#%%
flu=aFlu50
yerr=np.std(flu[0:500,1])
for i in range(len(flu[:,1])):
    if flu[i,1] <= yerr/10:
        flu[i,1]=yerr/10


absorcion=np.zeros((3648,3), dtype=float)
absorcion[:,0]=fondo[:,0]
absorcion[:,1]=-np.log(flu[:,1]/fondo[:,1])
absorcion[:,2]=((yerr/flu[:,1])**2+(yerrfondo/fondo[:,1])**2)**0.5

plt.errorbar(absorcion[:,0],absorcion[:,1],yerr=absorcion[:,2],fmt='b.',errorevery=10, ecolor='b', ms=2, label='Agua')
plt.title('Espectro de absorción de la fluoresceína 50 uM')
plt.xlabel('Longitud de onda [nm]')
plt.ylabel('Absorbancia')
plt.xlim(350,700)
#plt.ylim(-1.5,6)


flu=aFlu50b
yerr=np.std(flu[0:500,1])
for i in range(len(flu[:,1])):
    if flu[i,1] <= yerr:
        flu[i,1]=yerr


absorcion=np.zeros((3648,3), dtype=float)
absorcion[:,0]=fondo[:,0]
absorcion[:,1]=-np.log(flu[:,1]/fondo[:,1])
absorcion[:,2]=((yerr/flu[:,1])**2+(yerrfondo/fondo[:,1])**2)**0.5

plt.errorbar(absorcion[:,0],absorcion[:,1],yerr=absorcion[:,2],fmt='r.',errorevery=10, ecolor='r', ms=2,label='Buffer')
#plt.title('Emisión fluoresceína 5 uM')
#plt.xlabel('Longitud de onda [nm]')
#plt.ylabel('Intensidad [UA]')
#plt.xlim(350,550)
plt.legend(loc = 'best')
#plt.savefig('absflub', dpi=350)

#%%
flu=aR6G50
yerr=np.std(flu[0:500,1])
for i in range(len(flu[:,1])):
    if flu[i,1] <= yerr/2:
        flu[i,1]=yerr/2


absorcion=np.zeros((3648,3), dtype=float)
absorcion[:,0]=fondo[:,0]
absorcion[:,1]=-np.log(flu[:,1]/fondo[:,1])
absorcion[:,2]=((yerr/flu[:,1])**2+(yerrfondo/fondo[:,1])**2)**0.5

plt.errorbar(absorcion[:,0],absorcion[:,1],yerr=absorcion[:,2],fmt='b.',errorevery=10, ecolor='b', ms=2, label='Agua')
plt.title('Espectro de absorción de la rodamina 50 uM')
plt.xlabel('Longitud de onda [nm]')
plt.ylabel('Absorbancia')
plt.xlim(350,700)
#plt.ylim(-1.5,6)


flu=aR6G50b
yerr=np.std(flu[0:500,1])
for i in range(len(flu[:,1])):
    if flu[i,1] <= yerr:
        flu[i,1]=yerr


absorcion=np.zeros((3648,3), dtype=float)
absorcion[:,0]=fondo[:,0]
absorcion[:,1]=-np.log(flu[:,1]/fondo[:,1])
absorcion[:,2]=((yerr/flu[:,1])**2+(yerrfondo/fondo[:,1])**2)**0.5

plt.errorbar(absorcion[:,0],absorcion[:,1],yerr=absorcion[:,2],fmt='r.',errorevery=10, ecolor='r', ms=2,label='Buffer')
#plt.title('Emisión fluoresceína 5 uM')
#plt.xlabel('Longitud de onda [nm]')
#plt.ylabel('Intensidad [UA]')
#plt.xlim(350,550)
plt.legend(loc = 'best')
plt.savefig('absrodab', dpi=350)

#%%
flu=aFRET50
yerr=np.std(flu[0:500,1])
for i in range(len(flu[:,1])):
    if flu[i,1] <= yerr:
        flu[i,1]=yerr


absorcion=np.zeros((3648,3), dtype=float)
absorcion[:,0]=fondo[:,0]
absorcion[:,1]=-np.log(flu[:,1]/fondo[:,1])
absorcion[:,2]=((yerr/flu[:,1])**2+(yerrfondo/fondo[:,1])**2)**0.5

plt.errorbar(absorcion[:,0],absorcion[:,1],yerr=absorcion[:,2],fmt='b.',errorevery=10, ecolor='b', ms=2, label='Agua')
plt.title('Espectro de absorción de la mezcla 50 uM')
plt.xlabel('Longitud de onda [nm]')
plt.ylabel('Absorbancia')
plt.xlim(350,700)
#plt.ylim(-1.5,6)


flu=aFRET50b
yerr=np.std(flu[0:500,1])
for i in range(len(flu[:,1])):
    if flu[i,1] <= yerr:
        flu[i,1]=yerr


absorcion=np.zeros((3648,3), dtype=float)
absorcion[:,0]=fondo[:,0]
absorcion[:,1]=-np.log(flu[:,1]/fondo[:,1])
absorcion[:,2]=((yerr/flu[:,1])**2+(yerrfondo/fondo[:,1])**2)**0.5

plt.errorbar(absorcion[:,0],absorcion[:,1],yerr=absorcion[:,2],fmt='r.',errorevery=10, ecolor='r', ms=2,label='Buffer')
#plt.title('Emisión fluoresceína 5 uM')
#plt.xlabel('Longitud de onda [nm]')
#plt.ylabel('Intensidad [UA]')
#plt.xlim(350,550)
plt.legend(loc = 'best')
plt.savefig('absfretb', dpi=350)