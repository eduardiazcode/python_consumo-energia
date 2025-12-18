# Analizador de Consumo de Energía Eléctrica (ESAMC)

Este programa es una herramienta de consola desarrollada en Python para procesar y analizar el consumo mensual de energía eléctrica en una ciudad, categorizando los datos por tipo de consumidor.

## 📋 Descripción del Proyecto
El script permite ingresar datos de múltiples consumidores de forma iterativa, calculando automáticamente estadísticas críticas como consumos máximos, mínimos, totales por sector y promedios industriales.

Este proyecto fue desarrollado originalmente como parte de la disciplina de **Lógica de Programación y Algoritmos** en la ESAMC - Faculdade de Sorocaba (2020).

## 🚀 Funcionalidades
- **Categorización:** Clasificación en tipos Residencial (R), Comercial (C) e Industrial (I).
- **Cálculo de Extremos:** Identifica el mayor y menor consumo en el sector residencial.
- **Seguimiento de Máximos:** Identifica el mayor consumo en los sectores comercial e industrial.
- **Acumulación de Datos:** Calcula el total de kWh consumidos por cada sector individualmente.
- **Análisis Estadístico:** Calcula la media general del consumo en el sector industrial.

## 💻 Instrucciones de Uso
1. Ejecuta el archivo con Python:
   ```bash
   python nombre_del_archivo.py