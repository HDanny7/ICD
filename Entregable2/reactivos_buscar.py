# Tabla d ereactivos y filtrado por volumen
import pandas as red
import numpy as np

data = {'reactivos' : ['acetona', 'acetato_etilo', 'alcohol_amilico', 'terbutanol', 'n_butanol', 'etanol', '2_propanol', 'metanol', 'acetato_amilo', 'acetato_metilo', '2_butanol', '2_butanona', 'ciclohexano', 'ciclohexanol', 'ciclohexeno', 'n_butilo', 'sec_butilo', 'terbutilo', 'dietilenglicol', 'eter_etilico', 'etilenglicol', 'hexano', 'metanol', 'tolueno', 'pentanol'],
'numero_cas' : ['67-64-1', '141-78-6', '71-41-0', '75-65-0', '71-36-13', '64-17-5', '67-63-0', '67-56-1', '628-63-7', '79-20-9', '78-92-2', '78-93-3', '110-82-7', '108-93-0', '110-83-8', '109-69-3', '78-86-4', '507-20-0', '111-46-6', '60-29-7', '107-21-1', '110-54-3', '67-56-1', '108-88-3', '6032-29-7'],
'volumen' : [874.2, 6748, 4748.3, 4728, 3657, 9649.9, 1092, 9860, 1542.4, 8764, 5969, 6252.7, 3480, 948.8, 6532, 7272, 8584.1, 4738, 2639.7, 4788, 793, 6838, 9484, 8575.5, 3729]}
df = red.DataFrame(data)
print(df[df['reactivos'] == 'acetona'])