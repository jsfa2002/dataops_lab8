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

## Estrategias de Escalabilidad del Pipeline

Escalar un pipeline de datos significa prepararlo para crecer. Por ejemplo hoy proceso 100 registros de ventas, pero mañana podrían ser 10,000 o incluso millones. Para lograrlo sin que todo colapse, implementamos cinco estrategias que trabajan juntas como un equipo coordinado.

**1. Orquestación Modular**

La orquestación modular es como armar con bloques de Lego en lugar de construir una pieza gigante. En el pipeline, dividimos el trabajo en componentes independientes: uno valida datos, otro los procesa, otro los enriquece. Cada pieza hace su trabajo específico y puede ser reemplazada, mejorada o reparada sin afectar al resto. Por ejemplo, si necesitamos cambiar cómo validamos los datos, solo modificamos ese módulo, el orquestador actúa coordinando cuándo y cómo cada componente debe ejecutarse, asegurándose de que todos trabajen en armonía y en el orden correcto.

**2. Paralelismo Controlado**

El paralelismo controlado es la capacidad de hacer varias cosas al mismo tiempo, pero con inteligencia. Por ejemplo si tenemos datos de ventas de 50 regiones diferentes, en lugar de procesarlas una por una, podemos procesarlas simultáneamente en grupos más pequeños. Sin embargo, no podemos lanzar todas las tareas al mismo tiempo porque saturaríamos la memoria y el procesador. Por eso es "controlado": definimos límites, como por ejemplo "procesar máximo 5 regiones a la vez". Esto acelera mucho el pipeline sin romper nada, aemás, si una región falla, las otras continúan procesándose normalmente.

**3. Uso de Contenedores**

Los contenedores son como cajas especiales que empaquetan todo lo que el pipeline necesita para funcionar: el código, las librerías, las configuraciones. Cuando empaquetamos el pipeline en un contenedor, usando tecnologías como Docker, aseguramos que funcionará exactamente igual en la computadora, en el servidor de pruebas y en producción. Esto elimina los momentos de "en mi computadora funciona pero en producción no", y facilita escalar el pipeline, porque puede crear múltiples copias idénticas del contenedor para manejar más carga.

**4. Logs Centralizados**

Los logs centralizados son una bitácora única donde se registra absolutamente todo lo que sucede en el pipeline. En lugar de tener archivos de log dispersos en diferentes computadoras o servicios, todos los mensajes (errores, advertencias, información de progreso) se envían a un lugar central. Cuando algo falla a las 3 AM, no tienes que buscar entre 10 archivos diferentes en 5 servidores distintos para entender qué pasó. Simplemente buscas en el sistema centralizado: "muéstrame todos los errores del pipeline de ventas en las últimas 2 horas". Esto ahorra tiempo valioso en debugging y permite detectar patrones de problemas que serían invisibles mirando logs individuales.

**5. Configuración Flexible**

La configuración flexible significa que el comportamiento del pipeline puede cambiar sin modificar el código. Todo lo importante (rutas de archivos, conexiones a bases de datos, umbrales de calidad) se define en archivos de configuración externos, como nuestro pipeline_config.yaml. Quieres procesar datos cada hora en lugar de cada día? Cambias la configuración. Necesitas conectar a una base de datos diferente? Cambias la configuración. Es como tener un panel de control con perillas y botones para ajustar el pipeline sin necesidad de ser programador. Esto es crítico para escalar porque diferentes entornos (desarrollo, pruebas, producción) necesitan configuraciones diferentes, y con este enfoque puedes manejar todos con el mismo código base.

## Preguntas de Reflexión

**1. Ventajas de la Orquestación**

La orquestación convierte un conjunto de scripts sueltos en un sistema profesional y confiable. Su primera gran ventaja es el control total: decides exactamente cuándo se ejecuta cada paso, en qué orden, y qué hacer si algo falla. No más "olvidé ejecutar este script" o "los ejecuté en el orden equivocado". La trazabilidad es otra ventaja clave: cada ejecución del pipeline genera un registro completo de qué pasó, cuándo pasó, y qué datos procesó. Si un reporte sale mal el martes, puedes revisar exactamente qué sucedió ese día. Finalmente, la automatización elimina el trabajo manual repetitivo y los errores humanos. Una vez configurado, el pipeline se ejecuta solo, a la hora exacta, todos los días, sin necesidad de que alguien lo active manualmente.

**2. Importancia de la Integración Continua (CI)**

La integración continua es como tener un inspector de calidad que revisa automáticamente cada cambio que haces en el código antes de que llegue a producción. Imagina que modificas la lógica de validación de datos y accidentalmente rompes algo. Sin CI, ese error llegaría a producción y afectaría a usuarios reales. Con CI, cada vez que subes un cambio a GitHub, se ejecutan automáticamente todas las pruebas: "¿el código sigue funcionando?", "¿las validaciones pasan?", "¿los reportes se generan correctamente?". Si algo falla, recibes una alerta inmediata y el código problemático nunca llega a producción. Esto te da confianza para hacer cambios frecuentes, porque sabes que hay una red de seguridad que atrapará los errores. En equipos de varias personas, el CI es aún más crítico porque evita que el código de un desarrollador rompa el trabajo de otro.

**3. Valor del Logging**

El logging es la memoria del pipeline. Cuando algo funciona bien, los logs registran el éxito y las métricas de rendimiento. Cuando algo falla, los logs son la diferencia entre resolver el problema en 10 minutos versus pasar horas buscando a ciegas. Los logs facilitan auditorías porque permiten responder preguntas como "¿cuántos registros procesamos el mes pasado?" o "¿cuándo comenzó a fallar la validación?". En la depuración, los logs son oro puro: te dicen exactamente en qué línea del código falló el proceso, qué datos estaba procesando, y qué error específico ocurrió. Además, con logs estructurados puedes generar métricas automáticas (velocidad de procesamiento, tasa de errores) que ayudan a optimizar el pipeline continuamente. Sin buenos logs, operas a ciegas; con ellos, tienes visibilidad total.

**4. Retos de Escalabilidad**

Escalar un pipeline no es solo "agregar más recursos". El primer reto es la concurrencia: cuando procesas múltiples tareas simultáneamente, aparecen problemas que no existían antes, como dos procesos intentando escribir en el mismo archivo o bloqueos en la base de datos. Resolver esto requiere diseñar cuidadosamente cómo se coordinan las tareas paralelas. El segundo reto es la distribución: cuando los datos crecen tanto que no caben en una sola máquina, necesitas distribuir el procesamiento entre múltiples servidores. Esto introduce complejidad en la coordinación, el manejo de fallos de red, y la sincronización de resultados. El tercer reto es el costo: más recursos cuestan más dinero. Debes encontrar el balance entre rendimiento y presupuesto, optimizando para procesar más datos con menos recursos. Además, al escalar, los pequeños ineficiencias del código se magnifican: una consulta lenta que no molestaba con 100 registros puede paralizar el sistema con un millón de registros.

**5. Aprendizaje del Laboratorio**

Este laboratorio integró tres pilares fundamentales de la ingeniería de datos moderna. Primero, la integración CI/CD enseña que el código no termina cuando funciona en tu computadora; debe funcionar automáticamente, con pruebas, en cualquier entorno. Ver cómo GitHub Actions ejecuta el pipeline, corre las pruebas, y reporta resultados automáticamente muestra el poder de la automatización. Segundo, la modularidad demuestra que dividir un problema complejo en componentes pequeños y especializados hace el sistema más fácil de entender, probar, y mantener. Cada módulo (validación, procesamiento, enriquecimiento) tiene una responsabilidad clara, lo que facilita encontrar y corregir problemas. Tercero, la escalabilidad enseña a pensar en el futuro: diseñar hoy para que el sistema pueda crecer mañana. Documentar estrategias de escalabilidad (de local a nube a distribuido) muestra que no existe una solución única para todos los casos, sino un camino evolutivo que se adapta según el volumen de datos y las necesidades del negocio. La lección más valiosa es que un buen pipeline no es solo código que funciona, es un sistema completo con automatización, monitoreo, documentación, y capacidad de crecer.

---

##  Autores

- **Juan Sebastián Fajardo Acevedo**
- **Profesora:** María José Torres

---

##  Referencias

- [GitHub Actions](https://docs.github.com/es/actions)
- [DataOps Principles](https://www.dataopsmanifesto.org/)
- [pytest](https://docs.pytest.org/en/stable/)

