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
En la acrpeta docs se encuentran los diagramas

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

## Test
<img width="1919" height="489" alt="image" src="https://github.com/user-attachments/assets/74ff4a54-d6aa-4e58-a1c6-51499bc9be3c" />

# Dependencias del Pipeline

- Validación: requiere esquema (`data/schemas/sales_schema_v1.json`) y archivos en `validation.required_files`
- Transformación: depende de validación exitosa
- Enriquecimiento: depende de procesado y requiere `data/raw/product_catalog.csv`
- Carga/Entregas: depende de enriquecimiento exitoso


## Estrategias de Escalabilidad del Pipeline

Escalar un pipeline de datos significa prepararlo para crecer. Hoy podemos procesar 100 registros de ventas, pero mañana podrían ser 10,000 o incluso millones. Para que el sistema no colapse al crecer, aplicamos cinco estrategias que trabajan juntas como un equipo coordinado.

**1. Orquestación Modular**

La orquestación modular es como construir con bloques de Lego en lugar de una sola pieza gigante. En nuestro pipeline dividimos el trabajo en partes independientes: una valida los datos, otra los procesa y otra los enriquece. Cada módulo hace su tarea específica y puede cambiarse o mejorarse sin afectar al resto.
El orquestador se encarga de coordinar cuándo y cómo se ejecuta cada módulo, asegurando que todo ocurra en el orden correcto y sin interferencias. Esto hace que el sistema sea más ordenado, flexible y fácil de mantener.

**2. Paralelismo Controlado**

El paralelismo controlado permite hacer varias tareas al mismo tiempo, pero sin sobrecargar el sistema. Por ejemplo, si tenemos datos de 50 regiones, no las procesamos una por una, sino en grupos más pequeños, como cinco regiones a la vez.
De esta forma el pipeline trabaja más rápido, pero sin saturar la memoria o el procesador. Además, si una región falla, las demás continúan sin problema. Este enfoque mejora mucho el rendimiento, manteniendo el control y la estabilidad del sistema.

**3. Uso de Contenedores**

Los contenedores son como cajas que guardan todo lo que el pipeline necesita: el código, las librerías y las configuraciones. Al usar tecnologías como Docker, garantizamos que el pipeline funcione igual en cualquier entorno, ya sea en la computadora, en pruebas o en producción.
Esto evita errores del tipo “en mi computadora funciona pero en producción no”, y facilita escalar, ya que se pueden crear varias copias idénticas del contenedor para procesar más datos al mismo tiempo.

**4. Logs Centralizados**

Los logs centralizados son como una bitácora única donde se registra todo lo que pasa en el pipeline. En vez de tener archivos de registro en distintos servidores, todo se guarda en un solo lugar.
Así, si ocurre un error, podemos buscarlo rápidamente sin revisar varios archivos. Esto ahorra tiempo, facilita encontrar fallas y ayuda a detectar patrones de error o lentitud que serían difíciles de ver de otra forma. También mejora el monitoreo general del sistema.

**5. Configuración Flexible**

La configuración flexible permite cambiar cómo se comporta el pipeline sin tener que modificar el código. Aspectos como las rutas de archivos, conexiones a bases de datos o frecuencias de ejecución se definen en archivos externos, como pipeline_config.yaml.
Esto permite adaptar el pipeline fácilmente a distintos entornos (desarrollo, pruebas o producción) usando el mismo código base. Es como tener un panel de control que te deja ajustar todo con unos pocos cambios.

## Preguntas de Reflexión
**1. Ventajas de la Orquestación**

La orquestación convierte varios scripts sueltos en un sistema automatizado y confiable, permite definir el orden exacto de ejecución, manejar errores correctamente y tener trazabilidad de cada paso. Además, reduce errores humanos y elimina la necesidad de ejecutar tareas manualmente, ya que el pipeline puede funcionar solo y de forma programada.

**2. Importancia de la Integración Continua (CI)**

La integración continua es como un inspector automático que revisa el código cada vez que se hacen cambios, cuando subimos una actualización a GitHub, se ejecutan pruebas automáticas para comprobar que todo sigue funcionando.
así se evitan que errores nuevos lleguen a producción y da confianza para modificar o mejorar el código constantemente. En equipos grandes, la CI es clave para evitar que un cambio afecte el trabajo de otros.

**3. Valor del Logging**

El logging es la memoria del pipeline. Guarda los resultados de cada proceso, tanto los correctos como los errores. Gracias a los logs, se puede saber cuándo y por qué algo falló, o revisar el rendimiento general del sistema.
También permiten generar métricas como velocidad de procesamiento o tasas de error, lo que facilita mejorar el pipeline continuamente. Sin buenos logs, trabajaríamos a ciegas; con ellos, tenemos control total.

**4. Retos de Escalabilidad**

Escalar un pipeline no se trata solo de agregar más recursos. Uno de los principales retos es manejar tareas simultáneas sin generar conflictos o bloqueos. Otro es distribuir los datos entre varios servidores cuando son demasiado grandes para uno solo.
Además, más recursos significan más costos, por lo que se debe buscar el equilibrio entre rendimiento y presupuesto. Incluso pequeños errores en el código pueden causar grandes problemas al trabajar con millones de registros, por lo que optimizarlo es esencial.

**5. Aprendizaje del Laboratorio**


Este laboratorio enseñó tres conceptos fundamentales: automatización, modularidad y escalabilidad. La automatización con CI/CD demuestra que el código debe funcionar de forma estable en cualquier entorno. La modularidad facilita entender, probar y mantener cada parte del sistema.
Finalmente, la escalabilidad enseña a diseñar pensando en el futuro, asegurando que el pipeline pueda crecer según las necesidades del proyecto. En conjunto, todo esto muestra que un buen pipeline no solo procesa datos, sino que también es confiable, monitoreable y capaz de evolucionar con el tiempo.

---

##  Autores

- **Juan Sebastián Fajardo Acevedo**
- **Profesora:** María José Torres

---

##  Referencias

- [GitHub Actions](https://docs.github.com/es/actions)
- [DataOps Principles](https://www.dataopsmanifesto.org/)
- [pytest](https://docs.pytest.org/en/stable/)

