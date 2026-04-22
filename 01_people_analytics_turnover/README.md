# 🔍 People Analytics: Predicción de Rotación Voluntaria

> **Stack:** Python · Pandas · Scikit-learn · XGBoost · Matplotlib  
> **Dataset:** IBM HR Analytics Employee Attrition & Performance (1,470 empleados)  
> **Mejor modelo:** Logistic Regression — AUC 0.82 · F1 0.42 (umbral 0.35)

---

## Objetivo

Predecir qué empleados tienen mayor probabilidad de renunciar voluntariamente, integrando modelado predictivo con un marco sociológico para traducir los resultados en intervenciones de RRHH concretas y diferenciadas.

---

## Hallazgos Clave

| Insight | Dato | Implicancia |
|---|---|---|
| Horas extra = principal predictor | 3.4× más riesgo | Gestión de carga de trabajo |
| Ingreso mediano: +$5,500 para quienes se quedan | Efecto protector claro | Política salarial = retención |
| Los primeros 3 años son críticos | Rotación cae tras año 3 | Onboarding estratégico |
| Perfil "Quemado" y "Desenganchado" | 40%+ de rotación | Intervenciones diferenciadas |

---

## Perfiles Sociológicos Identificados

| Perfil | N | Rotación | Marco teórico |
|---|---|---|---|
| 🔥 Quemado | 39 | 41% | Modelo Demanda-Control (Karasek) |
| 😶 Desenganchado | 40 | 40% | Teoría del Engagement (Kahn) |
| ⏳ Estancado | 307 | 12% | Movilidad interna (Sicherman) |
| ✅ Estable | 1,084 | 16% | Línea base |

---

## Modelos Entrenados

| Modelo | AUC | F1 | Average Precision |
|---|---|---|---|
| Logistic Regression | **0.820** | 0.422 | **0.638** |
| XGBoost | 0.806 | 0.463 | 0.519 |
| Random Forest | 0.793 | **0.508** | 0.424 |

> Umbral ajustado a **0.35** para compensar el desbalance de clases.

---

## Feature Engineering

```python
SatisfactionIndex = media(JobSat + EnvSat + RelSat + WLB) / 4  # Herzberg
OverloadScore     = f(HorasExtra, RotaciónLaboral, WLB_bajo)    # Karasek
StagnationScore   = f(SinPromoción, RolEstancado, NivelJunior)  # Sicherman
IncomeGap         = z-score del salario vs peers del mismo rol   # Adams
```

---

## Estructura del Repositorio

```
01_people_analytics_turnover/
├── notebook.ipynb
├── data/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
├── figures/
│   ├── 01_attrition_overview.png
│   ├── 02_correlations.png
│   ├── 03_perfiles_sociologicos.png
│   ├── 04_eda_key_vars.png
│   ├── 05_roc_curves.png
│   ├── 06_feature_importance.png
│   ├── 07_confusion_matrix.png
│   └── 08_risk_business_impact.png
└── README.md
```

---

## Cómo Reproducir

```bash
pip install pandas numpy scikit-learn xgboost matplotlib seaborn scipy
jupyter notebook notebook.ipynb
```

---

## ¿Por qué importa este análisis?
Las organizaciones suelen tratar la rotación de personal como un problema de recursos humanos operativo —una métrica más en un dashboard. Sin embargo, cada salida voluntaria representa un costo real: se estima que reemplazar a un empleado cuesta entre el 50% y el 200% de su salario anual, considerando reclutamiento, onboarding y la productividad perdida durante la transición.

Lo que este proyecto propone es un cambio de perspectiva: la rotación no es un evento aleatorio, sino el resultado de procesos sociales acumulativos que pueden anticiparse.

Integrar teoría sociológica al modelado predictivo permite ir más allá de saber quién va a rotar, para entender por qué y, en consecuencia, qué hacer. Un empleado que rota porque está sobrecargado de horas extra necesita una intervención completamente diferente a uno que lleva cinco años sin una promoción. Tratarlos igual no solo es ineficiente: es contraproducente.

Los cuatro perfiles identificados en este análisis —Quemado, Desenganchado, Estancado y Estable— permiten a los equipos de People & Culture priorizar recursos donde el impacto es mayor. El modelo de impacto económico muestra que, con un umbral de clasificación bien calibrado, una empresa de tamaño mediano podría evitar costos de reemplazo de varios cientos de miles de dólares anuales, simplemente actuando antes de que la decisión de renunciar sea irreversible.

En síntesis, este proyecto demuestra que el análisis de datos no reemplaza el juicio humano en las organizaciones, sino que lo hace más informado, más oportuno y más justo.

## Próximos Pasos

- [ ] Survival Analysis (Cox Proportional Hazards)
- [ ] SHAP values para explicabilidad individual
- [ ] Dashboard en Streamlit para equipos de RRHH

---
*Portfolio de Data Science — People Analytics & Sociología Computacional*
