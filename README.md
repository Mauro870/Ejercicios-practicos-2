Ejercicio práctico clase 

E1: Diseñe una aplicación para obtener datos de sitios web en internet a través de
peticiones de tipo "GET". El sitio web envía una respuesta luego de que se le hace una
petición GET, de dicha respuesta se debe extraer cierta información detallada del sitio
tal como: el servidor en el que está alojado el sitio, el tipo de codificación del
contenido, el tipo de contenido, la IP pública del sitio, etc. La información recopilada
debe ser almacenada de forma que se pueda disponer de ella a través de una
persistencia (base de datos, almacenamiento físico, etc), es decir que la información
se debe encapsular en cierto tipo de objetos definidos por el usuario.
Indicaciones útiles:

Diseñe una clase que tenga métodos que implementen las distintas funciones que
requiere la aplicación, por ejemplo, recibir la lista de sitios que se van a consultar,
hacer la petición GET a un sitio, discriminar la información requerida de la respuesta
recibida a la petición, etc.

La clase mencionada anteriormente debería contar con atributos, tanto variables de
clase como de instancia, para ir almacenando información que sea relevante, tanto
para los resultados finales de la aplicación como información que deba compartirse
entre los distintos métodos de la clase.
