# Proyecto 3
## Tecnologías usadas
- Python 3
- Spark (PySpark)

## Dependencias de Python
- pandas
- matplotlib

## Ejemplo de graficar
```python
# Tenemos un dataframe de spark
colombia_by_state = colombia.groupBy('Departamento o Distrito ').count().orderBy('count', ascending=False)


# Pasamos el dataframe de spark a pandas
colombia_by_state_pandas = colombia_by_state.toPandas()[:10]
colombia_by_state_pandas.set_index("Departamento o Distrito ", inplace = True)

# Graficamos con matplolib
colombia_by_state_pandas.plot.bar(figsize=(10,6)).legend(["Comfirmed cases"])
plt.title('Top 10 of Colombian states with more comfirmed cases')
plt.show()
``` 

## Datos
- [Colombia](https://www.datos.gov.co)
- [Global](https://github.com/CSSEGISandData/COVID-19)