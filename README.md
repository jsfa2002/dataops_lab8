#  Laboratorio 8 - Orquestación de Pipelines DataOps

Este proyecto implementa un laboratorio práctico de **DataOps**, enfocado en la **orquestación de pipelines**, la **automatización con CI/CD**, y la **verificación de calidad de datos**.  
El objetivo es simular el flujo de trabajo de una empresa que integra, valida y transforma datos antes de usarlos en análisis o dashboards.


## Estructura principal
- `src/` : código del orquestador y módulos de pipeline.
- `config/` : configuración YAML del pipeline.
- `data/` : datos de ejemplo (raw, schemas, outputs).
- `docs/` : diagramas y documentación requeridos por la guía.
- `tests/` : pruebas unitarias e integración.
- `.github/workflows/` : workflows para CI y CD.
- `scripts/` : utilidades (generar datos, validar config, reporte de ejecución)



## Estructura del Proyecto

<img width="221" height="574" alt="image" src="https://github.com/user-attachments/assets/ccca918f-6461-4175-bc45-ce60fc7b632d" />
   

---

##  Ejecución local

1. Clona el repositorio:

```bash
git clone https://github.com/jsfa2002/dataops_lab8.git
cd dataops_lab8
```

2. Crea un entorno virtual y activa:

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Instala dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecuta el pipeline principal:
```bash
python src/orchestrator.py
```

---

##  Estrategias de Escalabilidad

1. **Orquestación modular**
2. **Paralelismo controlado**
3. **Uso de contenedores**
4. **Logs centralizados**
5. **Configuración flexible**

---

##  Preguntas de Reflexión

1. **Ventajas de la orquestación:** Control, trazabilidad, automatización.  
2. **Importancia de CI:** Detectar fallos antes de desplegar.  
3. **Logging:** Facilita auditorías y depuración.  
4. **Retos de escalabilidad:** Concurrencia, distribución y costo.  
5. **Aprendizaje:** Integrar CI/CD, modularidad y escalabilidad.

---

##  Autores

- **Juan Sebastián Fajardo Acevedo**
- **Profesora:** María José Torres

---

##  Referencias

- [GitHub Actions](https://docs.github.com/es/actions)
- [DataOps Principles](https://www.dataopsmanifesto.org/)
- [pytest](https://docs.pytest.org/en/stable/)

