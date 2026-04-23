import pandas as pd

# Cargar archivo de datos (modifica el nombre si es necesario)
df = pd.read_excel('tu_archivo.xlsx')

# ----------- LIMPIEZA Y TRANSFORMACIONES DEL WORKFLOW -----------

# Si existe la columna DGED, haz reemplazos masivos y luego renombra
if 'DGED' in df.columns:
    valores_a_eliminar = ['0', '124', '125', '15', '5', '9']
    df.loc[df['DGED'].astype(str).isin(valores_a_eliminar), 'DGED'] = ''
    df = df.rename(columns={'DGED': 'EDAD'})

# Renombrar otras columnas si existen
renombres = {
    'PTESXN': 'SEXO',
    'IDPTE': 'ID PACIENTE',
    'IDESTN': 'ESTABLECIMIENTO',
    'MFG': 'MORFOLOGIA',
    'MFGN': 'MORFOLOGIA LETRA',
    'COMP': 'COMPORTAMIENTO',
    'DIFHI': 'DIFERENCIA HISTORICA',
    'TOPO LETRA FINAL': 'TOPOGRAFIA LETRA FINAL',
    'TOPO FINAL': 'TOPOGRAFIA FINAL',
    'CTNM': 'TNM CLINICA',
    'PTNM': 'TNM PATOLOGICA',
    'FEULT': 'ULTIMO CONTROL',
    'FEDEF': 'FECHA DEFUNCION'
}
df = df.rename(columns={k: v for k, v in renombres.items() if k in df.columns})

# Limpiar espacios en MORFOLOGIA
if 'MORFOLOGIA' in df.columns:
    df['MORFOLOGIA'] = df['MORFOLOGIA'].astype(str).str.strip()

# Reemplazos en COMPORTAMIENTO
if 'COMPORTAMIENTO' in df.columns:
    df.loc[df['COMPORTAMIENTO'].astype(str).isin(['999', '-999']), 'COMPORTAMIENTO'] = ''

# Reemplazos en AÑO DIAG
if 'AÑO DIAG' in df.columns:
    df.loc[df['AÑO DIAG'].astype(str) == '#VALUE!', 'AÑO DIAG'] = ''
    df.loc[df['AÑO DIAG'].astype(str) == '1985', 'AÑO DIAG'] = ''

# Reemplazos en LATERALIDAD
if 'LATERALIDAD' in df.columns:
    df.loc[df['LATERALIDAD'].isin(['No', 'N/D']), 'LATERALIDAD'] = 'No especificado'

# Reemplazos en TNM CLINICA
if 'TNM CLINICA' in df.columns:
    reemplazos_tnm_clinica = {
        '...': '', 'N/A': '', 'IGN': '', 'IS': '0', '0is': '0',
        'LA': 'I', 'FigI': 'I', 'lb1': 'IIA', 'lb2': 'IIIA', 'FigIIA2': 'II'
    }
    df['TNM CLINICA'] = df['TNM CLINICA'].replace(reemplazos_tnm_clinica)

# Reemplazos en TNM PATOLOGICA
if 'TNM PATOLOGICA' in df.columns:
    reemplazos_tnm_pato = {
        '...': '', 'IGN': '', 'N/A': '', '0a': '0', '0is': '0', 'IS': '0',
        'FigI': 'I', 'FigIA': 'IA', 'FigIA1': 'IA', 'FigIB': 'IB', 'FigIB1': 'IB',
        'FigIB2': 'IB', 'FigIIA1': 'IIA', 'FigIVA': 'IVA'
    }
    df['TNM PATOLOGICA'] = df['TNM PATOLOGICA'].replace(reemplazos_tnm_pato)

# Reemplazos en DIFERENCIA HISTORICA
if 'DIFERENCIA HISTORICA' in df.columns:
    df.loc[df['DIFERENCIA HISTORICA'].astype(str).isin(['-999', '999']), 'DIFERENCIA HISTORICA'] = ''

# ----------- FILTRO POR EDAD -----------
if 'EDAD' in df.columns:
    df['EDAD'] = pd.to_numeric(df['EDAD'], errors='coerce')
    df = df[(df['EDAD'] > 17) & (df['EDAD'] <= 110) | df['EDAD'].isna()]

# ----------- CLASIFICACIÓN DE MORFOLOGÍA -----------
grupo_map = {
    'Adenocarcinoma': [8140,8143,8144,8145,8147,8154,8160,8210,8211,8230,8260,8263,8310,8312,8317,8330,8337,8380],
    'Carcinoma basocelular': [8090,8092,8093,8094,8095,8097,8102],
    'Carcinoma de células pequeñas': [8041,8046],
    'Carcinoma escamoso': [8050,8051,8070,8071,8072,8073,8076,8077,8081,8083,8084],
    'Carcinoma especializado': [8480,8490,8500,8501,8503,8510,8514,8520,8521,8522,8523,8524,8541,8550,8560,8562,8570,8573,8574,8575,8200,8201,8340,8350],
    'Carcinoma, SAI': [8010,8011,8012,8013,8020,8022,8031],
    'Linfoma/Leucemia': [9061,9063,9065,9070,9085,9591,9650,9652,9663,9673,9679,9680,9695,9698,9709,9731,9732,9740,9761,9800,9801,9823,9831,9861,9863,9866,9950,9960,9970,9989],
    'Melanoma': [8720,8721],
    'Neoplasia, SAI': [8000,8005],
    'Sarcoma': [8620,8700,8800,8801,8802,8850,8894,8900,8936,8950,8963,8964,8980,9013,9020,9044,9140,9150,9184,9240],
    'Tumor SNC': [9380,9400,9401,9420,9421,9440,9505,9530,9560],
    'Otros': [8270,8401,8430,8440,8441,8450,8460,8461,8463,8470,8246]
}
def map_grupo(valor):
    try:
        codigo = int(str(valor).split('.')[0]) # manejo str y float
    except:
        return ''
    for grupo, codigos in grupo_map.items():
        if codigo in codigos:
            return grupo
    return ''

if 'MORFOLOGIA' in df.columns:
    df['GRUPO MORFOLOGIA'] = df['MORFOLOGIA'].apply(map_grupo)

# ----------- GUARDAR RESULTADO -----------
df.to_excel('ONCOLOGIA-2018-A-2025-POLITECNICO-final-xlsx (1).xlsx',
            index=False,
            sheet_name='ONCOLOGIA 2018 A 2025 POLITECNI')

