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

## Próximos Pasos

- [ ] Survival Analysis (Cox Proportional Hazards)
- [ ] SHAP values para explicabilidad individual
- [ ] Dashboard en Streamlit para equipos de RRHH

---
*Portfolio de Data Science — People Analytics & Sociología Computacional*
